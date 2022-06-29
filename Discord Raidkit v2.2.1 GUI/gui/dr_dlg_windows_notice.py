# Form implementation generated from reading ui file 'dr_dlg_windows_notice.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgWindowsNotice(object):
    def setupUi(self, dlgWindowsNotice):
        dlgWindowsNotice.setObjectName("dlgWindowsNotice")
        dlgWindowsNotice.resize(362, 158)
        dlgWindowsNotice.setMinimumSize(QtCore.QSize(362, 158))
        dlgWindowsNotice.setMaximumSize(QtCore.QSize(362, 158))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        dlgWindowsNotice.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgWindowsNotice.setWindowIcon(icon)
        self.dlgWindowsNoticeBtnBox = QtWidgets.QDialogButtonBox(dlgWindowsNotice)
        self.dlgWindowsNoticeBtnBox.setGeometry(QtCore.QRect(248, 110, 100, 32))
        self.dlgWindowsNoticeBtnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dlgWindowsNoticeBtnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.dlgWindowsNoticeBtnBox.setCenterButtons(True)
        self.dlgWindowsNoticeBtnBox.setObjectName("dlgWindowsNoticeBtnBox")
        self.lblTitle = QtWidgets.QLabel(dlgWindowsNotice)
        self.lblTitle.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblWindowsNoticeDesc1 = QtWidgets.QLabel(dlgWindowsNotice)
        self.lblWindowsNoticeDesc1.setGeometry(QtCore.QRect(20, 60, 321, 16))
        self.lblWindowsNoticeDesc1.setObjectName("lblWindowsNoticeDesc1")
        self.lblWindowsNoticeDesc2 = QtWidgets.QLabel(dlgWindowsNotice)
        self.lblWindowsNoticeDesc2.setGeometry(QtCore.QRect(20, 80, 331, 16))
        self.lblWindowsNoticeDesc2.setObjectName("lblWindowsNoticeDesc2")
        self.lblWindowsNoticeDesc3 = QtWidgets.QLabel(dlgWindowsNotice)
        self.lblWindowsNoticeDesc3.setGeometry(QtCore.QRect(20, 100, 161, 16))
        self.lblWindowsNoticeDesc3.setObjectName("lblWindowsNoticeDesc3")

        self.retranslateUi(dlgWindowsNotice)
        self.dlgWindowsNoticeBtnBox.accepted.connect(dlgWindowsNotice.accept) # type: ignore
        self.dlgWindowsNoticeBtnBox.rejected.connect(dlgWindowsNotice.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgWindowsNotice)

    def retranslateUi(self, dlgWindowsNotice):
        _translate = QtCore.QCoreApplication.translate
        dlgWindowsNotice.setWindowTitle(_translate("dlgWindowsNotice", "Payload Error"))
        self.lblTitle.setText(_translate("dlgWindowsNotice", "Payload Error"))
        self.lblWindowsNoticeDesc1.setText(_translate("dlgWindowsNotice", "Some fields entered contained invalid names"))
        self.lblWindowsNoticeDesc2.setText(_translate("dlgWindowsNotice", "for Windows OS."))
        self.lblWindowsNoticeDesc3.setText(_translate("dlgWindowsNotice", "Please enter different data."))