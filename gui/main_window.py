from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIS Scraper")
        self.layout = QVBoxLayout()
        self.button = QPushButton("בחר קובץ")
        self.label = QLabel("")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.show()

        self.button.clicked.connect(self.open_file)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "בחר קובץ",
            "",
            "ZIP Files (*.zip);;All Files (*)",  # סינון קבצים
        )
        if file_path:
            self.label.setText(file_path)


if __name__ == "__main__":
    MainWindow.run()
