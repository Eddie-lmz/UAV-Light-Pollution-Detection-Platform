from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
import sys
import threading
import time


class ToolsUi(QDialog):
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_write_msg = QtCore.pyqtSignal(str)

    def __init__(self, num):
        """
        初始化窗口
        :param num: 计数窗口
        """
        self.new_data = []
        self.light_data = 0
        super(ToolsUi, self).__init__()
        self.num = num
        self._translate = QtCore.QCoreApplication.translate
        self.charView = QChartView(self)  # 定义charView，父窗体类型为 Window

        self.threadCtl = threading.Thread(target=self.linechart_plot_thread)
        self.threadCtl.start()
        # 定时更新折线图
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(400)

        self.init_line()
        self.add_axis()

        self.setObjectName("TCP-UDP")
        self.resize(980, 700)
        self.setAcceptDrops(False)
        self.setSizeGripEnabled(False)

        # 定义控件
        self.pushButton_get_ip = QtWidgets.QPushButton()
        self.pushButton_get_ip.setObjectName("pushButton_get_ip")
        self.pushButton_get_ip.setStyleSheet("#pushButton_get_ip{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:4px;\n"
                                           "}\n"
                                           "#pushButton_get_ip:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_get_ip:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_get_ip.setFont(font)
        self.pushButton_link = QtWidgets.QPushButton()
        self.pushButton_link.setObjectName("pushButton_link")
        self.pushButton_link.setStyleSheet("#pushButton_link{\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    border:3px solid rgb(182, 182, 182);\n"
                                       "    border-radius:8px;\n"
                                       "}\n"
                                       "#pushButton_link:hover{\n"
                                       "    background-color: rgb(249, 248, 222);\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "}\n"
                                       "#pushButton_link:pressed{\n"
                                       "    padding-top:5px;\n"
                                       "    padding-left:5px;\n"
                                       "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_link.setFont(font)
        self.pushButton_unlink = QtWidgets.QPushButton()
        self.pushButton_unlink.setObjectName("pushButton_unlink")
        self.pushButton_unlink.setStyleSheet("#pushButton_unlink{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:8px;\n"
                                           "}\n"
                                           "#pushButton_unlink:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_unlink:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_unlink.setFont(font)
        self.pushButton_clear = QtWidgets.QPushButton()
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_clear.setStyleSheet("#pushButton_clear{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:8px;\n"
                                           "}\n"
                                           "#pushButton_clear:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_clear:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_clear.setFont(font)
        self.pushButton_exit = QtWidgets.QPushButton()
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet("#pushButton_exit{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:8px;\n"
                                           "}\n"
                                           "#pushButton_exit:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_exit:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_exit.setFont(font)
        self.pushButton_send = QtWidgets.QPushButton()
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_send.setStyleSheet("#pushButton_send{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:8px;\n"
                                           "}\n"
                                           "#pushButton_send:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_send:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_send.setFont(font)
        self.pushButton_dir = QtWidgets.QPushButton()
        self.pushButton_dir.setObjectName("pushButton_dir")
        self.pushButton_dir.setStyleSheet("#pushButton_dir{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:8px;\n"
                                           "}\n"
                                           "#pushButton_dir:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_dir:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_dir.setFont(font)
        self.pushButton_else = QtWidgets.QPushButton()
        self.pushButton_else.setObjectName("pushButton_else")
        self.pushButton_else.setStyleSheet("#pushButton_else{\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "    border:3px solid rgb(182, 182, 182);\n"
                                             "    border-radius:4px;\n"
                                             "}\n"
                                             "#pushButton_else:hover{\n"
                                             "    background-color: rgb(249, 248, 222);\n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}\n"
                                             "#pushButton_else:pressed{\n"
                                             "    padding-top:5px;\n"
                                             "    padding-left:5px;\n"
                                             "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_else.setFont(font)
        self.pushButton_datasave = QtWidgets.QPushButton()
        self.pushButton_datasave.setObjectName("pushButton_else")
        self.pushButton_datasave.setStyleSheet("#pushButton_else{\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border:3px solid rgb(182, 182, 182);\n"
                                           "    border-radius:4px;\n"
                                           "}\n"
                                           "#pushButton_else:hover{\n"
                                           "    background-color: rgb(249, 248, 222);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "#pushButton_else:pressed{\n"
                                           "    padding-top:5px;\n"
                                           "    padding-left:5px;\n"
                                           "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_datasave.setFont(font)

        self.pushButton_dataimport = QtWidgets.QPushButton()
        self.pushButton_dataimport.setObjectName("pushButton_else")
        self.pushButton_dataimport.setStyleSheet("#pushButton_else{\n"
                                               "    background-color: rgb(255, 255, 255);\n"
                                               "    color: rgb(0, 0, 0);\n"
                                               "    border:3px solid rgb(182, 182, 182);\n"
                                               "    border-radius:4px;\n"
                                               "}\n"
                                               "#pushButton_else:hover{\n"
                                               "    background-color: rgb(249, 248, 222);\n"
                                               "    color: rgb(0, 0, 0);\n"
                                               "}\n"
                                               "#pushButton_else:pressed{\n"
                                               "    padding-top:5px;\n"
                                               "    padding-left:5px;\n"
                                               "}")
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        self.pushButton_dataimport.setFont(font)

        self.label_port = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_port.setFont(font)
        self.label_ip = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_ip.setFont(font)
        self.label_rev = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 B")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_rev.setFont(font)
        self.label_send = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 B")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_send.setFont(font)
        self.label_sendto = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_sendto.setFont(font)
        self.label_dir = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_dir.setFont(font)
        self.label_written = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_written.setFont(font)
        self.lineEdit_port = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(9)
        self.lineEdit_port.setFont(font)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.lineEdit_port.setStyleSheet("#lineEdit_port{\n"
                                  "border: 2px solid gray;\n"
                                  "border-radius:9px;\n"
                                  "}")
        self.lineEdit_ip_send = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(9)
        self.lineEdit_ip_send.setFont(font)
        self.lineEdit_ip_send.setObjectName("lineEdit_ip_send")
        self.lineEdit_ip_send.setStyleSheet("#lineEdit_ip_send{\n"
                                  "border: 2px solid gray;\n"
                                  "border-radius:9px;\n"
                                  "}")
        self.lineEdit_ip_local = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(9)
        self.lineEdit_ip_local.setFont(font)
        self.lineEdit_ip_local.setObjectName("lineEdit_ip_local")
        self.lineEdit_ip_local.setStyleSheet("#lineEdit_ip_local{\n"
                                  "border: 2px solid gray;\n"
                                  "border-radius:9px;\n"
                                  "}")
        self.textEdit_send = QtWidgets.QTextEdit()
        self.textEdit_send.lower()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(11)
        self.textEdit_send.setFont(font)
        self.textBrowser_recv = QtWidgets.QTextBrowser()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        self.textBrowser_recv.setFont(font)
        self.comboBox_tcp = QtWidgets.QComboBox()
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(9)
        self.comboBox_tcp.setFont(font)
        self.comboBox_tcp.setObjectName("comboBox_tcp")
        self.comboBox_tcp.setStyleSheet("#comboBox_tcp{\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius:4px;\n"
                                    "padding:1px 2px 1px 2px;\n"
                                    "min-width :  5em;\n"
                                    "}\n"
                                    "#comboBox_tcp:down-arrow{\n"
                                    "    image: url(picture/icondown.jpg);\n"
                                    "}\n"
                                    "#comboBox_tcp:drop-down{\n"
                                    "    width: 25px;\n"
                                    "}")
        self.UAV_label = QtWidgets.QLabel(self)
        self.UAV_label.raise_()
        self.UAV_label.setGeometry(QtCore.QRect(130, 142, 60, 48))
        self.UAV_label.setStyleSheet("image: url(picture/UAV.jpg);")
        self.UAV_label.setText("")
        self.UAV_label.setObjectName("UAV_label")

        # 定义布局
        self.h_box_1 = QHBoxLayout()
        self.h_box_2 = QHBoxLayout()
        self.h_box_3 = QHBoxLayout()
        self.h_box_4 = QHBoxLayout()
        self.h_box_recv = QHBoxLayout()
        self.h_box_save = QHBoxLayout()
        self.h_box_exit = QHBoxLayout()
        self.h_box_all = QHBoxLayout()
        self.v_box_set = QVBoxLayout()
        self.v_box_send = QVBoxLayout()
        self.v_box_web = QVBoxLayout()
        self.v_box_exit = QVBoxLayout()
        self.v_box_right = QVBoxLayout()
        self.v_box_left = QVBoxLayout()
        self.v_box_right2right = QVBoxLayout()

        # 向选择功能的下拉菜单添加选项
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")
        self.comboBox_tcp.addItem("")


        # 设置字体

        # 设置控件的初始属性
        self.label_dir.hide()
        self.label_sendto.hide()
        self.pushButton_dir.hide()
        self.lineEdit_ip_send.hide()
        self.label_dir.setWordWrap(True)  # 让label自动换行
        self.pushButton_unlink.setEnabled(False)
        self.textBrowser_recv.insertPlainText("这是窗口-%s\n" % self.num)

        # 调用布局方法和控件显示文字的方法
        self.layout_ui()
        self.ui_translate()
        self.connect()




    def layout_ui(self):
        """
        设置控件的布局
        :return:
        """
        # 左侧布局添加
        self.h_box_1.addWidget(self.label_ip)
        self.h_box_1.addWidget(self.lineEdit_ip_local)
        self.h_box_1.addWidget(self.pushButton_get_ip)
        self.h_box_2.addWidget(self.label_port)
        self.h_box_2.addWidget(self.lineEdit_port)
        self.h_box_2.addWidget(self.pushButton_else)
        self.h_box_3.addWidget(self.label_sendto)
        self.h_box_3.addWidget(self.lineEdit_ip_send)
        self.h_box_4.addWidget(self.comboBox_tcp)
        self.h_box_4.addWidget(self.pushButton_link)
        self.h_box_4.addWidget(self.pushButton_unlink)
        self.v_box_set.addLayout(self.h_box_1)
        self.v_box_set.addLayout(self.h_box_2)
        self.v_box_set.addLayout(self.h_box_3)
        self.v_box_set.addLayout(self.h_box_4)
        self.v_box_web.addWidget(self.label_dir)
        self.v_box_web.addWidget(self.pushButton_dir)
        self.v_box_send.addWidget(self.label_send)
        self.v_box_send.addWidget(self.textEdit_send)
        self.v_box_send.addLayout(self.v_box_web)
        self.v_box_exit.addWidget(self.pushButton_send)
        self.v_box_exit.addWidget(self.pushButton_exit)
        self.h_box_exit.addWidget(self.label_written)
        self.h_box_exit.addLayout(self.v_box_exit)
        self.v_box_left.addLayout(self.v_box_set)
        self.v_box_left.addLayout(self.v_box_send)
        self.v_box_left.addLayout(self.h_box_exit)

        # 右侧布局添加
        self.h_box_recv.addWidget(self.label_rev)
        self.h_box_recv.addWidget(self.pushButton_clear)
        self.h_box_save.addWidget(self.pushButton_datasave)
        self.h_box_save.addWidget(self.pushButton_dataimport)
        self.v_box_right.addLayout(self.h_box_recv)
        self.v_box_right.addWidget(self.textBrowser_recv)
        self.v_box_right.addLayout(self.h_box_save)
        self.v_box_right2right.addWidget(self.charView)


        # 将左右布局添加到窗体布局
        self.h_box_all.addLayout(self.v_box_left)
        self.h_box_all.addLayout(self.v_box_right)
        self.h_box_all.addLayout(self.v_box_right2right)

        # 设置窗体布局到窗体
        self.setLayout(self.h_box_all)

    def ui_translate(self):
        """
        控件默认显示文字的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # 设置各个控件显示的文字
        # 也可使用控件的setText()方法设置文字
        self.setWindowTitle(self._translate("TCP-UDP", "光污染检测UAV网络测试助手-窗口%s" % self.num))
        self.comboBox_tcp.setItemText(0, self._translate("TCP-UDP", "TCP服务端"))
        self.comboBox_tcp.setItemText(1, self._translate("TCP-UDP", "TCP客户端"))
        self.comboBox_tcp.setItemText(2, self._translate("TCP-UDP", "UDP服务端"))
        self.comboBox_tcp.setItemText(3, self._translate("TCP-UDP", "UDP客户端"))
        self.comboBox_tcp.setItemText(4, self._translate("TCP-UDP", "WEB服务端"))
        self.pushButton_link.setText(self._translate("TCP-UDP", "连接网络"))
        self.pushButton_unlink.setText(self._translate("TCP-UDP", "断开网络"))
        self.pushButton_get_ip.setText(self._translate("TCP-UDP", "重新获取IP"))
        self.pushButton_clear.setText(self._translate("TCP-UDP", "清除消息"))
        self.pushButton_send.setText(self._translate("TCP-UDP", "发送"))
        self.pushButton_exit.setText(self._translate("TCP-UDP", "退出系统"))
        self.pushButton_dir.setText(self._translate("TCP-UDP", "选择路径"))
        self.pushButton_datasave.setText(self._translate("TCP-UDP", "数据保存"))
        self.pushButton_dataimport.setText(self._translate("TCP-UDP", "数据导入"))
        self.pushButton_else.setText(self._translate("TCP-UDP", "窗口多开another"))
        self.label_ip.setText(self._translate("TCP-UDP", "本机IP:"))
        self.label_port.setText(self._translate("TCP-UDP", "端口号:"))
        self.label_sendto.setText(self._translate("TCP-UDP", "目标IP:"))
        self.label_rev.setText(self._translate("TCP-UDP", "接收区域"))
        self.label_send.setText(self._translate("TCP-UDP", "发送区域"))
        self.label_dir.setText(self._translate("TCP-UDP", "请选择index.html所在的文件夹"))
        self.label_written.setText(self._translate("TCP-UDP", "Written by lmz for NCSAP"))

    def connect(self):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        self.signal_write_msg.connect(self.write_msg)
        self.comboBox_tcp.currentIndexChanged.connect(self.combobox_change)

    def combobox_change(self):
        # 此函数用于选择不同功能时界面会作出相应变化
        """
        combobox控件内容改变时触发的槽
        :return: None
        """
        self.close_all()
        if self.comboBox_tcp.currentIndex() == 0 or self.comboBox_tcp.currentIndex() == 2:
            self.label_sendto.hide()
            self.label_dir.hide()
            self.pushButton_dir.hide()
            self.pushButton_send.show()
            self.lineEdit_ip_send.hide()
            self.textEdit_send.show()
            self.label_port.setText(self._translate("TCP-UDP", "端口号:"))

        if self.comboBox_tcp.currentIndex() == 1 or self.comboBox_tcp.currentIndex() == 3:
            self.label_sendto.show()
            self.label_dir.hide()
            self.pushButton_dir.hide()
            self.pushButton_send.show()
            self.lineEdit_ip_send.show()
            self.textEdit_send.show()
            self.label_port.setText(self._translate("TCP-UDP", "目标端口:"))

        if self.comboBox_tcp.currentIndex() == 4:
            self.label_sendto.hide()
            self.label_dir.show()
            self.pushButton_dir.show()
            self.pushButton_send.hide()
            self.lineEdit_ip_send.hide()
            self.textEdit_send.hide()
            self.label_port.setText(self._translate("TCP-UDP", "端口号:"))

    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.textBrowser_recv.insertPlainText(msg)
        # 滚动条移动到结尾
        self.textBrowser_recv.moveCursor(QtGui.QTextCursor.End)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        self.close_all()

    def close_all(self):
        pass

    def init_line(self):
        # 实例折线对象
        self.series_1 = QLineSeries()  # 定义LineSerise，将类QLineSeries实例化
        # 折线初始数据了列表
        self._1_point_list = []
        for i in range(20):
            y = 0
            self._1_point_list.append(QPointF(i, y))

        self.series_1.append(self._1_point_list)  # 折线添加坐标点清单
        self.series_1.setName("光照强度")

    def add_axis(self):
        # 设置x轴
        self.x_Aix = QValueAxis()
        self.x_Aix.setRange(0.00, 10.00)
        self.x_Aix.setTitleText("T(t)")
        self.x_Aix.setLabelFormat("%0.2f")
        self.x_Aix.setTickCount(21)  # 将0-10分成11份
        self.x_Aix.setMinorTickCount(2)  # 设置每一份的分割数

        # 设置y轴
        self.y_Aix = QValueAxis()
        self.y_Aix.setTitleText("light(lux)")
        self.y_Aix.setRange(0.00, 200.00)
        self.y_Aix.setLabelFormat("%0.2f")
        self.y_Aix.setTickCount(11)
        self.y_Aix.setMinorTickCount(4)

        self.charView.chart().addSeries(self.series_1)  # 添加折线实例

        # 添加轴，Qt.AlignBottom表示底部，Qt.AlignLeft表示左边，Qt.AlignRight表示右边
        self.charView.chart().addAxis(self.x_Aix, Qt.AlignBottom)
        self.charView.chart().addAxis(self.y_Aix, Qt.AlignLeft)

        # 将折线与对应的y轴关联，这里只写了一个y轴，如果有多条折线可以关联不同的y轴
        self.series_1.attachAxis(self.y_Aix)

        # 隐藏或者显示折线 setVisible
        # self.series_1.setVisible(False)  # 隐藏折线

    def update(self):
        # 更新折线上的点的坐标
        if len(self.new_data) > 0:
            self.value = self.new_data[0]
            self.new_data.pop(0)
            del self._1_point_list[len(self._1_point_list) - 1]
            self._1_point_list.insert(0, QPointF(0, self.value))
            for i in range(0, len(self._1_point_list)):
                self._1_point_list[i].setX(i)
            self.series_1.replace(self._1_point_list)

    def linechart_plot_thread(self):
        while True:
            try:
                data = self.light_data
                if data != 0:
                    self.new_data.append(data)
            except:
                pass
            time.sleep(0.4)




if __name__ == '__main__':
    """
    显示界面
    """
    app = QApplication(sys.argv)
    ui = ToolsUi(1)
    ui.show()
    sys.exit(app.exec_())
