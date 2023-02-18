import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import snap7
from snap7.util import *

from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.turnonButton.clicked.connect(self.turnon_lamp)
        self.turnoffButton.clicked.connect(self.turnoff_lamp)
 

    def turnon_lamp(self):
        client = snap7.client.Client()
        client.connect("192.168.2.1", 0, 1)
        if client.get_connected():
            #读取M3字节，由于是bool量，所以最后一个参数是1
            data=client.read_area(Areas.MK, 0, 3, 1)
            #将data字节的第2位的值设置为1(True)
            set_bool(data,0,2,True)
            client.write_area(Areas.MK,0,3,data)
            self.Lamp.setStyleSheet("background-color: rgb(0,255,0);border-style:none;border:1px solid #3f3f3f; padding:5px;min-height:20px;border-radius:45px;")
            client.disconnect() 
    def turnoff_lamp(self):
        client = snap7.client.Client()
        client.connect("192.168.2.1", 0, 1)
        if client.get_connected():
            #读取M3字节，由于是bool量，所以最后一个参数是1
            data=client.read_area(Areas.MK, 0, 3, 1)
            #将data字节的第2位的值设置为0(False)
            set_bool(data,0,2,False)
            #将data写入M3.2，关灯
            client.write_area(Areas.MK,0,3,data)
            self.Lamp.setStyleSheet("background-color: grey;border-style:none;border:1px solid #3f3f3f; padding:5px;min-height:20px;border-radius:45px;")
            client.disconnect() 

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
"""
client = snap7.client.Client()
client.connect("192.168.2.1", 0, 1)         
if client.get_connected():
    print('connect is done')
    #读取M3最右边的一个字节
    data=client.read_area(Areas.MK, 0, 3, 1)
    #得到M3.2的值并转为bool值
    print(get_bool(data,0,2))
    #写入M3.2，开灯
    set_bool(data,0,2,True)
    client.write_area(Areas.MK,0,3,data)
    #写入M3.2，关灯
    set_bool(data,0,2,True)
    client.write_area(Areas.MK,0,3,data)
    client.disconnect()
"""
