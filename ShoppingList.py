#Shopping List
#Vilina Prenko
#13.11.2025

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    
    QLineEdit,
    QPushButton,
    QWidget,
    QListWidget,
    QAbstractItemView,
    QGridLayout,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout

    )




class ShoppingList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shopping List')
        self.enter_line = QLineEdit()
        self.list = QListWidget()
        self.button_add = QPushButton('+')
        self.button_remove = QPushButton('Remove')
        my_file = open('ShoppingList.txt')

        self.button_add.clicked.connect(self.add_item)
        self.enter_line.returnPressed.connect(self.add_item)
        self.button_remove.clicked.connect(self.remove_item)
        for item in my_file.readlines():
            self.list.addItem(item.strip())
        my_file.close()

        self.list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setStyleSheet("background-color: #FFDBE9;")
        self.list.setSortingEnabled(True)

        layout = QGridLayout()
        
        
        layout.addWidget(self.enter_line, 0, 0)
        layout.addWidget(self.button_add, 0, 1)
        layout.addWidget(self.list, 1, 0, 2, 2)
        layout.addWidget(self.button_remove, 3, 0, 1, 2)
        

        container_all_items = QWidget()
        container_all_items.setLayout(layout)
        

        self.setCentralWidget(container_all_items)

    def add_item(self):
        if len(self.enter_line.text()) != 0:
            self.list.addItem(self.enter_line.text())
            self.enter_line.clear()
            self.enter_line.setFocus()
    
    def remove_item(self):
        dialog = Dialog()
        if dialog.exec():
            list_of_items = self.list.selectedItems()
            for item in list_of_items:
                self.list.takeItem(self.list.row(item))

    def closeEvent(self, event):
        my_shopping_list = open('ShoppingList.txt', 'w')
        length = self.list.count()
        for row in range(length + 1):
            my_shopping_list.write(self.list.item(row).text() + '\n')
        my_shopping_list.close()

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #FFDBE9;")
        self.setWindowTitle('STOP!!!')

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel(f"Are you sure you want to delete? ({len(window.list.selectedItems())})" + ('Item' if len(window.list.selectedItems()) == 1 else 'Items'))
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication()
    window = ShoppingList()
    window.show()
    app.exec()