from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys
import res_rc


# --------------------------------------------------------------------------------------------------------------------
# login Page
# --------------------------------------------------------------------------------------------------------------------


class Ui_LoginWindow:
    def setupUi(self, LoginWindow) -> None:
        """
        Sets up the UI components for the login widget.

        Args:
            LoginWindow (QWidget): The QWidget instance to configure.
        """
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(700, 400)
        LoginWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        LoginWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setStyleSheet(
            "QPushButton#pushButton_Login{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QPushButton#pushButton_Login:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 188, 132, 226));\n"
            "}\n"
            "QPushButton#pushButton_Login:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(105, 118, 132, 200);\n"
            "}"
        )

        self.label_Background1 = QtWidgets.QLabel(parent=self.widget)
        self.label_Background1.setGeometry(QtCore.QRect(30, 20, 600, 290))
        self.label_Background1.setStyleSheet(
            "border-image: url(:/Images/flag.jpg);\n" "border-radius: 20px;"
        )
        self.label_Background1.setText("")
        self.label_Background1.setObjectName("label_Background1")

        self.label_Background2 = QtWidgets.QLabel(parent=self.widget)
        self.label_Background2.setGeometry(QtCore.QRect(30, 20, 600, 290))
        self.label_Background2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
            "border-radius: 20px;"
        )
        self.label_Background2.setText("")
        self.label_Background2.setObjectName("label_Background2")

        self.label_Background3 = QtWidgets.QLabel(parent=self.widget)
        self.label_Background3.setGeometry(QtCore.QRect(40, 40, 570, 260))
        self.label_Background3.setStyleSheet(
            "background-color: rgba(0, 0, 0, 100);\n" "border-radius: 15px;"
        )
        self.label_Background3.setObjectName("label_Background3")

        self.label_Header = QtWidgets.QLabel(parent=self.widget)
        self.label_Header.setGeometry(QtCore.QRect(180, 40, 301, 50))
        font = QtGui.QFont("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_Header.setFont(font)
        self.label_Header.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_Header.setObjectName("label_Header")

        self.lineEdit_ID = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(220, 130, 211, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(12)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
            "color:rgba(255, 255, 255, 230);\n"
            "padding-bottom: 7px"
        )
        self.lineEdit_ID.setObjectName("lineEdit_ID")

        self.lineEdit_Pin = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_Pin.setGeometry(QtCore.QRect(220, 190, 211, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(12)
        self.lineEdit_Pin.setFont(font)
        self.lineEdit_Pin.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
            "color:rgba(255, 255, 255, 230);\n"
            "padding-bottom: 7px"
        )
        self.lineEdit_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_Pin.setObjectName("lineEdit_Pin")

        # Button (Login button)
        self.pushButton_Login = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_Login.setGeometry(QtCore.QRect(220, 240, 211, 41))
        font = QtGui.QFont("Arial")
        font.setPointSize(15)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setObjectName("pushButton_Login")

        # Error message label
        self.label_Err = QtWidgets.QLabel(parent=self.widget)
        self.label_Err.setGeometry(QtCore.QRect(220, 90, 211, 31))
        self.label_Err.setStyleSheet(
            "background-color: rgb(255, 193, 174);\n"
            "border: 1px solid;\n"
            "border-color:rgb(255, 0, 0);"
            "color: red;"
        )
        self.label_Err.setText("")
        self.label_Err.setObjectName("label_Err")
        self.label_Err.setVisible(False)

        layout.addWidget(self.widget)

        self.centralwidget.setLayout(layout)

        LoginWindow.setLayout(layout)

        self.label_Background1.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25,
                xOffset=0,
                yOffset=0,
                color=QtGui.QColor(234, 221, 186, 100),
            )
        )

        self.label_Background3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25,
                xOffset=0,
                yOffset=0,
                color=QtGui.QColor(105, 118, 132, 100),
            )
        )

        self.pushButton_Login.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25,
                xOffset=3,
                yOffset=3,
                color=QtGui.QColor(105, 118, 132, 100),
            )
        )

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow) -> None:
        """
        Sets up the UI components for the login widget.

        Args:
            LoginWindow (QWidget): The QWidget instance to configure.
        """
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Window"))
        self.label_Background3.setText(_translate("LoginWindow", "TextLabel"))
        self.label_Header.setText(_translate("LoginWindow", "Federal Ballot Service"))
        self.lineEdit_ID.setPlaceholderText(_translate("LoginWindow", "Voter ID"))
        self.lineEdit_Pin.setPlaceholderText(_translate("LoginWindow", "PIN"))
        self.pushButton_Login.setText(_translate("LoginWindow", "Login"))


# --------------------------------------------------------------------------------------------------------------------
# Help Page
# --------------------------------------------------------------------------------------------------------------------


