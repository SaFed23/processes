import sys
import os
import psutil
import ctypes
import signal
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import interface

helper = ctypes.cdll.LoadLibrary('./helper.so')
about = ctypes.cdll.LoadLibrary('./about.so')


class About:
    def __init__(self):
        self.obj = about.About_new()

    def about(self):
        about.getStr.restype = ctypes.c_wchar_p
        return about.getStr("")


class ProcessesApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    pid_on_delete = None
    name_of_process_on_delete = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableOfProcesses.setColumnCount(3)
        self.tableOfProcesses.horizontalHeader().setStretchLastSection(True)
        self.tableOfProcesses.setHorizontalHeaderLabels(('PID', 'Username', 'Name of Process'))
        self.inputField.setStyleSheet("QTextEdit {background-color:black; color:white}")
        self.printButton.clicked.connect(self.print_all_processes)
        self.tableOfProcesses.cellClicked.connect(self.init_current_proc)
        self.deleteButton.clicked.connect(self.delete)
        self.createButton.clicked.connect(self.create_process)
        self.aboutButton.clicked.connect(self.about)

    def print_all_processes(self):
        self.tableOfProcesses.setRowCount(0)
        row = 0
        all_processes = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            except psutil.NoSuchProcess:
                pass
            else:
                self.tableOfProcesses.insertRow(row)
                item_pid = QtWidgets.QTableWidgetItem(str(pinfo['pid']))
                item_pid.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item_username = QtWidgets.QTableWidgetItem(pinfo['username'])
                item_username.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item_name = QtWidgets.QTableWidgetItem(pinfo['name'])
                item_name.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableOfProcesses.setItem(row, 0, item_pid)
                self.tableOfProcesses.setItem(row, 1, item_username)
                self.tableOfProcesses.setItem(row, 2, item_name)
                row += 1
                all_processes.append(pinfo['name'])
        helper.print_all_processes_in_file(ctypes.c_wchar_p("\n".join(all_processes)))

    def init_current_proc(self, row):
        self.pid_on_delete = self.tableOfProcesses.item(row, 0).text()
        self.name_of_process_on_delete = self.tableOfProcesses.item(row, 2).text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Info")
        msg.setWindowTitle("Info")
        helper.message_about_process.restype = ctypes.c_wchar_p
        msg.setInformativeText(helper.message_about_process(ctypes.c_wchar_p(self.name_of_process_on_delete)))
        msg.exec_()

    def delete(self):
        if self.pid_on_delete is None:
            pass
        else:
            try:
                helper.print_delete_processes_in_file(ctypes.c_wchar_p(self.name_of_process_on_delete))
                os.system("pkill " + self.name_of_process_on_delete)
                self.pid_on_delete = None
                self.print_all_processes()
            except psutil.NoSuchProcess:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Oops...")
                msg.setInformativeText("Process with this pid doesn't exist. Please update the list of processes")
                msg.setWindowTitle("Warning")
                msg.exec_()

    def create_process(self):
        os.system(self.inputField.toPlainText())

    def about(self):
        about = About()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("About")
        msg.setWindowTitle("About")
        msg.setInformativeText(about.about())
        msg.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProcessesApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
