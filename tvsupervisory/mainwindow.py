# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1176, 689)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/tv.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 251, 248))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.capture_std_btn = QtWidgets.QPushButton(self.groupBox)
        self.capture_std_btn.setObjectName("capture_std_btn")
        self.gridLayout.addWidget(self.capture_std_btn, 1, 3, 1, 1)
        self.camera_table = QtWidgets.QTableWidget(self.groupBox)
        self.camera_table.setColumnCount(2)
        self.camera_table.setObjectName("camera_table")
        self.camera_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.camera_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.camera_table.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.camera_table, 0, 0, 1, 4)
        self.refresh_camera_table_btn = QtWidgets.QPushButton(self.groupBox)
        self.refresh_camera_table_btn.setObjectName("refresh_camera_table_btn")
        self.gridLayout.addWidget(self.refresh_camera_table_btn, 1, 1, 1, 1)
        self.add_camera_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_camera_btn.setObjectName("add_camera_btn")
        self.gridLayout.addWidget(self.add_camera_btn, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 263, 249, 223))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.power_box = QtWidgets.QWidget()
        self.power_box.setObjectName("power_box")
        self.formLayout = QtWidgets.QFormLayout(self.power_box)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.power_box)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_box_num = QtWidgets.QLineEdit(self.power_box)
        self.txt_box_num.setObjectName("txt_box_num")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_box_num)
        self.label_2 = QtWidgets.QLabel(self.power_box)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_box_interval = QtWidgets.QLineEdit(self.power_box)
        self.txt_box_interval.setObjectName("txt_box_interval")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_box_interval)
        self.stackedWidget.addWidget(self.power_box)
        self.direct_power = QtWidgets.QWidget()
        self.direct_power.setObjectName("direct_power")
        self.formLayout_2 = QtWidgets.QFormLayout(self.direct_power)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.direct_power)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_direct_num = QtWidgets.QLineEdit(self.direct_power)
        self.txt_direct_num.setObjectName("txt_direct_num")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_direct_num)
        self.label_4 = QtWidgets.QLabel(self.direct_power)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txt_direct_off_time = QtWidgets.QLineEdit(self.direct_power)
        self.txt_direct_off_time.setObjectName("txt_direct_off_time")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_direct_off_time)
        self.label_5 = QtWidgets.QLabel(self.direct_power)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txt_direct_power_key = QtWidgets.QLineEdit(self.direct_power)
        self.txt_direct_power_key.setObjectName("txt_direct_power_key")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_direct_power_key)
        self.label_6 = QtWidgets.QLabel(self.direct_power)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txt_direct_interval = QtWidgets.QLineEdit(self.direct_power)
        self.txt_direct_interval.setObjectName("txt_direct_interval")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_direct_interval)
        self.stackedWidget.addWidget(self.direct_power)
        self.pro800_power = QtWidgets.QWidget()
        self.pro800_power.setObjectName("pro800_power")
        self.formLayout_3 = QtWidgets.QFormLayout(self.pro800_power)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.pro800_power)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txt_cross_num = QtWidgets.QLineEdit(self.pro800_power)
        self.txt_cross_num.setObjectName("txt_cross_num")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_cross_num)
        self.label_8 = QtWidgets.QLabel(self.pro800_power)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txt_cross_address = QtWidgets.QLineEdit(self.pro800_power)
        self.txt_cross_address.setObjectName("txt_cross_address")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_cross_address)
        self.label_9 = QtWidgets.QLabel(self.pro800_power)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txt_cross_on_key = QtWidgets.QLineEdit(self.pro800_power)
        self.txt_cross_on_key.setObjectName("txt_cross_on_key")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_cross_on_key)
        self.label_10 = QtWidgets.QLabel(self.pro800_power)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.txt_cross_off_key = QtWidgets.QLineEdit(self.pro800_power)
        self.txt_cross_off_key.setObjectName("txt_cross_off_key")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_cross_off_key)
        self.label_21 = QtWidgets.QLabel(self.pro800_power)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.txt_cross_interval = QtWidgets.QLineEdit(self.pro800_power)
        self.txt_cross_interval.setObjectName("txt_cross_interval")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_cross_interval)
        self.stackedWidget.addWidget(self.pro800_power)
        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 490, 251, 93))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.result_dir_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.result_dir_txt.setObjectName("result_dir_txt")
        self.gridLayout_6.addWidget(self.result_dir_txt, 0, 0, 1, 2)
        self.result_dir_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.result_dir_btn.setObjectName("result_dir_btn")
        self.gridLayout_6.addWidget(self.result_dir_btn, 0, 2, 1, 2)
        self.refresh_port_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.refresh_port_btn.setObjectName("refresh_port_btn")
        self.gridLayout_6.addWidget(self.refresh_port_btn, 1, 0, 1, 1)
        self.port_lists_combox = QtWidgets.QComboBox(self.groupBox_3)
        self.port_lists_combox.setObjectName("port_lists_combox")
        self.gridLayout_6.addWidget(self.port_lists_combox, 1, 1, 1, 2)
        self.open_port_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.open_port_btn.setObjectName("open_port_btn")
        self.gridLayout_6.addWidget(self.open_port_btn, 1, 3, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 20, 831, 531))
        self.groupBox_4.setObjectName("groupBox_4")
        self.camera_tab = QtWidgets.QTabWidget(self.groupBox_4)
        self.camera_tab.setGeometry(QtCore.QRect(10, 20, 811, 501))
        self.camera_tab.setObjectName("camera_tab")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(540, 590, 296, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.start_supervision_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.start_supervision_btn.setObjectName("start_supervision_btn")
        self.horizontalLayout_6.addWidget(self.start_supervision_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.camera_tab.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TvSupervisory"))
        self.groupBox.setTitle(_translate("Form", "CameraSetting"))
        self.capture_std_btn.setText(_translate("Form", "拍摄标准图"))
        item = self.camera_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.camera_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        self.refresh_camera_table_btn.setText(_translate("Form", "刷新列表"))
        self.add_camera_btn.setText(_translate("Form", "打开摄像头"))
        self.groupBox_2.setTitle(_translate("Form", "PowerType"))
        self.label.setText(_translate("Form", "开关机次数"))
        self.label_2.setText(_translate("Form", "拍摄时间间隔"))
        self.label_3.setText(_translate("Form", "开关机次数"))
        self.label_4.setText(_translate("Form", "关机时间"))
        self.label_5.setText(_translate("Form", "电源键值"))
        self.label_6.setText(_translate("Form", "拍摄时间间隔"))
        self.label_7.setText(_translate("Form", "开关机次数"))
        self.label_8.setText(_translate("Form", "继电器地址"))
        self.label_9.setText(_translate("Form", "开机键值"))
        self.label_10.setText(_translate("Form", "关机键值"))
        self.label_21.setText(_translate("Form", "拍摄时间间隔"))
        self.comboBox.setItemText(0, _translate("Form", "电源箱交流"))
        self.comboBox.setItemText(1, _translate("Form", "红外直流"))
        self.comboBox.setItemText(2, _translate("Form", "PRO800交流"))
        self.groupBox_3.setTitle(_translate("Form", "BasicSetting"))
        self.result_dir_btn.setText(_translate("Form", "结果路径"))
        self.refresh_port_btn.setText(_translate("Form", "刷新"))
        self.open_port_btn.setText(_translate("Form", "打开COM"))
        self.groupBox_4.setTitle(_translate("Form", "Video"))
        self.start_supervision_btn.setText(_translate("Form", "开始监控"))
        self.pushButton_3.setText(_translate("Form", "查看报告"))

