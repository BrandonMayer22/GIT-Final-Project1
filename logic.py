from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic:
    def __init__(
        self, ui_login, ui_help, ui_ballot, window_login, window_help, window_ballot
    ):
        # self.current_window = None
        self.ui_login = ui_login
        self.ui_help = ui_help
        self.ui_ballot = ui_ballot
        self.window_login = window_login
        self.window_help = window_help
        self.window_ballot = window_ballot
        self.setup_connections()

    def setup_connections(self):
        self.ui_login.pushButton.clicked.connect(self.validate_login)
        self.ui_help.pushButton_forward.clicked.connect(self.fwd_button_clicked)

    def show_login(self):
        if self.current_window:
            self.current_window.close()

        self.current_window = QWidget()
        self.login_ui = Ui_LoginWindow()
        self.login_ui.setupUi(self.current_window)
        self.current_window.show()

    def show_help_page(self):
        # if self.current_window:
        #     self.current_window.close()

        self.current_window = QMainWindow()
        self.help_ui = Ui_help_page()
        self.help_ui.setupUi(self.current_window)
        self.current_window.show()

    def show_ballot_page(self):
        # if self.current_window:
        #     self.current_window.close()

        self.current_window = QMainWindow()
        self.ballot_ui = Ui_ballot()
        self.ballot_ui.setupUi(self.current_window)
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

                        self.window_login.close()
                        self.show_help_page()
                        break
                    else:

                        self.ui_login.label_5.setText("Incorrect PIN entered")
                        self.ui_login.label_5.setVisible(True)
                        break

            if not found:

                self.ui.label_5.setText("Voter ID not registered")
                self.ui.label_5.setVisible(True)

    def fwd_button_clicked(self):
        self.hide_current_page()
        self.show_ballot_page()
