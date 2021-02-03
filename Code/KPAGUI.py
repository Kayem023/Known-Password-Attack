# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from client import Client
import hashlib
import random
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.passwordProperties='''Qualities of a strong password\n
        1. 12 Characters or More
        2. Mixed and Matched Caps, Symbols, and Numbers
        3. No obvious substiturions
        4. Not in the Dictionary
        5. Does not contain names
        6. Does not contain phone or address numbers
        7. Unique'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 919)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 0, 211, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Norasi")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Kinnari")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(570, 510, 500, 51))
        self.submit.setStyleSheet("background-color:magenta;\n"
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
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(18)
        font.setItalic(True)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 680, 1101, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.userText = QtWidgets.QLineEdit(self.centralwidget)
        self.userText.setGeometry(QtCore.QRect(570, 310, 500, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.userText.setFont(font)
        self.userText.setObjectName("userText")
        self.userButton = QtWidgets.QPushButton(self.centralwidget)
        self.userButton.setGeometry(QtCore.QRect(270, 310, 271, 51))
        self.userButton.setStyleSheet("background-color:blue;\n"
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
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(18)
        font.setItalic(True)
        self.userButton.setFont(font)
        self.userButton.setObjectName("userButton")
        self.passText = QtWidgets.QLineEdit(self.centralwidget)
        self.passText.setGeometry(QtCore.QRect(570, 410, 500, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.passText.setFont(font)
        self.passText.setObjectName("passText")
        self.passwordButton = QtWidgets.QPushButton(self.centralwidget)
        self.passwordButton.setGeometry(QtCore.QRect(270, 410, 271, 51))
        self.passwordButton.setStyleSheet("background-color:blue;\n"
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
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(18)
        font.setItalic(True)
        self.passwordButton.setFont(font)
        self.passwordButton.setObjectName("passwordButton")
        self.prevent = QtWidgets.QPushButton(self.centralwidget)
        self.prevent.setGeometry(QtCore.QRect(570, 220, 500, 51))
        self.prevent.setStyleSheet("background-color:green;\n"
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
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(18)
        font.setItalic(True)
        self.prevent.setFont(font)
        self.prevent.setObjectName("prevent")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(570, 590, 500, 51))
        self.reset.setStyleSheet("background-color:black;\n"
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
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(18)
        font.setItalic(True)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.submit.clicked.connect(self.submitButtonHandler)
        self.reset.clicked.connect(self.resetButtonHandler)
        self.userButton.clicked.connect(self.username_FileHandler)
        self.passwordButton.clicked.connect(self.password_FileHandler)
        self.prevent.clicked.connect(self.makepasswordHandler)
        
        self.client= Client()
        self.passFile = False
        self.userFile = False

        self.browserText = " Enter filename or text of username or password by corresponding buttons\n Enter submit button to initiate attack\n Enter makepassword button to get a strong password to crack"
        self.textBrowser.setText(self.browserText)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.label_3.setText(_translate("MainWindow", "Password "))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.userButton.setText(_translate("MainWindow", "Choose File"))
        self.passwordButton.setText(_translate("MainWindow", "Choose File"))
        self.prevent.setText(_translate("MainWindow", "Make Password"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        
    def submitButtonHandler(self):
        print("submit clicked")
        if self.passFile and self.userFile:
            if self.checkFormatOfFile(self.userText.text()) and self.checkFormatOfFile(self.passText.text()):
                print("valid both file")
                count =0
                totalcount =0
                with open(self.userText.text(), "r") as userFile:
                    with open(self.passText.text(), "r") as passFile:
                        userFiledata= userFile.readlines()
                        passFiledata= passFile.readlines()
                        with open("out.txt","wb") as outFile:
                            for usersline in userFiledata:
                                usersline = usersline.replace('\n','')
                                users = usersline.split()
                                print(users)
                                for passline in passFiledata:
                                    passline = passline.replace('\n','')
                                    passwords = passline.split()
                                    print(passwords)
                                    for user in users:
                                        for password in passwords:
                                            totalcount= totalcount + 1
                                            result = self.processRequest(user,password)
                                            #time.sleep(5)
                                            print(user+" "+password)
                                            if result == 1:
                                                count = count + 1
                                                outFile.write(bytearray((user+" "+password+"\n"),'utf-8'))
                                                break
            print("total matched: "+ str(count)+" out of "+str(totalcount))
            self.textBrowser.setText("total matched: "+ str(count)+" out of "+str(totalcount))
            pass
        else:
            if self.passFile:
                if self.checkFormatOfFile(self.passText.text()) and len(self.userText.text())>0 :
                    print("passFile only")
                    with open(self.passText.text(), "r") as passFile:
                        passFiledata= passFile.readlines()
                        flag = False
                        for passline in passFiledata:
                            passline = passline.replace('\n','')
                            passwords = passline.split()
                            print(passwords)
                            for password in passwords:
                                result = self.processRequest(self.userText.text(),password)
                                #time.sleep(5)
                                print(self.userText.text()+" "+password)
                                if result == 1:
                                    self.textBrowser.setText("User is matched with password :  "+password)
                                    flag = True
                                    break
                            if flag:
                                break
                        if flag == False:
                            self.textBrowser.setText("username does not match with password file")
                    pass
                else:
                    self.textBrowser.setText("Select user File or give a user")
            else:
                if self.userFile:
                    if self.checkFormatOfFile(self.userText.text()) and len(self.passText.text())>0 :
                        print("userFile only")
                        with open(self.userText.text(), "r") as userFile:
                            userFiledata= userFile.readlines()
                            flag = False
                            for userline in userFiledata:
                                userline = userline.replace('\n','')
                                users = userline.split()
                                print(users)
                                for user in users:
                                    result = self.processRequest(user,self.passText.text())
                                    #time.sleep(5)
                                    print(user+" "+self.passText.text())
                                    if result == 1:
                                        self.textBrowser.setText("Password is matched with user :  "+user)
                                        flag = True
                                        break
                                if flag:
                                    break
                            if flag == False:
                                self.textBrowser.setText("password does not match with any username")
                    else:
                        self.textBrowser.setText("Select password File or give a password")
                else:
                    print("login entered")
                    username = self.userText.text()
                    password = self.passText.text()
                    result = self.processRequest(username,password)
                    if result == 1:
                        self.textBrowser.setText("Username and password matched")
                    if result == 2:
                        self.textBrowser.setText("Enter username and password")
                    if result == 0:
                        self.textBrowser.setText("Username and password do not matched")
        
    def processRequest(self,username , password):
        if len(username)>0  and  len(password)>0 :
            sendMsg = self.makeMessage(username, password,"login")
            self.client.send(sendMsg)
            response = self.client.receive()
            print(response)
            if response=="OK":
                return 1
            if response == "NO":
                return 0
        else:
            return 2
        
    def resetButtonHandler(self):
        print("reset clicked")
        self.userText.setEnabled(True)
        self.userText.clear()
        self.passText.setEnabled(True)
        self.passText.clear()
        self.passFile = False
        self.userFile = False
        self.textBrowser.clear()
        self.textBrowser.setText(self.browserText)
        
    def username_FileHandler(self):
        print("user clicked")
        filename = self.open_dialog_box()
        print(filename)
        
        if filename :
            self.userText.setText(filename)
            self.userText.setDisabled(True)
            self.userFile = True
        else:
            pass
        
    def makeMessage(self,username,password, type):
        return type+" "+username+" "+str(hashlib.md5(password.encode()).hexdigest())
    
    def checkFormatOfFile(self,filename):
        if filename.endswith(".txt"):
            return True
        return False
    
    
    def password_FileHandler(self):
        print("password clicked")
        filename = self.open_dialog_box()
        print(filename)
        
        if filename :
            self.passText.setText(filename)
            self.passText.setDisabled(True)
            self.passFile = True
        else:
            pass
        
    def makepasswordHandler(self):
        print("make password clicked")
        #self.textBrowser.setText("Guidelines for Strong Passwords\n\n1.At least 8 characters—the more characters, the better\n2. A mixture of both uppercase and lowercase letters\n3. A mixture of letters and numbers\n4. Inclusion of at least one special character, e.g., ! @ # ? ]");
        
        passlength = random.randint(12,20)
        print(passlength)
        special = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']','{','}','|','\\',':',';','\'','"','?','/','>','<','.',',']
        number = ['0','1','2','3','4','5','6','7','8','9']
        capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        small   = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        fullset = special+number+capital+small
        print(special)
        print(number)
        print(capital)
        print(small)
        print(fullset)
        password = [' ' for i in range(passlength)]
        
        rand1 = random.randint(0,2)
        rand2 = random.randint(3,5)
        rand3 = random.randint(6,8)
        rand4 = random.randint(9,11)
        print(rand1)
        print(rand2)
        print(rand3)
        print(rand4)
        password[rand1] = small[random.randint(0,len(small)-1)]
        password[rand2] = number[random.randint(0,len(number)-1)]
        password[rand3] = special[random.randint(0,len(special)-1)]
        password[rand4] = capital[random.randint(0,len(capital)-1)]
        
        for i in range(passlength):
            if password[i] == ' ':
                password[i] = fullset[random.randint(0, len(fullset)-1)]
                
        self.textBrowser.setText("\nYour strong password is  : "+"".join(password)+"\n")
        self.textBrowser.append(self.passwordProperties)
            
            
        
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        return path
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
