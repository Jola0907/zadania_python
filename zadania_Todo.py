import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Zadanie(QListWidgetItem):
    def __init__(self, nazwa, data_dodania, deadline, wykonane = False):
        super().__init__() #konstruktor uruchamiany klasy nadrzednej
        self.nazwa = nazwa
        self.data_dodania= data_dodania
        self.deadline=deadline
        self.wykonane=wykonane

        self.update_text()
    def update_text(self):
        text=f"Task: {self.nazwa}, Dodane dnia: {self.data_dodania}, Deadline: {self.deadline}"#wstrzykiwanie danych do stringa, formatowanie stringa
        self.setText(text)

        if QDate.currentDate()>QDate.fromString(self.deadline, Qt.ISODate) and not self.wykonane:
            self.setBackground(QBrush(QColor("red")))
        else:
            self.setBackground(QBrush(QColor("white")))





class Todo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("TODO")
        self.opis_input=QLineEdit(self) #pole tekstowe połączone z aplikacją
        self.deadline_input=QDateEdit(QDate.currentDate(),self)
        self.dodaj_button=QPushButton("Dodaj zadanie", self)
        self.todo_list=QListWidget(self)
        self.ukryj_wykonane_checkbox=QCheckBox("Ukryj wykonane", self)
        self.metoda_sortowania=QComboBox(self)
        self.metoda_sortowania.addItems(["Sortuj rosnąco", "Sortuj malejąco"])

        layout=QVBoxLayout()
        layout.addWidget(self.opis_input)
        layout.addWidget(self.deadline_input)
        layout.addWidget(self.dodaj_button)
        layout.addWidget(self.ukryj_wykonane_checkbox)
        layout.addWidget(self.metoda_sortowania)
        layout.addWidget(self.todo_list)

        self.dodaj_button.clicked.connect(self.dodaj_zadanie)
        self.ukryj_wykonane_checkbox.toggled.connect(self.ukryj_wykonane)
        self.metoda_sortowania.currentIndexChanged.connect(self.sortuj)

        self.main_widget = QWidget()
        self.main_widget.setLayout(layout)
        self.setCentralWidget(self.main_widget)

    def dodaj_zadanie(self):
        nazwa_zadania=self.opis_input.text()
        deadline=self.deadline_input.date().toString(Qt.ISODate)
        data_dodania=QDate.currentDate().toString(Qt.ISODate)

        zadanie=Zadanie(nazwa_zadania, data_dodania, deadline)
        self.todo_list.addItem(zadanie)
        self.opis_input.clear()
        self.deadline_input.setDate(QDate.currentDate())


        self.sortuj()


    def ukryj_wykonane(self):
        for i in range(self.todo_list.count()):
            item = self.todo_list.item(i)
            if isinstance(item, Zadanie) and item.wykonane:
                item.setHidden(self.ukryj_wykonane_checkbox.isChecked())


    def sortuj(self):
        if self.metoda_sortowania.currentText()=="Sortuj rosnąco":
            self.todo_list.sortItems(Qt.AscendingOrder) #sortowanie rosnące
        else:
            self.todo_list.sortItems(Qt.DescendingOrder) #malejąco

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo = Todo()
    todo.show()
    sys.exit(app.exec_())