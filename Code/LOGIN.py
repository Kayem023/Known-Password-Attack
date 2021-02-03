# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from client import Client
import hashlib


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 758)
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 270, 131, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 360, 131, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 0, 211, 171))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("auth.png"))
        self.label_4.setObjectName("label_4")
        self.userText = QtWidgets.QLineEdit(self.centralwidget)
        self.userText.setGeometry(QtCore.QRect(450, 274, 491, 41))
        self.userText.setObjectName("userText")
        self.passText = QtWidgets.QLineEdit(self.centralwidget)
        self.passText.setGeometry(QtCore.QRect(450, 360, 491, 41))
        self.passText.setObjectName("passText")
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(720, 450, 211, 51))
        self.login.setStyleSheet("background-color:green;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 20px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.login.setObjectName("login")
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(450, 450, 241, 51))
        self.signup.setStyleSheet("background-color:blue;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 20px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.signup.setObjectName("signup")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 531, 1071, 161))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.login.clicked.connect(self.loginButtonHandler)
        self.signup.clicked.connect(self.signupButtonHandler)
        
        
        self.client = Client()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.signup.setText(_translate("MainWindow", "SIGN UP"))
        
    def loginButtonHandler(self):
        print("login entered")
        username = self.userText.text()
        password = self.passText.text()
        
        if len(username)>0  and  len(password)>0 :
            sendMsg = self.makeMessage(username, password,"login")
            self.client.send(sendMsg)
            response = self.client.receive()
            print(response)
            if response=="OK":
                self.textBrowser.setText("Login Successful. Thank You")
            else:
                if response == "NO":
                    self.textBrowser.setText("Username, Password combination is invalid")
        else:
            self.textBrowser.setText("Please give input to all field correctly")
        
    def signupButtonHandler(self):
        print("signup entered")
        username = self.userText.text()
        password = self.passText.text()
        
        if len(username)>0  and  len(password)>0 :
            sendMsg = self.makeMessage(username, password,"register")
            self.client.send(sendMsg)
            response = self.client.receive()
            print(response)
            if response=="OK":
                self.textBrowser.setText("Registration Successful. Thank You")
            else:
                if response == "NO":
                    self.textBrowser.setText("Username exists, change it")
        else:
            self.textBrowser.setText("Please give input to all field correctly")
        
        
        
    def makeMessage(self,username,password, type):
        return type+" "+username+" "+str(hashlib.md5(password.encode()).hexdigest())
        
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''

print(str(hashlib.md5("12345".encode()).hexdigest()))