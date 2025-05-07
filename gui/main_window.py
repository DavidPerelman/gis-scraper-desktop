from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIS Scraper")
        layout = QVBoxLayout()
        button = QPushButton("בחר קובץ")
        label = QLabel("")

        layout.addWidget(button)
        layout.addWidget(label)

        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    MainWindow.run()
