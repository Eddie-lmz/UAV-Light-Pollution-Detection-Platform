from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
import tcp_logic, udp_logic, web_logic
import socket
import sys
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 733)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 100, 441, 491))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-top-right-radius:30px;\n"
                                   "border-bottom-right-radius:30px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(500, 130, 281, 51))
        self.frame.setStyleSheet("#frame{\n"
                                 "    color: rgb(85, 0, 255);\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 191, 28))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
                                      "    border:none;\n"
                                      "}\n"
                                      "#pushButton:focus{\n"
                                      "    color: rgb(207, 207, 207);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 51, 41))
        self.label_3.setStyleSheet("image: url(picture/UAVicon.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 100, 340, 490))
        self.label.setStyleSheet("border-image: url(picture/UAVlogin1.jpg);\n"
                                 "border-top-left-radius:30px;\n"
                                 "border-bottom-left-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 110, 31, 31))
        self.pushButton_3.setStyleSheet("border:none;")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/logouticon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setShortcut('esc')
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(430, 200, 411, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
                                    "border-radius:10px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 80, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
                                      "border-radius:10px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 140, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:1px solid rgb(0,0,0);\n"
                                      "border-radius:10px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:1px solid rgb(0,0,0);\n"
                                      "border-radius:10px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 260, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
                                      "border-radius:10px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 320, 171, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
                                        "    background-color: rgb(149, 149, 149);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border:3px solid rgb(149, 149, 149);\n"
                                        "    border-radius:8px;\n"
                                        "}\n"
                                        "#pushButton_2:hover{\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    color: rgb(149, 149, 149);\n"
                                        "}\n"
                                        "#pushButton_2:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px;\n"
                                        "}")
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setShortcut('enter')
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(220, 320, 51, 31))
        self.label_4.setStyleSheet("image: url(picture/enterkeyicon.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 110, 31, 31))
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("picture/iconshide.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(43, 33))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_3.clicked.connect(Form.close)  # type: ignore
        self.pushButton_4.clicked.connect(Form.showMinimized)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "无人机光污染检测平台"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  账号："))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  密码："))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "  IP："))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "  端口："))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "  数据库："))
        self.pushButton_2.setText(_translate("Form", "登录"))


