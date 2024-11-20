from logic import *


def main():
    app = QApplication([])

    ui_login = Ui_LoginWindow()
    ui_help = Ui_help_page()
    ui_ballot = Ui_ballot()

    window_login = QWidget()  # Main window for the login UI
    ui_login.setupUi(window_login)  # Set up the UI for the login window

    window_help = QMainWindow()  # Main window for the help page UI
    ui_help.setupUi(window_help)  # Set up the UI for the help page

    window_ballot = QMainWindow()  # Main window for the help page UI
    ui_help.setupUi(window_ballot)

    # Create the Logic instance for the login UI and pass both UIs to it
    logic = Logic(
        ui_login, ui_help, ui_ballot, window_login, window_help, window_ballot
    )

    # Store the Logic instance in the UI
    ui_login.logic = logic

    # Show the login window
    window_login.show()

    app.exec()


if __name__ == "__main__":
    main()
