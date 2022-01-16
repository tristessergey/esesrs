from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,
                        QGroupBox, QVBoxLayout, QLabel, QMessageBox, QRadioButton)

app = QApplication([]) #создание приложения
my_win = QWidget() #создание главного окна
my_win.setWindowTitle('Конкурс')
my_win.resize(400, 200)

q = QGroupBox() #создание группы кнопок
text = QLabel('Здесь должен быть вопрос:')
btn1 = QRadioButton('Ответ 1')
btn2 = QRadioButton('Ответ 2')
btn3 = QRadioButton('Ответ 3')
btn4 = QRadioButton('Ответ 4')
push = QPushButton('Ответить')

layout1 = QHBoxLayout() #горизонтальная направляющая для qGroupBox
layout2 = QVBoxLayout() #вертикальная
layout3 = QVBoxLayout() #вертикальная
layout2.addWidget(btn1)
layout2.addWidget(btn2)
layout3.addWidget(btn3)
layout3.addWidget(btn4) #добавление виджетов на групбокс
layout1.addLayout(layout2) #добавление двух вертикальных на горизонтальную направляющую групбокса
layout1.addLayout(layout3)
q.setLayout(layout1) #установка внешнего вида групбокса
l1 = QHBoxLayout() #вопрос
l2 = QHBoxLayout() #групбокс
l3 = QHBoxLayout() #ответить кнопка
l1.addWidget(text) #добавление вопроса на основной экран
l2.addWidget(q) #добавление группы кнопок
l3.addWidget(push) #добавление самой кнопки "ответить"
l3.addStretch(3)
lv = QVBoxLayout() #основная направляющая для всего окна
lv.addLayout(l1, stretch= 2)
lv.addLayout(l2, stretch= 8)
lv.addLayout(l3, stretch= 1)
my_win.setLayout(lv) #установка внешнего вида окна


def show_question():
    #показывать панель вопросов и ответов
    q.show()
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)

    

my_win.show()
app.exec_()