class MainWindow(tcp_logic.TcpLogic, udp_logic.UdpLogic, web_logic.WebLogic):
    def __init__(self, num):
        super(MainWindow, self).__init__(num)
        self.client_socket_list = list()
        self.another = None
        self.link = False

        # 打开软件时默认获取本机ip
        self.click_get_ip()

    def connect(self, ):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # 如需传递参数可以修改为connect(lambda: self.click(参数))
        super(MainWindow, self).connect()
        self.pushButton_link.clicked.connect(self.click_link)
        self.pushButton_unlink.clicked.connect(self.click_unlink)
        self.pushButton_get_ip.clicked.connect(self.click_get_ip)
        self.pushButton_clear.clicked.connect(self.click_clear)
        self.pushButton_send.clicked.connect(self.send)
        self.pushButton_dir.clicked.connect(self.click_dir)
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_else.clicked.connect(self.another_window)
        self.pushButton_datasave.clicked.connect(self.saveFile)
        self.pushButton_dataimport.clicked.connect(self.inputFile)


    def click_link(self):
        """
        pushbutton_link控件点击触发的槽
        :return: None
        """
        # 连接时根据用户选择的功能调用函数
        if self.comboBox_tcp.currentIndex() == 0:
            self.tcp_server_start()
        if self.comboBox_tcp.currentIndex() == 1:
            self.tcp_client_start()
        if self.comboBox_tcp.currentIndex() == 2:
            self.udp_server_start()
        if self.comboBox_tcp.currentIndex() == 3:
            self.udp_client_start()
        if self.comboBox_tcp.currentIndex() == 4:
            self.web_server_start()
        self.link = True
        self.pushButton_unlink.setEnabled(True)
        self.pushButton_link.setEnabled(False)

    def click_unlink(self):
        """
        pushbutton_unlink控件点击触发的槽
        :return: None
        """
        # 关闭连接
        self.close_all()
        self.link = False
        self.pushButton_unlink.setEnabled(False)
        self.pushButton_link.setEnabled(True)

    def click_get_ip(self):
        """
        pushbutton_get_ip控件点击触发的槽
        :return: None
        """
        # 获取本机ip
        self.lineEdit_ip_local.clear()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            my_addr = s.getsockname()[0]
            self.lineEdit_ip_local.setText(str(my_addr))
        except Exception as ret:
            # 若无法连接互联网使用，会调用以下方法
            try:
                my_addr = socket.gethostbyname(socket.gethostname())
                self.lineEdit_ip_local.setText(str(my_addr))
            except Exception as ret_e:
                self.signal_write_msg.emit("无法获取ip，请连接网络！\n")
        finally:
            s.close()

    def send(self):
        """
        pushbutton_send控件点击触发的槽
        :return:
        """
        # 连接时根据用户选择的功能调用函数
        if self.comboBox_tcp.currentIndex() == 0 or self.comboBox_tcp.currentIndex() == 1:
            self.tcp_send()
        if self.comboBox_tcp.currentIndex() == 2 or self.comboBox_tcp.currentIndex() == 3:
            self.udp_send()
        if self.comboBox_tcp.currentIndex() == 4:
            self.web_send()

    def click_clear(self):
        """
        pushbutton_clear控件点击触发的槽
        :return: None
        """
        # 清空接收区屏幕
        self.textBrowser_recv.clear()

    def click_dir(self):
        # WEB服务端功能中选择路径
        self.web_get_dir()

    def close_all(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        # 连接时根据用户选择的功能调用函数
        if self.comboBox_tcp.currentIndex() == 0 or self.comboBox_tcp.currentIndex() == 1:
            self.tcp_close()
        if self.comboBox_tcp.currentIndex() == 2 or self.comboBox_tcp.currentIndex() == 3:
            self.udp_close()
        if self.comboBox_tcp.currentIndex() == 4:
            self.web_close()
        self.reset()

    def reset(self):
        """
        功能函数，将按钮重置为初始状态
        :return:None
        """
        self.link = False
        self.client_socket_list = list()
        self.pushButton_unlink.setEnabled(False)
        self.pushButton_link.setEnabled(True)

    def another_window(self):
        """
        开启一个新的窗口的方法
        :return:
        """
        # 弹出一个消息框，提示开启了一个新的窗口
        QtWidgets.QMessageBox.warning(self,
                                      '光污染检测UAV网络测试助手',
                                      "已经开启了新的光污染检测UAV网络测试助手！",
                                      QtWidgets.QMessageBox.Yes)
        # 计数，开启了几个窗口
        self.num = self.num + 1
        # 开启新的窗口
        self.another = MainWindow(self.num)
        self.another.show()

    def inputFile(self):
        '''导入信息'''
        try:
            directory1 = QFileDialog.getOpenFileName(None, "选择文件", '', 'json(*.json)')
            # self.signal_write_msg.emit(str(directory1))
            # print(directory1)  # 打印文件夹路径
            path = directory1[0]
            if path != '':
                # with open(file=path, mode='r', encoding='utf8') as file:
                #     items = json.load(file)['database']
                #     self.tableWidget.setRowCount(0)
                #     self.tableWidget.clearContents()
                #     self.freshTable(items)
                pass
        except:
            QMessageBox.critical(self, '警告', '导入文件出错')

    def saveFile(self):
        '''导出信息'''
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", '', 'json(*.json)')
        save_path = fileName2
        if save_path != '':
            items = []
            # for i in range(self.tableWidget.rowCount()):
            #     lis = []
            #     for g in range(self.tableWidget.columnCount()):  # 此处是7行
            #         if self.tableWidget.item(i, g):
            #             lis.append(self.tableWidget.item(i, g).text())
            #     items.append(lis)
            pass
            with open(file=save_path, mode='w+', encoding='utf8') as file:
                file.write(json.dumps({"database": items}))

class Main(QDialog, Ui_Form):
    def __init__(self):
        super(Main, self).__init__()
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('无人机光污染检测平台')
        self.pushButton_2.clicked.connect(self.login)
    def login(self):
        global gl_host,gl_port,gl_pwd
        gl_db = self.lineEdit_5.text()
        gl_host = self.lineEdit_3.text()
        gl_pwd = self.lineEdit_2.text()
        gl_user = self.lineEdit.text()
        gl_port = self.lineEdit_4.text()
        if gl_user == 'UAV' :
            if gl_db == 'UAV' :
                self.close()
                self.index_ui = MainWindow(1)
                self.index_ui.show()
            else:
                QMessageBox.critical(self, '警告', '数据库name错误', QMessageBox.Yes)
        else:
            QMessageBox.critical(self, '警告', '密码或账号错误', QMessageBox.Yes)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