class Ui_help_page:
    def setupUi(self, help_page) -> None:
        """
        Sets up the UI components for the help page.

        Args:
            help_page (QMainWindow): The QMainWindow instance to configure.
        """
        help_page.setObjectName("help_page")
        help_page.resize(1350, 900)
        help_page.setMinimumSize(QtCore.QSize(1350, 900))
        help_page.setMaximumSize(QtCore.QSize(1350, 900))
        help_page.setStyleSheet("background-color: rgb(210, 255, 255);\n" "")
        self.centralwidget = QtWidgets.QWidget(parent=help_page)
        self.centralwidget.setObjectName("centralwidget")
        self.label_topbanner = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_topbanner.setGeometry(QtCore.QRect(0, 0, 1350, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(25)
        self.label_topbanner.setFont(font)
        self.label_topbanner.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "color: rgb(225, 225, 225)\n" ""
        )
        self.label_topbanner.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_topbanner.setObjectName("label_topbanner")
        self.frame_help1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_help1.setGeometry(QtCore.QRect(10, 60, 1330, 291))
        self.frame_help1.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius: 10px;"
        )
        self.frame_help1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_help1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_help1.setObjectName("frame_help1")
        self.label_num1 = QtWidgets.QLabel(parent=self.frame_help1)
        self.label_num1.setGeometry(QtCore.QRect(10, 10, 47, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_num1.setFont(font)
        self.label_num1.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n"
            "color: white; /* Text color */\n"
            "border-radius: 20px; /* Half of the width and height */\n"
            "min-width: 40px; /* Width of the circle */\n"
            "min-height: 40px; /* Height of the circle */\n"
            "font-weight: bold; /* Make the number bold */\n"
            "text-align: center; /* Center-align the text */"
        )
        self.label_num1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_num1.setObjectName("label_num1")
        self.label_frm1help1 = QtWidgets.QLabel(parent=self.frame_help1)
        self.label_frm1help1.setGeometry(QtCore.QRect(60, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.label_frm1help1.setFont(font)
        self.label_frm1help1.setStyleSheet("")
        self.label_frm1help1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm1help1.setObjectName("label_frm1help1")
        self.label_frm1help2 = QtWidgets.QLabel(parent=self.frame_help1)
        self.label_frm1help2.setGeometry(QtCore.QRect(10, 70, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm1help2.setFont(font)
        self.label_frm1help2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm1help2.setWordWrap(True)
        self.label_frm1help2.setObjectName("label_frm1help2")
        self.label_frm1help3 = QtWidgets.QLabel(parent=self.frame_help1)
        self.label_frm1help3.setGeometry(QtCore.QRect(20, 240, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm1help3.setFont(font)
        self.label_frm1help3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm1help3.setWordWrap(True)
        self.label_frm1help3.setObjectName("label_frm1help3")
        self.frame_ballbox1 = QtWidgets.QFrame(parent=self.frame_help1)
        self.frame_ballbox1.setGeometry(QtCore.QRect(860, 20, 291, 151))
        self.frame_ballbox1.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 0px;"
        )
        self.frame_ballbox1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ballbox1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ballbox1.setObjectName("frame_ballbox1")
        self.frame_candbox1 = QtWidgets.QFrame(parent=self.frame_ballbox1)
        self.frame_candbox1.setGeometry(QtCore.QRect(5, 30, 281, 31))
        self.frame_candbox1.setStyleSheet(
            "background-color: rgb(225, 225, 225);\n" "border-radius: 5px;"
        )
        self.frame_candbox1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_candbox1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_candbox1.setObjectName("frame_candbox1")
        self.frame_chkbox1 = QtWidgets.QFrame(parent=self.frame_candbox1)
        self.frame_chkbox1.setGeometry(QtCore.QRect(10, 6, 20, 20))
        self.frame_chkbox1.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 3px;"
        )
        self.frame_chkbox1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_chkbox1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_chkbox1.setObjectName("frame_chkbox1")
        self.frame_candbox2 = QtWidgets.QFrame(parent=self.frame_ballbox1)
        self.frame_candbox2.setGeometry(QtCore.QRect(5, 70, 281, 31))
        self.frame_candbox2.setStyleSheet(
            "background-color: rgb(227, 239, 170);\n" "border-radius: 5px;"
        )
        self.frame_candbox2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_candbox2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_candbox2.setObjectName("frame_candbox2")
        self.frame_chkbox2 = QtWidgets.QFrame(parent=self.frame_candbox2)
        self.frame_chkbox2.setGeometry(QtCore.QRect(10, 6, 20, 20))
        self.frame_chkbox2.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 3px;"
        )
        self.frame_chkbox2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_chkbox2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_chkbox2.setObjectName("frame_chkbox2")
        self.label_frm1chk = QtWidgets.QLabel(parent=self.frame_chkbox2)
        self.label_frm1chk.setGeometry(QtCore.QRect(0, -3, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm1chk.setFont(font)
        self.label_frm1chk.setStyleSheet("color: rgb(57, 255, 20);")
        self.label_frm1chk.setScaledContents(True)
        self.label_frm1chk.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm1chk.setObjectName("label_frm1chk")
        self.frame_candbox3 = QtWidgets.QFrame(parent=self.frame_ballbox1)
        self.frame_candbox3.setGeometry(QtCore.QRect(5, 110, 281, 31))
        self.frame_candbox3.setStyleSheet(
            "background-color: rgb(225, 225, 225);\n" "border-radius: 5px;"
        )
        self.frame_candbox3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_candbox3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_candbox3.setObjectName("frame_candbox3")
        self.frame_chkbox3 = QtWidgets.QFrame(parent=self.frame_candbox3)
        self.frame_chkbox3.setGeometry(QtCore.QRect(10, 6, 20, 20))
        self.frame_chkbox3.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 3px;"
        )
        self.frame_chkbox3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_chkbox3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_chkbox3.setObjectName("frame_chkbox3")
        self.frame_candbox2.raise_()
        self.frame_candbox3.raise_()
        self.frame_candbox1.raise_()
        self.frame_backfrm = QtWidgets.QFrame(parent=self.frame_help1)
        self.frame_backfrm.setGeometry(QtCore.QRect(920, 220, 71, 61))
        self.frame_backfrm.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 0px;"
        )
        self.frame_backfrm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_backfrm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_backfrm.setObjectName("frame_backfrm")
        self.frame_backbutt = QtWidgets.QFrame(parent=self.frame_backfrm)
        self.frame_backbutt.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.frame_backbutt.setStyleSheet(
            "background-color: rgb(223, 230, 81);\n" "border-radius: 3px;"
        )
        self.frame_backbutt.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_backbutt.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_backbutt.setObjectName("frame_backbutt")
        self.label_backarrow = QtWidgets.QLabel(parent=self.frame_backbutt)
        self.label_backarrow.setGeometry(QtCore.QRect(10, 0, 47, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_backarrow.setFont(font)
        self.label_backarrow.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n"
            "color: white; /* Text color */\n"
            "border-radius: 20px; /* Half of the width and height */\n"
            "min-width: 40px; /* Width of the circle */\n"
            "min-height: 40px; /* Height of the circle */\n"
            "font-weight: bold; /* Make the number bold */\n"
            "text-align: center; /* Center-align the text */"
        )
        self.label_backarrow.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_backarrow.setObjectName("label_backarrow")
        self.frame_fwdfrm = QtWidgets.QFrame(parent=self.frame_help1)
        self.frame_fwdfrm.setGeometry(QtCore.QRect(1020, 220, 71, 61))
        self.frame_fwdfrm.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 0px;"
        )
        self.frame_fwdfrm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fwdfrm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fwdfrm.setObjectName("frame_fwdfrm")
        self.frame_fwdbutt = QtWidgets.QFrame(parent=self.frame_fwdfrm)
        self.frame_fwdbutt.setGeometry(QtCore.QRect(0, 10, 61, 41))
        self.frame_fwdbutt.setStyleSheet(
            "background-color: rgb(223, 230, 81);\n" "border-radius: 3px;"
        )
        self.frame_fwdbutt.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fwdbutt.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fwdbutt.setObjectName("frame_fwdbutt")
        self.label_fwdarrow = QtWidgets.QLabel(parent=self.frame_fwdbutt)
        self.label_fwdarrow.setGeometry(QtCore.QRect(10, 0, 47, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_fwdarrow.setFont(font)
        self.label_fwdarrow.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n"
            "color: white; /* Text color */\n"
            "border-radius: 20px; /* Half of the width and height */\n"
            "min-width: 40px; /* Width of the circle */\n"
            "min-height: 40px; /* Height of the circle */\n"
            "font-weight: bold; /* Make the number bold */\n"
            "text-align: center; /* Center-align the text */"
        )
        self.label_fwdarrow.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_fwdarrow.setObjectName("label_fwdarrow")
        self.frame_help2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_help2.setGeometry(QtCore.QRect(10, 360, 1330, 191))
        self.frame_help2.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius: 10px;"
        )
        self.frame_help2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_help2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_help2.setObjectName("frame_help2")
        self.label_num2 = QtWidgets.QLabel(parent=self.frame_help2)
        self.label_num2.setGeometry(QtCore.QRect(10, 10, 47, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_num2.setFont(font)
        self.label_num2.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n"
            "color: white; /* Text color */\n"
            "border-radius: 20px; /* Half of the width and height */\n"
            "min-width: 40px; /* Width of the circle */\n"
            "min-height: 40px; /* Height of the circle */\n"
            "font-weight: bold; /* Make the number bold */\n"
            "text-align: center; /* Center-align the text */"
        )
        self.label_num2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_num2.setObjectName("label_num2")
        self.label_frm2help1 = QtWidgets.QLabel(parent=self.frame_help2)
        self.label_frm2help1.setGeometry(QtCore.QRect(60, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.label_frm2help1.setFont(font)
        self.label_frm2help1.setStyleSheet("")
        self.label_frm2help1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm2help1.setObjectName("label_frm2help1")
        self.label_frm2help2 = QtWidgets.QLabel(parent=self.frame_help2)
        self.label_frm2help2.setGeometry(QtCore.QRect(10, 100, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm2help2.setFont(font)
        self.label_frm2help2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm2help2.setWordWrap(True)
        self.label_frm2help2.setObjectName("label_frm2help2")
        self.frame_balfrm2 = QtWidgets.QFrame(parent=self.frame_help2)
        self.frame_balfrm2.setGeometry(QtCore.QRect(860, 20, 291, 151))
        self.frame_balfrm2.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 0px;"
        )
        self.frame_balfrm2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_balfrm2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_balfrm2.setObjectName("frame_balfrm2")
        self.frame_candbox4 = QtWidgets.QFrame(parent=self.frame_balfrm2)
        self.frame_candbox4.setGeometry(QtCore.QRect(5, 30, 281, 31))
        self.frame_candbox4.setStyleSheet(
            "background-color: rgb(227, 239, 170);\n" "border-radius: 5px;"
        )
        self.frame_candbox4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_candbox4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_candbox4.setObjectName("frame_candbox4")
        self.frame_frm2chk1 = QtWidgets.QFrame(parent=self.frame_candbox4)
        self.frame_frm2chk1.setGeometry(QtCore.QRect(10, 6, 20, 20))
        self.frame_frm2chk1.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 3px;"
        )
        self.frame_frm2chk1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_frm2chk1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_frm2chk1.setObjectName("frame_frm2chk1")
        self.label_frm2chk1 = QtWidgets.QLabel(parent=self.frame_frm2chk1)
        self.label_frm2chk1.setGeometry(QtCore.QRect(0, -2, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm2chk1.setFont(font)
        self.label_frm2chk1.setStyleSheet("color: rgb(57, 255, 20);")
        self.label_frm2chk1.setScaledContents(True)
        self.label_frm2chk1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm2chk1.setObjectName("label_frm2chk1")
        self.frame_candbox5 = QtWidgets.QFrame(parent=self.frame_balfrm2)
        self.frame_candbox5.setGeometry(QtCore.QRect(5, 70, 281, 31))
        self.frame_candbox5.setStyleSheet(
            "background-color: rgb(227, 239, 170);\n" "border-radius: 5px;"
        )
        self.frame_candbox5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_candbox5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_candbox5.setObjectName("frame_candbox5")
        self.frame_frm2chk2 = QtWidgets.QFrame(parent=self.frame_candbox5)
        self.frame_frm2chk2.setGeometry(QtCore.QRect(10, 6, 20, 20))
        self.frame_frm2chk2.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 3px;"
        )
        self.frame_frm2chk2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_frm2chk2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_frm2chk2.setObjectName("frame_frm2chk2")
        self.label_frm2chk2 = QtWidgets.QLabel(parent=self.frame_frm2chk2)
        self.label_frm2chk2.setGeometry(QtCore.QRect(0, -3, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm2chk2.setFont(font)
        self.label_frm2chk2.setStyleSheet("color: rgb(57, 255, 20);")
        self.label_frm2chk2.setScaledContents(True)
        self.label_frm2chk2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm2chk2.setObjectName("label_frm2chk2")
        self.frame_candbox6 = QtWidgets.QFrame(parent=self.frame_balfrm2)
        self.frame_candbox6.setGeometry(QtCore.QRect(5, 110, 281, 31))
        self.frame_candbox6.setStyleSheet(
            "background-color: rgb(227, 239, 170);\n" "border-radius: 5px;"
        )
        self.frame_candbox6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_candbox6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_candbox6.setObjectName("frame_candbox6")
        self.frame_frm2chk3 = QtWidgets.QFrame(parent=self.frame_candbox6)
        self.frame_frm2chk3.setGeometry(QtCore.QRect(10, 6, 20, 20))
        self.frame_frm2chk3.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "border-radius: 3px;"
        )
        self.frame_frm2chk3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_frm2chk3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_frm2chk3.setObjectName("frame_frm2chk3")
        self.label_frm2chk3 = QtWidgets.QLabel(parent=self.frame_frm2chk3)
        self.label_frm2chk3.setGeometry(QtCore.QRect(0, -2, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm2chk3.setFont(font)
        self.label_frm2chk3.setStyleSheet("color: rgb(57, 255, 20);")
        self.label_frm2chk3.setScaledContents(True)
        self.label_frm2chk3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm2chk3.setObjectName("label_frm2chk3")
        self.frame_help3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_help3.setGeometry(QtCore.QRect(10, 560, 1330, 211))
        self.frame_help3.setStyleSheet(
            "background-color: rgb(85, 170, 255);\n" "border-radius: 10px;"
        )
        self.frame_help3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_help3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_help3.setObjectName("frame_help3")
        self.label_num3 = QtWidgets.QLabel(parent=self.frame_help3)
        self.label_num3.setGeometry(QtCore.QRect(10, 10, 47, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_num3.setFont(font)
        self.label_num3.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n"
            "color: white; /* Text color */\n"
            "border-radius: 20px; /* Half of the width and height */\n"
            "min-width: 40px; /* Width of the circle */\n"
            "min-height: 40px; /* Height of the circle */\n"
            "font-weight: bold; /* Make the number bold */\n"
            "text-align: center; /* Center-align the text */"
        )
        self.label_num3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_num3.setObjectName("label_num3")
        self.label_frm3help1 = QtWidgets.QLabel(parent=self.frame_help3)
        self.label_frm3help1.setGeometry(QtCore.QRect(60, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.label_frm3help1.setFont(font)
        self.label_frm3help1.setStyleSheet("")
        self.label_frm3help1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm3help1.setObjectName("label_frm3help1")
        self.label_frm3help2 = QtWidgets.QLabel(parent=self.frame_help3)
        self.label_frm3help2.setGeometry(QtCore.QRect(10, 90, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_frm3help2.setFont(font)
        self.label_frm3help2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_frm3help2.setWordWrap(True)
        self.label_frm3help2.setObjectName("label_frm3help2")
        self.label_votebutt = QtWidgets.QLabel(parent=self.frame_help3)
        self.label_votebutt.setGeometry(QtCore.QRect(890, 80, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_votebutt.setFont(font)
        self.label_votebutt.setStyleSheet(
            "background-color: red; \n"
            "color: white;                     \n"
            "border-radius: 25px;            \n"
            "padding: 10px;                 \n"
            "font-size: 40px;            \n"
            "font-weight: bold; "
        )
        self.label_votebutt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_votebutt.setObjectName("label_votebutt")
        self.label_bottombanner = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bottombanner.setGeometry(QtCore.QRect(0, 780, 1350, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(25)
        self.label_bottombanner.setFont(font)
        self.label_bottombanner.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "color: rgb(225, 225, 225)\n" ""
        )
        self.label_bottombanner.setText("")
        self.label_bottombanner.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bottombanner.setObjectName("label_bottombanner")
        self.pushButton_forward = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_forward.setGeometry(QtCore.QRect(1250, 785, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_forward.setFont(font)
        self.pushButton_forward.setStyleSheet(
            "QPushButton#pushButton_forward {\n"
            "    background-color: rgb(240, 240, 0);\n"
            "    color: rgb(25, 25, 80);\n"
            "    border-radius: 5px;  \n"
            "}\n"
            "\n"
            "QPushButton#pushButton_forward:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,\n"
            "        stop:0 rgba(240, 240, 0, 255),  \n"
            "        stop:1 rgba(105, 188, 132, 226));  \n"
            "}\n"
            "\n"
            "QPushButton#pushButton_forward:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(105, 118, 132, 200); \n"
            "}\n"
            "\n"
            "\n"
            # "border-radius: 3px;"
        )
        self.pushButton_forward.setObjectName("pushButton_forward")
        help_page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=help_page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        help_page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=help_page)
        self.statusbar.setObjectName("statusbar")
        help_page.setStatusBar(self.statusbar)

        self.retranslateUi(help_page)
        QtCore.QMetaObject.connectSlotsByName(help_page)

    def retranslateUi(self, help_page) -> None:
        """
        Handles translation or dynamic updates to the UI elements.

        Args:
            help_page (QMainWindow): The QMainWindow instance to update.
        """
        _translate = QtCore.QCoreApplication.translate
        help_page.setWindowTitle(_translate("help_page", "MainWindow"))
        self.label_topbanner.setText(
            _translate(
                "help_page",
                "Voting on the Federal Ballot Service is as easy as 1, 2, 3",
            )
        )
        self.label_num1.setText(_translate("help_page", "1"))
        self.label_frm1help1.setText(_translate("help_page", "Make your selections"))
        self.label_frm1help2.setText(
            _translate(
                "help_page",
                "Click the bubble next to the candidate on the screen to make your selection",
            )
        )
        self.label_frm1help3.setText(
            _translate(
                "help_page", "Use the forward and back buttons to change the page"
            )
        )
        self.label_frm1chk.setText(_translate("help_page", "✔"))
        self.label_backarrow.setText(_translate("help_page", "←"))
        self.label_fwdarrow.setText(_translate("help_page", "→"))
        self.label_num2.setText(_translate("help_page", "2"))
        self.label_frm2help1.setText(_translate("help_page", "Review your selections"))
        self.label_frm2help2.setText(
            _translate(
                "help_page",
                "Scroll through to ensure your selections are accurate. Click back to make changes.",
            )
        )
        self.label_frm2chk1.setText(_translate("help_page", "✔"))
        self.label_frm2chk2.setText(_translate("help_page", "✔"))
        self.label_frm2chk3.setText(_translate("help_page", "✔"))
        self.label_num3.setText(_translate("help_page", "3"))
        self.label_frm3help1.setText(_translate("help_page", "Cast your ballot"))
        self.label_frm3help2.setText(
            _translate(
                "help_page",
                "Press the Vote button at the bottom of your screen when it appears to cast your ballot",
            )
        )
        self.label_votebutt.setText(_translate("help_page", "Vote"))
        self.pushButton_forward.setText(_translate("help_page", "→"))


# --------------------------------------------------------------------------------------------------------------------
# Ballot Selections Page
# --------------------------------------------------------------------------------------------------------------------
class Ui_ballot:
    def setupUi(self, ballot) -> None:
        """
        Sets up the UI components for the ballot page.

        Args:
            ballot (QMainWindow): The QMainWindow instance to configure.
        """
        ballot.setObjectName("ballot")
        ballot.resize(1350, 900)
        ballot.setMinimumSize(QtCore.QSize(1350, 900))
        ballot.setMaximumSize(QtCore.QSize(1350, 900))
        ballot.setStyleSheet("background-color: rgb(210, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=ballot)
        self.centralwidget.setObjectName("centralwidget")
        self.label_bottombanner = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bottombanner.setGeometry(QtCore.QRect(0, 785, 1350, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(25)
        self.label_bottombanner.setFont(font)
        self.label_bottombanner.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "color: rgb(225, 225, 225)\n" ""
        )
        self.label_bottombanner.setText("")
        self.label_bottombanner.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bottombanner.setObjectName("label_bottombanner")
        self.pushButton_voteballot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_voteballot.setGeometry(QtCore.QRect(570, 790, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_voteballot.setFont(font)
        self.pushButton_voteballot.setStyleSheet(
            "QPushButton#pushButton_voteballot {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,\n"
            "        stop:0 rgba(255, 0, 0, 255),    /* Bright red at the start */\n"
            "        stop:1 rgba(200, 0, 0, 255));  /* Darker red at the end */\n"
            "    color: rgb(255, 255, 255);          /* White text for contrast */\n"
            "    border-radius: 25px;\n"
            "    padding: 10px;\n"
            "    font-size: 30px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_voteballot:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,\n"
            "        stop:0 rgba(255, 50, 50, 255),  /* Stronger light red */\n"
            "        stop:1 rgba(100, 0, 0, 255));   /* Much darker red */\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_voteballot:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(180, 0, 0, 255);  /* Deep red for pressed state */\n"
            "}\n"
            "\n"
            ""
        )
        self.pushButton_voteballot.setObjectName("pushButton_voteballot")
        self.label_bottombanner_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bottombanner_2.setGeometry(QtCore.QRect(0, 0, 1350, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(25)
        self.label_bottombanner_2.setFont(font)
        self.label_bottombanner_2.setStyleSheet(
            "background-color: rgb(25, 25, 80);\n" "color: rgb(225, 225, 225)\n" ""
        )
        self.label_bottombanner_2.setText("")
        self.label_bottombanner_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bottombanner_2.setObjectName("label_bottombanner_2")
        self.frame_pres = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_pres.setGeometry(QtCore.QRect(80, 90, 381, 311))
        self.frame_pres.setStyleSheet("background-color: rgb(25, 25, 80);")
        self.frame_pres.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pres.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pres.setObjectName("frame_pres")
        self.label_pres = QtWidgets.QLabel(parent=self.frame_pres)
        self.label_pres.setGeometry(QtCore.QRect(70, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_pres.setFont(font)
        self.label_pres.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_pres.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_pres.setWordWrap(True)
        self.label_pres.setObjectName("label_pres")
        self.widget = QtWidgets.QWidget(parent=self.frame_pres)
        self.widget.setGeometry(QtCore.QRect(10, 80, 361, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout_pres = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_pres.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_pres.setObjectName("verticalLayout_pres")
        self.frame_presopt1 = QtWidgets.QFrame(parent=self.widget)
        self.frame_presopt1.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_presopt1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_presopt1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_presopt1.setObjectName("frame_presopt1")
        self.label_presopt1 = QtWidgets.QLabel(parent=self.frame_presopt1)
        self.label_presopt1.setGeometry(QtCore.QRect(100, 0, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_presopt1.setFont(font)
        self.label_presopt1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_presopt1.setWordWrap(True)
        self.label_presopt1.setObjectName("label_presopt1")
        self.checkBox_presopt1 = QtWidgets.QCheckBox(parent=self.frame_presopt1)
        self.checkBox_presopt1.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_presopt1.setFont(font)
        self.checkBox_presopt1.setStyleSheet("color: rgb(0, 255, 0);")
        self.checkBox_presopt1.setText("")
        self.checkBox_presopt1.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_presopt1.setObjectName("checkBox_presopt1")
        self.buttonGroup_pres = QtWidgets.QButtonGroup(ballot)
        self.buttonGroup_pres.setObjectName("buttonGroup_pres")
        self.buttonGroup_pres.addButton(self.checkBox_presopt1)
        self.verticalLayout_pres.addWidget(self.frame_presopt1)
        self.frame_pres1_2 = QtWidgets.QFrame(parent=self.widget)
        self.frame_pres1_2.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_pres1_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pres1_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pres1_2.setObjectName("frame_pres1_2")
        self.label_presopt2 = QtWidgets.QLabel(parent=self.frame_pres1_2)
        self.label_presopt2.setGeometry(QtCore.QRect(100, 0, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_presopt2.setFont(font)
        self.label_presopt2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_presopt2.setWordWrap(True)
        self.label_presopt2.setObjectName("label_presopt2")
        self.checkBox_presopt2 = QtWidgets.QCheckBox(parent=self.frame_pres1_2)
        self.checkBox_presopt2.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_presopt2.setFont(font)
        self.checkBox_presopt2.setText("")
        self.checkBox_presopt2.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_presopt2.setObjectName("checkBox_presopt2")
        self.buttonGroup_pres.addButton(self.checkBox_presopt2)
        self.verticalLayout_pres.addWidget(self.frame_pres1_2)
        self.frame_preswritein = QtWidgets.QFrame(parent=self.widget)
        self.frame_preswritein.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_preswritein.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_preswritein.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_preswritein.setObjectName("frame_preswritein")
        self.label_preswritein = QtWidgets.QLabel(parent=self.frame_preswritein)
        self.label_preswritein.setGeometry(QtCore.QRect(100, 0, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_preswritein.setFont(font)
        self.label_preswritein.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_preswritein.setWordWrap(True)
        self.label_preswritein.setObjectName("label_preswritein")
        self.checkBox_preswritein = QtWidgets.QCheckBox(parent=self.frame_preswritein)
        self.checkBox_preswritein.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_preswritein.setFont(font)
        self.checkBox_preswritein.setText("")
        self.checkBox_preswritein.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_preswritein.setObjectName("checkBox_preswritein")
        self.buttonGroup_pres.addButton(self.checkBox_preswritein)
        self.lineEdit_preswritein = QtWidgets.QLineEdit(parent=self.frame_preswritein)
        self.lineEdit_preswritein.setGeometry(QtCore.QRect(50, 20, 261, 31))
        self.lineEdit_preswritein.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_preswritein.setObjectName("lineEdit_preswritein")
        self.verticalLayout_pres.addWidget(self.frame_preswritein)

        self.frame_senate = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_senate.setGeometry(QtCore.QRect(480, 90, 381, 311))
        self.frame_senate.setStyleSheet("background-color: rgb(25, 25, 80);")
        self.frame_senate.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_senate.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_senate.setObjectName("frame_senate")
        self.label_senate = QtWidgets.QLabel(parent=self.frame_senate)
        self.label_senate.setGeometry(QtCore.QRect(70, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_senate.setFont(font)
        self.label_senate.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_senate.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_senate.setWordWrap(True)
        self.label_senate.setObjectName("label_senate")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame_senate)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 361, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_senate = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_senate.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_senate.setObjectName("verticalLayout_senate")
        self.frame_senopt1 = QtWidgets.QFrame(parent=self.layoutWidget)
        self.frame_senopt1.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_senopt1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_senopt1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_senopt1.setObjectName("frame_senopt1")
        self.label_senopt1 = QtWidgets.QLabel(parent=self.frame_senopt1)
        self.label_senopt1.setGeometry(QtCore.QRect(100, 0, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_senopt1.setFont(font)
        self.label_senopt1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_senopt1.setWordWrap(True)
        self.label_senopt1.setObjectName("label_senopt1")
        self.checkBox_senopt1 = QtWidgets.QCheckBox(parent=self.frame_senopt1)
        self.checkBox_senopt1.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_senopt1.setFont(font)
        self.checkBox_senopt1.setText("")
        self.checkBox_senopt1.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_senopt1.setObjectName("checkBox_senopt1")
        self.buttonGroup_senate = QtWidgets.QButtonGroup(ballot)
        self.buttonGroup_senate.setObjectName("buttonGroup_senate")
        self.buttonGroup_senate.addButton(self.checkBox_senopt1)
        self.verticalLayout_senate.addWidget(self.frame_senopt1)
        self.frame_senopt2 = QtWidgets.QFrame(parent=self.layoutWidget)
        self.frame_senopt2.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_senopt2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_senopt2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_senopt2.setObjectName("frame_senopt2")
        self.label_senopt2 = QtWidgets.QLabel(parent=self.frame_senopt2)
        self.label_senopt2.setGeometry(QtCore.QRect(100, 0, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_senopt2.setFont(font)
        self.label_senopt2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_senopt2.setWordWrap(True)
        self.label_senopt2.setObjectName("label_senopt2")
        self.checkBox_senopt2 = QtWidgets.QCheckBox(parent=self.frame_senopt2)
        self.checkBox_senopt2.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_senopt2.setFont(font)
        self.checkBox_senopt2.setText("")
        self.checkBox_senopt2.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_senopt2.setObjectName("checkBox_senopt2")
        self.buttonGroup_senate.addButton(self.checkBox_senopt2)
        self.verticalLayout_senate.addWidget(self.frame_senopt2)
        self.frame_senwritein = QtWidgets.QFrame(parent=self.layoutWidget)
        self.frame_senwritein.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_senwritein.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_senwritein.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_senwritein.setObjectName("frame_senwritein")
        self.label_senwritein = QtWidgets.QLabel(parent=self.frame_senwritein)
        self.label_senwritein.setGeometry(QtCore.QRect(100, 0, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_senwritein.setFont(font)
        self.label_senwritein.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_senwritein.setWordWrap(True)
        self.label_senwritein.setObjectName("label_senwritein")
        self.checkBox_senwritein = QtWidgets.QCheckBox(parent=self.frame_senwritein)
        self.checkBox_senwritein.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_senwritein.setFont(font)
        self.checkBox_senwritein.setText("")
        self.checkBox_senwritein.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_senwritein.setObjectName("checkBox_senwritein")
        self.buttonGroup_senate.addButton(self.checkBox_senwritein)
        self.lineEdit_senwritein = QtWidgets.QLineEdit(parent=self.frame_senwritein)
        self.lineEdit_senwritein.setGeometry(QtCore.QRect(50, 20, 261, 31))
        self.lineEdit_senwritein.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_senwritein.setObjectName("lineEdit_senwritein")
        self.verticalLayout_senate.addWidget(self.frame_senwritein)

        self.frame_house = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_house.setGeometry(QtCore.QRect(880, 90, 381, 311))
        self.frame_house.setStyleSheet("background-color: rgb(25, 25, 80);")
        self.frame_house.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_house.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_house.setObjectName("frame_house")
        self.label_house = QtWidgets.QLabel(parent=self.frame_house)
        self.label_house.setGeometry(QtCore.QRect(70, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_house.setFont(font)
        self.label_house.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_house.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_house.setWordWrap(True)
        self.label_house.setObjectName("label_house")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.frame_house)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 80, 361, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_house = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_house.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_house.setObjectName("verticalLayout_house")
        self.frame_houseopt1 = QtWidgets.QFrame(parent=self.layoutWidget_2)
        self.frame_houseopt1.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_houseopt1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_houseopt1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_houseopt1.setObjectName("frame_houseopt1")
        self.label_houseopt1 = QtWidgets.QLabel(parent=self.frame_houseopt1)
        self.label_houseopt1.setGeometry(QtCore.QRect(100, 0, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_houseopt1.setFont(font)
        self.label_houseopt1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_houseopt1.setWordWrap(True)
        self.label_houseopt1.setObjectName("label_houseopt1")
        self.checkBox_houseopt1 = QtWidgets.QCheckBox(parent=self.frame_houseopt1)
        self.checkBox_houseopt1.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_houseopt1.setFont(font)
        self.checkBox_houseopt1.setText("")
        self.checkBox_houseopt1.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_houseopt1.setObjectName("checkBox_houseopt1")
        self.buttonGroup_house = QtWidgets.QButtonGroup(ballot)
        self.buttonGroup_house.setObjectName("buttonGroup_house")
        self.buttonGroup_house.addButton(self.checkBox_houseopt1)
        self.verticalLayout_house.addWidget(self.frame_houseopt1)
        self.frame_houseopt2 = QtWidgets.QFrame(parent=self.layoutWidget_2)
        self.frame_houseopt2.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_houseopt2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_houseopt2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_houseopt2.setObjectName("frame_houseopt2")
        self.label_houseopt2 = QtWidgets.QLabel(parent=self.frame_houseopt2)
        self.label_houseopt2.setGeometry(QtCore.QRect(100, 0, 171, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_houseopt2.setFont(font)
        self.label_houseopt2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_houseopt2.setWordWrap(True)
        self.label_houseopt2.setObjectName("label_houseopt2")
        self.checkBox_houseopt2 = QtWidgets.QCheckBox(parent=self.frame_houseopt2)
        self.checkBox_houseopt2.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_houseopt2.setFont(font)
        self.checkBox_houseopt2.setText("")
        self.checkBox_houseopt2.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_houseopt2.setObjectName("checkBox_houseopt2")
        self.buttonGroup_house.addButton(self.checkBox_houseopt2)
        self.verticalLayout_house.addWidget(self.frame_houseopt2)
        self.frame_housewritein = QtWidgets.QFrame(parent=self.layoutWidget_2)
        self.frame_housewritein.setStyleSheet(
            "background-color: rgb(210, 255, 255);\n" "border-radius: 10px;"
        )
        self.frame_housewritein.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_housewritein.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_housewritein.setObjectName("frame_housewritein")
        self.label_housewritein = QtWidgets.QLabel(parent=self.frame_housewritein)
        self.label_housewritein.setGeometry(QtCore.QRect(100, 0, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_housewritein.setFont(font)
        self.label_housewritein.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_housewritein.setWordWrap(True)
        self.label_housewritein.setObjectName("label_housewritein")
        self.checkBox_housewritein = QtWidgets.QCheckBox(parent=self.frame_housewritein)
        self.checkBox_housewritein.setGeometry(QtCore.QRect(10, 10, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_housewritein.setFont(font)
        self.checkBox_housewritein.setText("")
        self.checkBox_housewritein.setIconSize(QtCore.QSize(100, 100))
        self.checkBox_housewritein.setObjectName("checkBox_housewritein")
        self.buttonGroup_house.addButton(self.checkBox_housewritein)
        self.lineEdit_housewritein = QtWidgets.QLineEdit(parent=self.frame_housewritein)
        self.lineEdit_housewritein.setGeometry(QtCore.QRect(50, 20, 261, 31))
        self.lineEdit_housewritein.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.lineEdit_housewritein.setObjectName("lineEdit_housewritein")
        self.verticalLayout_house.addWidget(self.frame_housewritein)
        self.pushButton_back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 790, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet(
            "QPushButton#pushButton_back {\n"
            "    background-color: rgb(240, 240, 0);\n"
            "    color: rgb(25, 25, 80);\n"
            "    border-radius: 5px;  \n"
            "}\n"
            "\n"
            "QPushButton#pushButton_back:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,\n"
            "        stop:0 rgba(240, 240, 0, 255),  \n"
            "        stop:1 rgba(105, 188, 132, 226));  \n"
            "}\n"
            "\n"
            "QPushButton#pushButton_back:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(105, 118, 132, 200); \n"
            "}\n"
            "\n"
            "\n"
            "border-radius: 3px;"
        )
        self.pushButton_back.setObjectName("pushButton_back")
        ballot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ballot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        ballot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ballot)
        self.statusbar.setObjectName("statusbar")
        ballot.setStatusBar(self.statusbar)

        self.retranslateUi(ballot)
        QtCore.QMetaObject.connectSlotsByName(ballot)

    def retranslateUi(self, ballot) -> None:
        """
        Sets up translations or dynamic text for the ballot UI components.

        Args:
        ballot (QMainWindow): The main window representing the ballot UI.
        """
        _translate = QtCore.QCoreApplication.translate
        ballot.setWindowTitle(_translate("ballot", "MainWindow"))
        self.pushButton_voteballot.setText(_translate("ballot", "Cast Your Vote"))
        self.label_pres.setText(
            _translate("ballot", "Electors for President and Vice President")
        )
        self.label_presopt1.setText(
            _translate(
                "ballot",
                "DONALD J. TRUMP For President and JD VANCE For Vice President Republican Party Nominee",
            )
        )
        self.label_presopt2.setText(
            _translate(
                "ballot",
                "KAMALA D. HARRIS For President and TIM WALZ For Vice President Democratic Party Nominee",
            )
        )
        self.label_preswritein.setText(_translate("ballot", "Write-in"))
        self.label_senate.setText(_translate("ballot", "United States Senate"))
        self.label_senopt1.setText(
            _translate("ballot", "MARSHA BLACKBURN Republican Party Nominee")
        )
        self.label_senopt2.setText(
            _translate("ballot", "GLORIA JOHNSON Democratic Party Nominee")
        )
        self.label_senwritein.setText(_translate("ballot", "Write-in"))
        self.label_house.setText(
            _translate("ballot", "United States House of Representatives")
        )
        self.label_houseopt1.setText(
            _translate("ballot", "SCOTT DESJARLAIS Republican Party Nominee")
        )
        self.label_houseopt2.setText(
            _translate("ballot", "VICTORIA ISABEL BRODERICK Democratic Party Nominee")
        )
        self.label_housewritein.setText(_translate("ballot", "Write-in"))
        self.pushButton_back.setText(_translate("ballot", "←"))


# --------------------------------------------------------------------------------------------------------------------
# Ending notification box
# --------------------------------------------------------------------------------------------------------------------
class Ui_notice_box:
    def setupUi(self, notice_box) -> None:
        """
        Sets up the UI components for the notice box.

        Args:
            notice_box (QMessageBox): The QMessageBox instance to configure.
        """
        notice_box.setWindowTitle("Notice")
        notice_box.setIcon(QMessageBox.Icon.Information)

        self.label_notification = QLabel(notice_box)
        self.label_notification.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_notification.setWordWrap(True)
        notice_box.setText("This is a placeholder notification.")
        notice_box.setStandardButtons(QMessageBox.StandardButton.Ok)

    def retranslateUi(self, notice_box) -> None:
        """
        Handles translation or dynamic updates to the UI elements.

        Args:
            notice_box (QMessageBox): The QMessageBox instance to update.
        """
        _translate = QtCore.QCoreApplication.translate
        notice_box.setWindowTitle(_translate("notice_box", "Notice"))
        self.label_notification.setText(
            _translate("notice_box", "This is a placeholder notification.")
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
