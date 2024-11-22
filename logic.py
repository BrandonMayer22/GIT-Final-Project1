from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from gui import *
import csv, os


class Logic:
    def __init__(
        self,
        ui_login,
        ui_help,
        ui_ballot,
        ui_notice_box,
        window_login,
        window_help,
        window_ballot,
        window_notice_box,
    ):
        self.ui_login = ui_login
        self.ui_help = ui_help
        self.ui_ballot = ui_ballot
        self.ui_notice_box = ui_notice_box
        self.window_login = window_login
        self.window_help = window_help
        self.window_ballot = window_ballot
        self.window_notice_box = window_notice_box
        self.current_window = None

        # Disable minimize and close buttons for the notice_box window
        flags = self.window_notice_box.windowFlags()
        flags &= ~QtCore.Qt.WindowType.WindowMinimizeButtonHint
        flags &= ~QtCore.Qt.WindowType.WindowCloseButtonHint
        flags &= ~QtCore.Qt.WindowType.WindowMaximizeButtonHint
        self.window_notice_box.setWindowFlags(flags)

    # Initialize CSV if it doesn't exist
    if not os.path.exists("vote_data.csv"):
        with open("vote_data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Voter ID", "Presidential Vote", "Senate Vote", "House Vote"]
            )

    def show_login(self):
        print("Setting up login page...")
        if self.current_window:
            self.current_window.close()
            self.current_window = None

        self.current_window = QWidget()
        self.login_ui = Ui_LoginWindow()
        self.login_ui.setupUi(self.current_window)
        self.ui_login = self.login_ui
        print("Login UI setup complete!")
        self.ui_login.pushButton.clicked.connect(self.validate_login)
        print("Login button connection established!")
        print("\n")
        self.current_window.show()

    def show_help_page(self):
        print("Setting up help page...")
        if self.current_window:
            self.current_window.close()
            self.current_window = None

        self.current_window = QMainWindow()
        self.help_ui = Ui_help_page()
        self.help_ui.setupUi(self.current_window)
        self.ui_help = self.help_ui
        print("Help UI setup complete!")
        self.ui_help.pushButton_forward.clicked.connect(self.fwd_button_clicked)
        print("Forward button connection established!")
        print("\n")
        self.current_window.show()

    def show_ballot_page(self):
        print("Setting up ballot page...")
        if self.current_window:
            self.current_window.close()
            self.current_window = None

        self.current_window = QMainWindow()
        self.ballot_ui = Ui_ballot()
        self.ballot_ui.setupUi(self.current_window)
        self.ui_ballot = self.ballot_ui
        print("Ballot UI setup complete!")
        self.ui_ballot.pushButton_voteballot.clicked.connect(self.vote_button_clicked)
        print("Vote button connection established!")
        self.ui_ballot.pushButton_back.clicked.connect(self.back_button_clicked)
        print("Back button connection established!")
        print("\n")
        self.current_window.show()

    def validate_login(self):
        voter_id = self.ui_login.lineEdit.text().strip()
        pin = self.ui_login.lineEdit_2.text().strip()

        found = False
        with open("login_credentials.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Voter ID"] == voter_id:
                    found = True
                    if row["PIN"] == pin:
                        self.voter_id = voter_id
                        if self.voter_history():
                            return
                        self.window_login.close()
                        self.show_help_page()
                        break
                    else:
                        self.ui_login.label_5.setText("Incorrect PIN entered")
                        self.ui_login.label_5.setVisible(True)
                        break

        if not found:
            self.ui_login.label_5.setText("Voter ID not registered")
            self.ui_login.label_5.setVisible(True)

    def fwd_button_clicked(self):
        print("Forward button clicked")
        self.show_ballot_page()

    def voter_history(self):
        print("Voter history requested")
        with open("vote_data.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Voter ID"] == self.voter_id:
                    self.ui_notice_box.label_notification.setText(
                        "This Voter ID has already cast a vote. Please see poll worker if assistance is required. Thank you!"
                    )
                    self.show_notice_box(close_login=True)
                    return True
        return False

    def show_notice_box(self, close_login=False):
        print("Setting up notice box...")
        # Create the QMessageBox instance
        msg_box = QMessageBox()

        # Set up the message box
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Notice")

        red_text = (
            "<font color='red'>"
            + self.ui_notice_box.label_notification.text()
            + "</font>"
        )
        msg_box.setText(red_text)

        # Add an "Close" button
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)

        # Connect the button's click event to close the message box
        msg_box.buttonClicked.connect(self.close_notice_button_clicked)

        # Show the message box
        msg_box.exec()

        # Optionally close login window if needed
        if close_login:
            self.window_login.close()

    def close_notice_button_clicked(self):
        print("Close button clicked, closing the notice box.")

        self.window_notice_box.close()

    def vote_button_clicked(self):
        """Handle vote submission."""

        # Collect votes
        pres_vote = self._get_selected_vote(self.ui_ballot, "pres")
        sen_vote = self._get_selected_vote(self.ui_ballot, "sen")
        house_vote = self._get_selected_vote(self.ui_ballot, "house")

        # Write to CSV
        with open("vote_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.voter_id, pres_vote, sen_vote, house_vote])

        print("Closing ballot window now...")
        self.window_ballot.close()
        print("Ballot window closed.")

        # Set the message for the notice box
        self.ui_notice_box.label_notification.setText(
            "You have successfully cast your vote!"
        )

        # Show the notice box as a QMessageBox
        self.window_ballot.close()
        self.show_notice_box(close_login=False)
        self.show_login()

    def _get_selected_vote(self, ballot_ui, prefix):
        """Helper method to get the selected vote based on prefix."""
        if getattr(ballot_ui, f"checkBox_{prefix}opt1").isChecked():
            return getattr(ballot_ui, f"label_{prefix}opt1").text()
        elif getattr(ballot_ui, f"checkBox_{prefix}opt2").isChecked():
            return getattr(ballot_ui, f"label_{prefix}opt2").text()
        elif getattr(ballot_ui, f"checkBox_{prefix}writein").isChecked():
            return getattr(ballot_ui, f"lineEdit_{prefix}writein").text().strip()

        return "Abstain"

    def back_button_clicked(self):
        print("Back button clicked!")
        self.show_help_page()
