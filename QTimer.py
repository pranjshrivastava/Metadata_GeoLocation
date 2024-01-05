from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel

def delayed_function():
    label.setText("Delayed function executed")

app = QApplication([])

# Create a QLabel
label = QLabel("Initial text")
label.show()

# Set up a single-shot timer to execute the delayed_function after 2000 milliseconds (2 seconds)
timer = QTimer.singleShot(2000, delayed_function)

app.exec_()
