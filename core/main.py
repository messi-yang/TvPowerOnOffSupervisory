#!/usr/bin/python  
# -*- coding: UTF-8 -*-

"""
author: Jeffrey
date: 2018/5/14
"""


import sys
import serial
import serial.tools.list_ports as list_ports
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from core.mainwindow import Ui_Form

ser = serial.Serial()
camera_list = []


class MainWindow(QWidget, Ui_Form):
    """
    Setup window
    """

    def __init__(self):
        """Constructor
        """

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.refresh_camera_list_btn.clicked.connect(self.refresh_camera_list)
        self.add_camera_btn.clicked.connect(self.add_camera)
        self.capture_std_btn.clicked.connect(self.capture_std)
        self.refresh_port_btn.clicked.connect(self.refresh_port)
        self.open_port_btn.clicked.connect(self.open_port)

    def refresh_camera_list(self):
        # self.camera_list.clear()
        # cameras = QCameraInfo.availableCameras()
        # if len(cameras) == 0:
        #     QMessageBox.information(self, 'Camera Info', "Haven't any camera device")
        #     return
        #
        # self.camera_list.setRowCount(len(cameras))
        # for item in cameras:
        #     self.camera_list.insertRow(len(cameras))
        #     print(self.camera_list.currentRow())
        #     cell = QTableWidgetItem('abc')
        #     self.camera_list.setItem(1, 0, cell)
        row_count = 10
        self.camera_list.setRowCount(row_count)
        for i in range(row_count):
            id = QTableWidgetItem('id %s' % (i + 1))
            name = QTableWidgetItem('name %s' % (i + 1))
            self.camera_list.setItem(i, 0, id)
            self.camera_list.setItem(i, 1, name)

    def add_camera(self):
        if self.camera_list.rowCount() == 0:
            pass

    def capture_std(self):
        pass

    def refresh_port(self):
        self.port_lists_combox.clear()
        com_list = list_ports.comports()
        port_name_list = []
        for port_item in com_list:
            port_name_list.append(port_item[0])
        self.port_lists_combox.addItems(sorted(port_name_list))

    def open_port(self):
        port_name = self.port_lists_combox.currentText()
        if port_name == '':
            QMessageBox.information(self, 'Invalid Port Name', 'Current selected port name is none')
            return

        ser.port = port_name
        if self.open_port_btn.text() == '关闭COM':
            ser.close()
            QMessageBox.information(self, 'Close Com Port', '{} has been closed successful'.format(port_name))
            self.open_port_btn.setText('打开COM')
            self.refresh_port_btn.setEnabled(True)
            self.port_lists_combox.setEnabled(True)
        else:
            try:
                ser.open()
                QMessageBox.information(self, 'Open Successful', '{} has been opened successful'.format(port_name))
                self.open_port_btn.setText('关闭COM')
                self.refresh_port_btn.setEnabled(False)
                self.port_lists_combox.setEnabled(False)
            except serial.SerialException as e:
                QMessageBox.information(self, 'Open Fail', e.__str__())


def run():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())