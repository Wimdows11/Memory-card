from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton,QPushButton ,QLabel, QSpinBox

app = QApplication([])
btn_menu = QPushButton("Меню")
btn_slepp = QPushButton("Відпочити")
box_time = QSpinBox()
box_time.setValue(30)
btn_ok = QPushButton("Відповісти")
question = QLabel("###")

#Варіанти відповід
RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()
rdbt_1= QRadioButton("answer1")
rdbt_2 = QRadioButton("answer2")
rdbt_3 = QRadioButton("answer3")
rdbt_4 = QRadioButton("answer4")

RadioGroup.addButton(rdbt_1)
RadioGroup.addButton(rdbt_2)
RadioGroup.addButton(rdbt_3)
RadioGroup.addButton(rdbt_4)

#Панель результатів
answerGrouBox = QGroupBox("Результат тесту")
lb_result = QLabel("###")
lb_true_ans = QLabel("###")

#Розміщення
ans1_layout = QHBoxLayout()
ans2_layout = QHBoxLayout()
ans3_layout = QHBoxLayout()

ans2_layout.addWidget(rdbt_1)
ans2_layout.addWidget(rdbt_2)

ans3_layout.addWidget(rdbt_3)
ans3_layout.addWidget(rdbt_4)

ans1_layout.addLayout(ans2_layout)
ans1_layout.addLayout(ans3_layout)