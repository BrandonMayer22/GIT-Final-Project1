from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from gui import *
import csv, os


class Logic:
    """
    Handles the application logic, including page transitions, user interactions,
    and background functionality for login, ballot casting, and voter history.
    """

    def __init__(
        self,
        ui_login: Ui_LoginWindow,
        ui_help: Ui_help_page,
        ui_ballot: Ui_ballot,
        ui_notice_box: Ui_notice_box,
    ) -> None:
        """
        Initializes the Logic class with UI components and window objects.

        Args:
            ui_login (Ui_LoginWindow): Login window UI.
            ui_help (Ui_help_page): Help page UI.
            ui_ballot (Ui_ballot): Ballot page UI.
            ui_notice_box (Ui_notice_box): Notice box UI.
            # window_login (QWidget): Login window object.
            # window_help (QMainWindow): Help page window object.
            # window_ballot (QMainWindow): Ballot page window object.
            # window_notice_box (QMessageBox): Notice box window object.
        """
        self.ui_login = ui_login
        self.ui_help = ui_help
        self.ui_ballot = ui_ballot
        self.ui_notice_box = ui_notice_box
        self.current_window: QWidget | None = None
        self.voter_id: str | None = None

        self.window_login = QWidget()
        self.window_help = QMainWindow()
        self.window_ballot = QMainWindow()
        self.window_notice_box = QMessageBox()

        # Disable minimize, maximize and close buttons for the notice_box window
        self.window_notice_box.setWindowFlags(
            self.window_notice_box.windowFlags()
            & ~Qt.WindowType.WindowMinimizeButtonHint
            & ~Qt.WindowType.WindowCloseButtonHint
            & ~Qt.WindowType.WindowMaximizeButtonHint
        )

        # Initialize CSV if it doesn't exist
        self.initialize_vote_data()

    # --------------------------------------------------------------------------------------------------------------------
    # Functions controlling the separate pages and their connections
    # --------------------------------------------------------------------------------------------------------------------
    def show_window(self, window: QWidget) -> None:
        """
        General method to handle window transitions for QWidget and QMainWindow.

        Args:
            window (QWidget): The window to show (could be QMainWindow or QWidget).
        """
        # Close any existing window
        if self.current_window:
            print(f"Closing window: {self.current_window.__class__.__name__}")
            self.current_window.close()

        # Set the current window to the new one and show it
        self.current_window = window
        self.current_window.show()

    def show_login(self) -> None:
        """Displays the login page."""
        print("Setting up login page...")

        self.ui_login.setupUi(self.window_login)
        print(f"Connecting {self.ui_login.pushButton.objectName()} to validate_login")

        self.ui_login.pushButton.clicked.connect(self.validate_login)
        print(f"Connection established for {self.ui_login.pushButton.objectName()}")

        self.window_login.show()

    def show_help_page(self) -> None:
        """Displays the help page."""

        self.ui_help.setupUi(self.window_help)

        print(
            f"Connecting {self.ui_help.pushButton_forward.objectName()} to fwd_button_clicked"
        )

        self.ui_help.pushButton_forward.clicked.connect(self.fwd_button_clicked)
        print(
            f"Connection established for {self.ui_help.pushButton_forward.objectName()}"
        )

        self.show_window(self.window_help)

    def show_ballot_page(self) -> None:
        """Displays the ballot page."""

        self.ui_ballot.setupUi(self.window_ballot)

        print(
            f"Connecting {self.ui_ballot.pushButton_voteballot.objectName()} to vote_button_clicked"
        )
        print(
            f"Connecting {self.ui_ballot.pushButton_back.objectName()} to back_button_clicked"
        )

        self.ui_ballot.pushButton_voteballot.clicked.connect(self.vote_button_clicked)
        self.ui_ballot.pushButton_back.clicked.connect(self.back_button_clicked)
        print(
            f"Connection established for {self.ui_ballot.pushButton_voteballot.objectName()}"
        )
        print(
            f"Connection established for {self.ui_ballot.pushButton_back.objectName()}"
        )

        self.show_window(self.window_ballot)

    def show_notice(self, close_login: bool = False) -> None:
        """
        Displays a notice box with a custom message.
        """
        print("Setting up notice box...")
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        msg_box.buttonClicked.connect(self.close_notice_button_clicked)
        msg_box.exec()

        if close_login:
            self.window_login.close()

    # --------------------------------------------------------------------------------------------------------------------
    # Background logic for login validation, voter history retrieval, ballot casting, CSV reader and writer functions.
    # --------------------------------------------------------------------------------------------------------------------
    def read_csv(self, file_path: str) -> list[dict]:
        """Reads a CSV file and returns its rows as a list of dictionaries."""
        try:
            with open(file_path, mode="r") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")
        except Exception as e:
            raise Exception(f"Error reading file '{file_path}': {e}")

    def write_csv(self, file_path: str, data: list[str]) -> None:
        """Writes a row of data to a CSV file."""
        try:
            with open(file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
        except Exception as e:
            raise Exception(f"Error writing to file '{file_path}': {e}")

    def initialize_vote_data(self) -> None:
        """
        Ensures that the `vote_data.csv` file exists and initializes it with headers if absent.
        """
        try:
            if not os.path.exists("vote_data.csv"):
                with open("vote_data.csv", mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            "Voter ID",
                            "Presidential Vote",
                            "Senate Vote",
                            "House Vote",
                        ]
                    )
                print("Initialized 'vote_data.csv' with headers.")
        except Exception as e:
            print(f"Error initializing 'vote_data.csv': {e}")

    def validate_login(self) -> None:
        """Validates user login credentials."""

        print("Validating login credentials.")

        voter_id = self.ui_login.lineEdit.text().strip()
        pin = self.ui_login.lineEdit_2.text().strip()
        print("Voter ID: {voter_id}, PIN: {pin}")

        try:
            reader = self.read_csv("login_credentials.csv")
            for row in reader:
                if row["Voter ID"] == voter_id:
                    if row["PIN"] == pin:
                        self.voter_id = voter_id
                        if self.voter_history():
                            return
                        self.window_login.close()
                        self.show_help_page()
                        return
                    else:
                        self.ui_login.label_5.setText("Incorrect PIN entered")
                        self.ui_login.label_5.setVisible(True)
                        return

            self.ui_login.label_5.setText("Voter ID not registered")
            self.ui_login.label_5.setVisible(True)
        except FileNotFoundError:
            self.display_error("Login credentials file is missing.")
        except Exception as e:
            self.display_error(f"An error occurred: {e}")
            print(f"Error validating login: {e}")

    def voter_history(self) -> bool:
        """
        Checks if the voter has already voted.

        Returns:
            bool: True if the voter has already voted, False otherwise.
        """

        try:
            rows = self.read_csv("vote_data.csv")
            for row in rows:
                if row["Voter ID"] == self.voter_id:
                    self.display_error(
                        "This Voter ID has already cast a vote. Please see a poll worker if assistance is required. Thank you!"
                    )
                    return True
        except FileNotFoundError:
            self.display_error(
                "Vote data file is missing. Please contact an administrator."
            )
        except Exception as e:
            self.display_error(f"An error occurred: {e}")

        return False

    def _get_selected_vote(self, ballot_ui: Ui_ballot, prefix: str) -> str:
        """
        Retrieves the selected vote for a specific category.

        Args:
            ballot_ui (Ui_ballot): The ballot UI instance.
            prefix (str): The prefix for the vote category (e.g., "pres", "sen").

        Returns:
            str: The selected vote or "Abstain" if no option is selected.
        """
        if getattr(ballot_ui, f"checkBox_{prefix}opt1").isChecked():
            return getattr(ballot_ui, f"label_{prefix}opt1").text()
        elif getattr(ballot_ui, f"checkBox_{prefix}opt2").isChecked():
            return getattr(ballot_ui, f"label_{prefix}opt2").text()
        elif getattr(ballot_ui, f"checkBox_{prefix}writein").isChecked():
            return getattr(ballot_ui, f"lineEdit_{prefix}writein").text().strip()

        return "Abstain"

    def display_error(self, message: str, close_login: bool = False) -> None:
        """
        Displays an error message using the notice box and optionally closes the login window.

        Args:
            message (str): The error message to display.
            close_login (bool): Whether to close the login window after showing the error.
        """
        # Create a message box to show the error
        msg_box = QMessageBox()
        msg_box.setIcon(
            QMessageBox.Icon.Critical
        )  # You can set the icon to error (Critical)
        msg_box.setText(message)  # Set the error message
        msg_box.setWindowTitle("Error")  # Optionally set a window title
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.buttonClicked.connect(
            self.close_notice_button_clicked
        )  # If you want a button action
        msg_box.exec()

        if close_login:
            self.window_login.close()

    # --------------------------------------------------------------------------------------------------------------------
    # Application buttons logic and transitions
    # --------------------------------------------------------------------------------------------------------------------
    def fwd_button_clicked(self) -> None:
        """Handles the forward button click event."""
        print("Forward button clicked")
        self.show_ballot_page()

    def close_notice_button_clicked(self) -> None:
        """Closes the notice box."""
        print("Close button clicked, closing the notice box.")

        self.window_notice_box.close()

    def vote_button_clicked(self) -> None:
        """Handle vote submission."""

        # Collect votes
        pres_vote = self._get_selected_vote(self.ui_ballot, "pres")
        sen_vote = self._get_selected_vote(self.ui_ballot, "sen")
        house_vote = self._get_selected_vote(self.ui_ballot, "house")

        # Write to CSV
        try:
            self.write_csv(
                "vote_data.csv", [self.voter_id, pres_vote, sen_vote, house_vote]
            )
            print("Vote data written to 'vote_data.csv'")
        except Exception as e:
            print(f"Error writing vote data: {e}")

        print("Closing ballot window now...")
        self.window_ballot.close()
        print("Ballot window closed.")

        # Display success message
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("You have successfully cast your vote!")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)
        msg_box.buttonClicked.connect(self.close_notice_button_clicked)
        msg_box.exec()

        self.window_login.show()

    def back_button_clicked(self) -> None:
        """Handles the back button click event."""
        print("Back button clicked!")
        self.show_help_page()
