#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel, QMessageBox, QRadioButton


class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.question = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []

question1 = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Алеуты', 'Чулымцы')
questions_list.append(question1)
question2 = Question('В каком году распался СССР?', '1991', '1990', '1989', '1992')
questions_list.append(question2)
question3 = Question('Купи слона', 'Да', 'Нет', 'Потом', 'Не хочу')
questions_list.append(question3)


app = QApplication([])
mainwin = QWidget()
mainwin.setWindowTitle('Memory Card')
mainwin.resize(500, 300)

mainwin.score = 0
mainwin.total = 0

question = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')

btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Чулымцы')
btn3 = QRadioButton('Смурфы')
btn4 = QRadioButton('Алеуты')

answers = [btn1, btn2, btn3, btn4]

radioGroupBox = QGroupBox('Варианты ответов')
formGroup = QGroupBox('Результат теста')
label = QLabel('Правильно/Неправильно')
result = QLabel('Правильный ответ')
formGroup.hide()

main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()

h1_layout.addWidget(question, alignment = Qt.AlignCenter)
h2_layout.addWidget(radioGroupBox)
h2_layout.addWidget(formGroup)
h3_layout.addWidget(btn_OK, stretch = 2)


main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h3_layout)

qv_layout = QVBoxLayout()
qh1_layout = QHBoxLayout()
qh2_layout = QHBoxLayout()

rh1_layout = QHBoxLayout()
rh2_layout = QHBoxLayout()
rv_layout = QVBoxLayout()
rv_layout.addLayout(rh1_layout)
rv_layout.addLayout(rh2_layout)

rh1_layout.addWidget(label)
rh2_layout.addWidget(result, alignment = Qt.AlignCenter)

qh1_layout.addWidget(btn1)
qh1_layout.addWidget(btn2)
qh2_layout.addWidget(btn3)
qh2_layout.addWidget(btn4)

qv_layout.addLayout(qh1_layout)
qv_layout.addLayout(qh2_layout)
formGroup.setLayout(rv_layout)

radioGroupBox.setLayout(qv_layout)

button_group = QButtonGroup()
button_group.addButton(btn1)
button_group.addButton(btn2)
button_group.addButton(btn3)
button_group.addButton(btn4)

mainwin.setLayout(main_layout)

def print_stat():
    print('Текущая статистика:', mainwin.score)

def show_result(res):
    result.setText(res)
    formGroup.show()
    radioGroupBox.hide()
    btn_OK.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    button_group.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    button_group.setExclusive(True)
    radioGroupBox.show()
    formGroup.hide()   
    btn_OK.setText('Ответить')

def ask(q):
    question.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def check_ans():
    if answers[0].isChecked() == True:
        show_result('Правильно!')
        mainwin.score += 1
        print_stat()
    else:
        show_result('Неправильно')
    print('Рейтинг:', mainwin.score/mainwin.total*100)

def next_question():
    mainwin.total += 1
    print_stat()
    rand = randint(0, len(questions_list)-1)
    q = questions_list[rand]
    ask(q)

def start_test():
    if btn_OK.text() == 'Ответить':
        check_ans()
    elif btn_OK.text() == 'Следующий вопрос':
        next_question()

btn_OK.clicked.connect(start_test)

next_question()

mainwin.show()
app.exec_()



