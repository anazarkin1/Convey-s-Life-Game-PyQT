# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created: Mon Jul 30 02:08:04 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(803, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 631, 381))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.grpBox_Tools = QtGui.QGroupBox(self.centralwidget)
        self.grpBox_Tools.setGeometry(QtCore.QRect(30, 410, 621, 131))
        self.grpBox_Tools.setAutoFillBackground(True)
        self.grpBox_Tools.setObjectName(_fromUtf8("grpBox_Tools"))
        self.btn_Exit = QtGui.QPushButton(self.grpBox_Tools)
        self.btn_Exit.setGeometry(QtCore.QRect(520, 30, 91, 51))
        self.btn_Exit.setObjectName(_fromUtf8("btn_Exit"))
        self.grpBox_AutoGen = QtGui.QGroupBox(self.grpBox_Tools)
        self.grpBox_AutoGen.setGeometry(QtCore.QRect(10, 20, 281, 80))
        self.grpBox_AutoGen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.grpBox_AutoGen.setFlat(False)
        self.grpBox_AutoGen.setObjectName(_fromUtf8("grpBox_AutoGen"))
        self.sld_GenSpeed = QtGui.QSlider(self.grpBox_AutoGen)
        self.sld_GenSpeed.setGeometry(QtCore.QRect(30, 30, 111, 19))
        self.sld_GenSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.sld_GenSpeed.setObjectName(_fromUtf8("sld_GenSpeed"))
        self.btn_AutoGen = QtGui.QPushButton(self.grpBox_AutoGen)
        self.btn_AutoGen.setGeometry(QtCore.QRect(150, 10, 111, 51))
        self.btn_AutoGen.setObjectName(_fromUtf8("btn_AutoGen"))
        self.lbl_GenSpeed = QtGui.QLabel(self.grpBox_AutoGen)
        self.lbl_GenSpeed.setGeometry(QtCore.QRect(50, 50, 67, 21))
        self.lbl_GenSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_GenSpeed.setObjectName(_fromUtf8("lbl_GenSpeed"))
        self.btn_NextGen = QtGui.QPushButton(self.grpBox_Tools)
        self.btn_NextGen.setGeometry(QtCore.QRect(280, 30, 111, 51))
        self.btn_NextGen.setObjectName(_fromUtf8("btn_NextGen"))
        self.btn_New = QtGui.QPushButton(self.grpBox_Tools)
        self.btn_New.setGeometry(QtCore.QRect(400, 30, 111, 51))
        self.btn_New.setObjectName(_fromUtf8("btn_New"))
        self.lbl_FpsText = QtGui.QLabel(self.centralwidget)
        self.lbl_FpsText.setGeometry(QtCore.QRect(670, 20, 67, 21))
        self.lbl_FpsText.setObjectName(_fromUtf8("lbl_FpsText"))
        self.lbl_Fps = QtGui.QLabel(self.centralwidget)
        self.lbl_Fps.setGeometry(QtCore.QRect(670, 40, 67, 21))
        self.lbl_Fps.setObjectName(_fromUtf8("lbl_Fps"))
        self.lbl_NumOfGen = QtGui.QLabel(self.centralwidget)
        self.lbl_NumOfGen.setGeometry(QtCore.QRect(670, 90, 67, 21))
        self.lbl_NumOfGen.setObjectName(_fromUtf8("lbl_NumOfGen"))
        self.lbl_NumOfGenText = QtGui.QLabel(self.centralwidget)
        self.lbl_NumOfGenText.setGeometry(QtCore.QRect(670, 70, 111, 21))
        self.lbl_NumOfGenText.setObjectName(_fromUtf8("lbl_NumOfGenText"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.grpBox_Tools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.grpBox_AutoGen.setTitle(QtGui.QApplication.translate("MainWindow", "AutoGen:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_AutoGen.setText(QtGui.QApplication.translate("MainWindow", "Start/Stop \n"
"Auto Generation", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_GenSpeed.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_NextGen.setText(QtGui.QApplication.translate("MainWindow", "Next Generation", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_New.setText(QtGui.QApplication.translate("MainWindow", "Start New Life", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_FpsText.setText(QtGui.QApplication.translate("MainWindow", "FPS:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_Fps.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_NumOfGen.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_NumOfGenText.setText(QtGui.QApplication.translate("MainWindow", "# Generation", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

