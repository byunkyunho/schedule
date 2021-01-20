from PyQt5 import QtCore, QtGui, QtWidgets
import json
import webbrowser
import sys
import datetime

with open("schedule_data.json", "r", encoding='utf-8') as load_file:
    json_data = json.load(load_file)
    url_list = json_data['url']
    schedule_list = json_data['schedule']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setWindowTitle("schedule")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.fast_button = QtWidgets.QPushButton(self.centralwidget)
        self.fast_button.setGeometry(QtCore.QRect(10, 10, 110, 23))
        self.fast_button.clicked.connect(self.open_now_class)
        self.fast_button.setText("바로가기")

        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.clicked.connect((lambda: self.open_url(self.button_1.text())))

        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.clicked.connect((lambda: self.open_url(self.button_2.text())))

        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.clicked.connect((lambda: self.open_url(self.button_3.text())))

        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.clicked.connect((lambda: self.open_url(self.button_4.text())))

        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.clicked.connect((lambda: self.open_url(self.button_5.text())))

        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.clicked.connect((lambda: self.open_url(self.button_6.text())))

        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.clicked.connect((lambda: self.open_url(self.button_7.text())))

        self.class_1 = QtWidgets.QLabel(self.centralwidget)
        self.class_2 = QtWidgets.QLabel(self.centralwidget)
        self.class_3 = QtWidgets.QLabel(self.centralwidget)
        self.class_4 = QtWidgets.QLabel(self.centralwidget)
        self.class_5 = QtWidgets.QLabel(self.centralwidget)
        self.class_6 = QtWidgets.QLabel(self.centralwidget)
        self.class_7 = QtWidgets.QLabel(self.centralwidget)

        self.button_list = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7]
        self.class_list =  [self.class_1, self.class_2, self.class_3, self.class_4, self.class_5, self.class_6, self.class_7]
        class_time_list = [" 9:10 ~ 9:50","10:00 ~ 10:40","10:50 ~ 11:30", "11:40 ~ 12:20","13:00 ~ 13:40","13:50 ~ 14:30","14:40 ~ 15:20" ]

        for loop, (button, class_label, time) in enumerate(zip(self.button_list, self.class_list, class_time_list)):
            button.setGeometry(QtCore.QRect(125, 40+loop*30, 79, 23))
            class_label.setGeometry(QtCore.QRect(10, 40+loop*30, 120, 23))
            class_label.setText(f"{loop + 1}교시 {time}")
            
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(125, 10, 79, 22))
        self.comboBox.currentIndexChanged.connect(self.set_schedule)

        for week in ["월","화","수","목","금"]:
            self.comboBox.addItem(f"    {week}요일")

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_schedule()

    def open_now_class(self):
        now = datetime.datetime.now().strftime("%H %M")
        now_minute =  int(now.split(" ")[0])*60 + int(now.split(" ")[1])
        if now_minute > 540 and now_minute < 590:
            now_class = 1
        elif now_minute > 590 and now_minute < 640:
            now_class = 2
        elif now_minute > 640 and now_minute < 690:
            now_class = 3
        elif now_minute > 690 and now_minute < 740:
            now_class = 4
        elif now_minute > 770 and now_minute < 820:
            now_class = 5
        elif now_minute > 820 and now_minute < 870:
            now_class = 6
        elif now_minute > 870 and now_minute < 920 and len(schedule) == 7:
            now_class = 7
        else:
            now_class = 0
        if now_class != 0:
            webbrowser.open(url_list[schedule[now_class - 1]])

    def set_schedule(self):
        global schedule
        schedule = schedule_list[str(self.comboBox.currentIndex())]

        for button, subject in zip(self.button_list, schedule):
            button.setText(subject)

        if len(schedule) > 6:
            self.button_7.show()
            self.class_7.show()
            self.button_7.setText(schedule[6])
            MainWindow.setFixedSize(215, 257)
        else:
            self.button_7.hide()
            self.class_7.hide()
            MainWindow.setFixedSize(215, 225)


    def open_url(self, subject):
        webbrowser.open(url_list[subject])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
