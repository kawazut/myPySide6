import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def create_main_window() -> QMainWindow:
    window = QMainWindow()
    window.setWindowTitle("My PySide6 App")

    message = QLabel("PySide6 GUI アプリへようこそ")
    button = QPushButton("クリック")
    button.clicked.connect(lambda: message.setText("ボタンがクリックされました"))

    layout = QVBoxLayout()
    layout.addWidget(message)
    layout.addWidget(button)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    return window


def main() -> int:
    app = QApplication(sys.argv)
    window = create_main_window()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
