from logic import *


def main():
    app = QApplication([])

    ui_login = Ui_LoginWindow()
    ui_help = Ui_help_page()
    ui_ballot = Ui_ballot()
    ui_notice_box = Ui_notice_box()

    window_login = QWidget()  # Main window for the login UI
    ui_login.setupUi(window_login)  # Set up the UI for the login window

    window_help = QMainWindow()  # Main window for the help page UI
    ui_help.setupUi(window_help)  # Set up the UI for the help page

    window_ballot = QMainWindow()  # Main window for the help page UI
    ui_help.setupUi(window_ballot)

    window_notice_box = QMessageBox()  # Notice box for displaying messages
    ui_notice_box.setupUi(window_notice_box)

    # Create the Logic instance for the login UI and pass both UIs to it
    logic = Logic(
        ui_login,
        ui_help,
        ui_ballot,
        ui_notice_box,
        window_login,
        window_help,
        window_ballot,
        window_notice_box,
    )

    # Store the Logic instance in the UI
    ui_login.logic = logic

    # Show the login window
    logic.show_login()

    app.exec()


if __name__ == "__main__":
    main()
