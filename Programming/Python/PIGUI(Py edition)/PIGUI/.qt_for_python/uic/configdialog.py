# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import CalcConfigResource_rc

class Ui_config(object):
    def setupUi(self, config):
        if not config.objectName():
            config.setObjectName(u"config")
        config.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/icon/src/gordon-johnson.with-permission.webp", QSize(), QIcon.Normal, QIcon.Off)
        config.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(config)
        self.tabWidget.setObjectName(u"tabWidget")
        self.calctypetab = QWidget()
        self.calctypetab.setObjectName(u"calctypetab")
        self.verticalLayout_2 = QVBoxLayout(self.calctypetab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.calctypetab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.radioButton = QRadioButton(self.calctypetab)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.calctypetab)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.calctypetab)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.calctypetab)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.calctypetab)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_2.addWidget(self.radioButton_5)

        self.verticalSpacer = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.calctypetab, "")
        self.calcnumtab = QWidget()
        self.calcnumtab.setObjectName(u"calcnumtab")
        self.gridLayout = QGridLayout(self.calcnumtab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.calcnumtab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.textEdit = QTextEdit(self.calcnumtab)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.calcnumtab)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.tabWidget.addTab(self.calcnumtab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(config)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(config)
        self.buttonBox.accepted.connect(config.accept)
        self.buttonBox.rejected.connect(config.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(config)
    # setupUi

    def retranslateUi(self, config):
        config.setWindowTitle(QCoreApplication.translate("config", u"Calculation Configuration", None))
        self.label.setText(QCoreApplication.translate("config", u"Calculation Type:", None))
        self.radioButton.setText(QCoreApplication.translate("config", u"Riemann Zeta", None))
        self.radioButton_2.setText(QCoreApplication.translate("config", u"Wallis Product", None))
        self.radioButton_3.setText(QCoreApplication.translate("config", u"Gregory-Leibniz", None))
        self.radioButton_4.setText(QCoreApplication.translate("config", u"Newer Gregory-Leibniz", None))
        self.radioButton_5.setText(QCoreApplication.translate("config", u"Montecalro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calctypetab), QCoreApplication.translate("config", u"Calculation Type", None))
        self.label_2.setText(QCoreApplication.translate("config", u"Number of trial\n"
"n th series", None))
        self.textBrowser.setHtml(QCoreApplication.translate("config", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans',''; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:18pt; font-weight:700; text-decoration: underline;\">Notice!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:18pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11p"
                        "t;\">The number must be written in standard form, not scientific notion or any other number displaying systems. And no comma's or period's for separation of number(ex. 1,000,000 or 1.000.000)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt;\">The correct way to input the number:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt;\">100000</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:11pt;\"><br /></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt;\">Incorrect way:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt;\">1*10^3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt;\">9,999,999</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt;\">9.999.999</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calcnumtab), QCoreApplication.translate("config", u"Trial Number/n th series", None))
    # retranslateUi

