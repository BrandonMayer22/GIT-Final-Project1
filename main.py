from logic import *


def main() -> None:
    """
    Initializes the PyQt application, sets up the UI windows, and starts the main event loop.

    This function creates instances of the various UI components (login, help, ballot, and notice box),
    and initializes the application logic that controls the transitions between different pages.
    It then displays the login page and starts the event loop.
    """
    app = QApplication([])

    ui_login = Ui_LoginWindow()
    ui_help = Ui_help_page()
    ui_ballot = Ui_ballot()
    ui_notice_box = Ui_notice_box()

    logic = Logic(ui_login, ui_help, ui_ballot, ui_notice_box)

    ui_login.logic = logic

    logic.show_login()

    app.exec()


if __name__ == "__main__":
    main()
