import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

# Hardcoded username and password for authentication
USERNAME = "JohnDoe"
PASSWORD = "tbc2024"


class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        loadUi("main.ui", self)
        self.loginButton.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        # Check if the input values are the same as hardcoded ones
        if username == USERNAME and password == PASSWORD:
            QMessageBox.information(self, "Success", "Login Successful!")
            self.accept()
        else:
            # If not authenticated, show error message
            QMessageBox.warning(self, "Error Occurred", "Invalid username or password")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    login_dialog.show()
    sys.exit(app.exec_())
