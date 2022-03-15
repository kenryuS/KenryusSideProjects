# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowKcEGZW.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QMessageBox)
import MainWinResource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 480)
        icon = QIcon()
        icon.addFile(u":/icon/src/gordon-johnson.with-permission.webp", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_About_the_Program = QAction(MainWindow)
        self.action_About_the_Program.setObjectName(u"action_About_the_Program")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.StartBTN = QPushButton(self.centralwidget)
        self.StartBTN.setObjectName(u"StartBTN")
        self.StartBTN.setEnabled(True)
        self.StartBTN.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/src/YctSHrw8bPz94HrLyfyruB-320-80.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.StartBTN.setIcon(icon1)
        self.StartBTN.setIconSize(QSize(320, 320))
        self.StartBTN.setAutoDefault(True)
        self.StartBTN.setFlat(False)

        self.gridLayout.addWidget(self.StartBTN, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 23))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menu_File.addAction(self.action_Exit)
        self.menu_About.addAction(self.action_About_the_Program)

        self.retranslateUi(MainWindow)
        self.action_Exit.triggered.connect(MainWindow.close)
        self.action_About_the_Program.triggered.connect(self.helpdialog)

        self.StartBTN.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PySolver - The PI Calculation Program", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_About_the_Program.setText(QCoreApplication.translate("MainWindow", u"&About the Program", None))
#if QT_CONFIG(tooltip)
        self.StartBTN.setToolTip(QCoreApplication.translate("MainWindow", u"Start the Calculation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.StartBTN.setWhatsThis(QCoreApplication.translate("MainWindow", u"Press button to start the calculation.", None))
#endif // QT_CONFIG(whatsthis)
        self.StartBTN.setText("")
#if QT_CONFIG(shortcut)
        self.StartBTN.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"PySolver - The PI Calculator", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

    def helpdialog(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("About the Program")
        dialog.setText("PI Calculator\n\nThe software which will allows you to calculate the value of PI in multiple methods.\n\nNotice!\nSince python uses internal math library and float decimal point, the accuracy and the available digits are limited. Also I recommend to set the proiority of software very high to obtain the maximum performance possible through task manager.\n\nDeveloped by:\nKenryuS(GitHub)")
        button = dialog.exec()

