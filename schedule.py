from PyQt5 import QtCore, QtGui, QtWidgets
import json
import webbrowser
import sys
import datetime

with open("data.json", "r", encoding='utf-8') as load_file:
    data = json.load(load_file)
    url_data = data['url']
    schedule_data = data['schedule']
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(215, 257)
        
        MainWindow.setWindowTitle("schedule")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.fast_button = QtWidgets.QPushButton(self.centralwidget)
        self.fast_button.setGeometry(QtCore.QRect(10, 10, 110, 23))
        self.fast_button.clicked.connect(self.open_now_class)
        self.fast_button.setText("바로가기")

        self.button_list = [QtWidgets.QPushButton(self.centralwidget) for _ in range(7)]
        self.button_list[0].clicked.connect((lambda: self.open_url(self.button_list[0].text())))
        self.button_list[1].clicked.connect((lambda: self.open_url(self.button_list[1].text())))
        self.button_list[2].clicked.connect((lambda: self.open_url(self.button_list[2].text())))
        self.button_list[3].clicked.connect((lambda: self.open_url(self.button_list[3].text())))
        self.button_list[4].clicked.connect((lambda: self.open_url(self.button_list[4].text())))
        self.button_list[5].clicked.connect((lambda: self.open_url(self.button_list[5].text())))
        self.button_list[6].clicked.connect((lambda: self.open_url(self.button_list[6].text())))

        self.class_list = [QtWidgets.QLabel(self.centralwidget) for _ in range(7)]

        class_time_list = [" 9:10 ~ 9:50","10:00 ~ 10:40","10:50 ~ 11:30", "11:40 ~ 12:20","13:10 ~ 13:50","14:00 ~ 14:40","14:50 ~ 15:30" ]

        for loop, (button, class_label, time) in enumerate(zip(self.button_list, self.class_list, class_time_list)):
            button.setGeometry(QtCore.QRect(125, 40+loop*30, 79, 23))
            class_label.setGeometry(QtCore.QRect(10, 40+loop*30, 120, 23))
            class_label.setText(f"{loop + 1}교시 {time}")
            
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(125, 10, 79, 22))
        self.comboBox.currentIndexChanged.connect(self.set_schedule)
        self.all_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.all_combobox.addItems(url_data.keys())
        self.all_combobox.currentTextChanged.connect(lambda : self.open_url(self.all_combobox.currentText()))

        for week in ["월","화","수","목","금"]:
            self.comboBox.addItem(f"{week}요일")

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_schedule()

    def open_now_class(self):
        now = datetime.datetime.now().strftime("%H %M")
        now_minute =  int(now.split(" ")[0])*60 + int(now.split(" ")[1])
        now_class = ((now_minute-540 )// 50)
        if now_class > 0 and now_class < 7: 
            if now_class > 5:
                if len(schedule) > 6:
                    webbrowser.open(url_data[schedule[now_class]])     
            else:
                webbrowser.open(url_data[schedule[now_class]])

    def set_schedule(self):
        schedule = schedule_data[self.comboBox.currentIndex()]

        for button, subject in zip(self.button_list, schedule):
            button.setText(subject)

        if len(schedule) > 6:
            MainWindow.setFixedSize(215, 287)
            self.button_list[6].show()
            self.class_list[6].show()
            self.button_list[6].setText(schedule[6])
            self.all_combobox.setGeometry(QtCore.QRect(10,250,193,23))
        else:
            MainWindow.setFixedSize(215, 255)
            self.button_list[6].hide()
            self.class_list[6].hide()
            self.all_combobox.setGeometry(QtCore.QRect(10,220,193,23))

    def open_url(self, subject):
        if subject in url_data:
            webbrowser.open(url_data[subject])

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
