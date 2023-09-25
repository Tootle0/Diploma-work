
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcome_screen(object):
    def setupUi(self, welcome_screen):
        welcome_screen.setObjectName("welcome_screen")
        welcome_screen.resize(470, 430)
        welcome_screen.setStyleSheet("background-color: rgb(183, 229, 176);")
        self.centralwidget = QtWidgets.QWidget(welcome_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.header_lb = QtWidgets.QLabel(self.centralwidget)
        self.header_lb.setGeometry(QtCore.QRect(120, 60, 251, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.header_lb.setFont(font)
        self.header_lb.setObjectName("header_lb")
        self.generate_keys_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_keys_btn.setGeometry(QtCore.QRect(50, 140, 101, 41))
        self.generate_keys_btn.setDefault(True)
        self.generate_keys_btn.setFlat(False)
        self.generate_keys_btn.setObjectName("generate_keys_btn")
        self.encryption_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encryption_btn.setGeometry(QtCore.QRect(50, 210, 101, 41))
        self.encryption_btn.setDefault(True)
        self.encryption_btn.setObjectName("encryption_btn")
        self.decryption_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decryption_btn.setGeometry(QtCore.QRect(50, 280, 101, 41))
        self.decryption_btn.setDefault(True)
        self.decryption_btn.setObjectName("decryption_btn")
        self.htu_lb = QtWidgets.QLabel(self.centralwidget)
        self.htu_lb.setGeometry(QtCore.QRect(240, 120, 101, 21))
        self.htu_lb.setScaledContents(True)
        self.htu_lb.setObjectName("htu_lb")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 120, 251, 201))
        self.label_3.setObjectName("label_3")
        welcome_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcome_screen)
        QtCore.QMetaObject.connectSlotsByName(welcome_screen)

    def retranslateUi(self, welcome_screen):
        _translate = QtCore.QCoreApplication.translate
        welcome_screen.setWindowTitle(
            _translate("welcome_screen", "MainWindow"))
        self.header_lb.setText(_translate(
            "welcome_screen", "Welcome to Password Encryption Tool(PET)"))
        self.generate_keys_btn.setText(
            _translate("welcome_screen", "Generate Keys"))
        self.encryption_btn.setText(_translate("welcome_screen", "Encryption"))
        self.decryption_btn.setText(_translate("welcome_screen", "Decryption"))
        self.htu_lb.setText(_translate("welcome_screen", "How to use:"))
        self.label_3.setText(_translate("welcome_screen", "Step 1: Generate Keys and store them safely on\n"
                                        " your local machine\n"
                                        "Step 2: Encrypt/Decrypt your Message\n"
                                        "Step 3: Save the output for later use!"))
