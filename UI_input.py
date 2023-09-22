import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog

class FileSelectionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Folder and File Selection')
        self.setGeometry(100, 100, 400, 150)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.folder_label = QLabel('Selected Folder:')
        layout.addWidget(self.folder_label)

        self.file_label = QLabel('Selected File:')
        layout.addWidget(self.file_label)

        self.select_folder_button = QPushButton('Select Folder')
        self.select_folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_folder_button)

        self.select_file_button = QPushButton('Select File')
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)

        central_widget.setLayout(layout)

    def select_folder(self):
        folder_dialog = QFileDialog()
        folder = folder_dialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.folder_label.setText(f'Selected Folder: {folder}')

    def select_file(self):
        file_dialog = QFileDialog()
        file, _ = file_dialog.getOpenFileName(self, 'Select File')
        if file:
            self.file_label.setText(f'Selected File: {file}')

def main():
    app = QApplication(sys.argv)
    window = FileSelectionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
