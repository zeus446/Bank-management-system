import sys
import csv
import random
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QMessageBox,
    QInputDialog, QGridLayout, QLineEdit
)

file_path = 'user_data.csv'


class BankingSystemGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #121212;")
        self.username = ""
        self.passwd = ""
        self.accountno = None
        self.apple = False  # used to ensure dashboard opens once per login
        self.login_create()

    def login_create(self):
        """Initial login/create screen"""
        self.resize(500, 500)
        self.setWindowTitle("Login portal")

        self.buttonl = QPushButton("Login")
        self.buttonc = QPushButton("Create")

        for btn in (self.buttonl, self.buttonc):
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #03DAC6;
                    color: #000000;
                    font: bold 14px;
                    border: 2px solid #03DAC6;
                    border-radius: 15px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #018786;
                }
                """
            )

        box = QGridLayout()
        box.addWidget(self.buttonl, 0, 0)
        box.addWidget(self.buttonc, 0, 1)

        central_widget = QWidget(self)
        central_widget.setLayout(box)
        self.setCentralWidget(central_widget)

        self.buttonl.clicked.connect(self.login)
        self.buttonc.clicked.connect(self.create_account)

    def create_account(self):
        """UI for creating a new account (enter name + password + register)"""
        self.resize(500, 500)
        self.setWindowTitle("Create account")

        self.buttona = QPushButton("Enter Name")
        self.buttona.clicked.connect(self.get_name)

        self.buttonb = QPushButton("Enter Password")
        self.buttonb.clicked.connect(self.get_passwd)

        self.buttoncheck = QPushButton("Register")
        self.buttoncheck.clicked.connect(self.registration)

        for btn in (self.buttona, self.buttonb, self.buttoncheck):
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #03DAC6;
                    color: #000000;
                    font: bold 14px;
                    border: 2px solid #03DAC6;
                    border-radius: 15px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #018786;
                }
                """
            )

        box = QGridLayout()
        box.addWidget(self.buttona, 0, 0)
        box.addWidget(self.buttonb, 1, 0)
        box.addWidget(self.buttoncheck, 2, 0)

        central_widget = QWidget(self)
        central_widget.setLayout(box)
        self.setCentralWidget(central_widget)

    def get_name(self):
        name, ok = QInputDialog.getText(self, "Name Submission", "Enter your name:")
        if ok and name:
            self.show_message("Name Submission", "Successfully submitted name")
            self.username = name

    def get_passwd(self):
        # Use password echo mode
        passwd1, ok1 = QInputDialog.getText(
            self, "Password Submission", "Enter a Password:", QLineEdit.EchoMode.Password
        )
        if not ok1:
            return
        passwd2, ok2 = QInputDialog.getText(
            self, "Resubmission", "Enter password again to confirm:", QLineEdit.EchoMode.Password
        )
        if ok2 and passwd1 == passwd2:
            self.show_message("Password Submission", "Successfully submitted Password")
            self.passwd = passwd1
        else:
            self.show_message("Password Submission", "Passwords did not match. Try again.")
            self.passwd = ""

    def registration(self):
        """Write new account to CSV; initial balance 3000 and zeros elsewhere"""
        if not self.username or not self.passwd:
            self.show_message("Registration error", "Please enter name and password before registering.")
            return

        self.accountno = self.getaccno()

        file_exists = os.path.exists(file_path)
        write_header = not file_exists or os.path.getsize(file_path) == 0

        with open(file_path, mode='a', newline='') as file:
            fieldnames = ['Name', 'Account number', 'Password', 'Account Balance', 'Credit Score', 'Credit Points', 'Investment']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerow({
                "Name": self.username,
                "Account number": self.accountno,
                "Password": self.passwd,
                "Account Balance": "3000",
                "Credit Score": "0",
                "Credit Points": "0",
                "Investment": "0"
            })

        self.show_message("Registration complete", "Account added")
        # reset apple so dashboard can open on next login
        self.apple = False
        self.login_create()

    def getaccno(self):
        return random.randint(10000, 99999)

    def login(self):
        """UI to prompt username and password and then check"""
        self.resize(500, 500)
        self.setWindowTitle("Login")

        self.buttona = QPushButton("Enter username")
        self.buttona.clicked.connect(self.get_name)

        self.buttonb = QPushButton("Enter Password")
        self.buttonb.clicked.connect(self.get_passwd)

        self.buttoncheck = QPushButton("Log in")
        self.buttoncheck.clicked.connect(self.check)

        for btn in (self.buttona, self.buttonb, self.buttoncheck):
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #03DAC6;
                    color: #000000;
                    font: bold 14px;
                    border: 2px solid #03DAC6;
                    border-radius: 15px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #018786;
                }
                """
            )

        box = QGridLayout()
        box.addWidget(self.buttona, 0, 0)
        box.addWidget(self.buttonb, 1, 0)
        box.addWidget(self.buttoncheck, 2, 0)

        central_widget = QWidget(self)
        central_widget.setLayout(box)
        self.setCentralWidget(central_widget)

    def setup_dashboard(self, actm):
        """Dashboard UI: actm is a CSV row list"""
        self.resize(600, 400)
        self.setWindowTitle("Dashboard")

        # Create buttons
        self.button1 = QPushButton("Deposit")
        self.button1.clicked.connect(self.deposit)

        self.button2 = QPushButton("Withdraw")
        self.button2.clicked.connect(self.withdraw)

        self.button3 = QPushButton("Check balance")
        self.button3.clicked.connect(self.check_balance)

        self.button4 = QPushButton("Logout")
        self.button4.clicked.connect(self.logout)

        self.button5 = QPushButton("Invest")
        self.button5.clicked.connect(self.invest)

        self.button6 = QPushButton("Check Credit Points")
        self.button6.clicked.connect(self.update_credit)

        self.button7 = QPushButton("Check Credit Score")
        self.button7.clicked.connect(self.update_credit_score)

        # Layout and placement
        box = QGridLayout()
        box.addWidget(self.button1, 0, 0)
        box.addWidget(self.button2, 1, 0)
        box.addWidget(self.button3, 2, 0)
        box.addWidget(self.button4, 3, 0)
        box.addWidget(self.button5, 0, 1)
        box.addWidget(self.button6, 1, 1)
        box.addWidget(self.button7, 2, 1)

        # Labels from CSV row (actm)
        # Expected actm indices: 0=Name,1=Account no,2=Password,3=Balance,4=Credit Score,5=Credit Points,6=Investment
        balance = actm[3] if len(actm) > 3 else "0"
        credit_score = actm[4] if len(actm) > 4 else "0"
        credit_points = actm[5] if len(actm) > 5 else "0"
        invested = actm[6] if len(actm) > 6 else "0"

        self.deposit_label = QLabel(f"Account Balance: ₹{balance}", self)
        self.deposit_label.setStyleSheet("color: #BB86FC; font: bold 16px;")

        self.credit_label = QLabel(f"Credit Points: {credit_points}", self)
        self.credit_label.setStyleSheet("color: #BB86FC; font: bold 16px;")

        self.credit_score_label = QLabel(f"Credit score: {credit_score}", self)
        self.credit_score_label.setStyleSheet("color: #BB86FC; font: bold 16px;")

        self.invest_label = QLabel(f"invested amount: {invested}", self)
        self.invest_label.setStyleSheet("color: #BB86FC; font: bold 16px;")

        box.addWidget(self.deposit_label, 0, 2)
        box.addWidget(self.credit_label, 1, 2)
        box.addWidget(self.credit_score_label, 2, 2)
        box.addWidget(self.invest_label, 3, 2)

        central_widget = QWidget(self)
        central_widget.setLayout(box)
        self.setCentralWidget(central_widget)

    def check(self):
        """Check username/password against CSV and open dashboard"""
        if not os.path.exists(file_path):
            self.show_message("Login failed", "No users registered yet.")
            return

        found = False
        with open(file_path, mode="r", newline='') as file:
            data = csv.reader(file)
            # If there is a header, skip it if needed
            rows = list(data)
            # skip header if present
            if rows and rows[0] and rows[0][0] == 'Name':
                rows = rows[1:]

            for r in rows:
                if len(r) < 3:
                    continue
                if self.username == r[0] and self.passwd == r[2] and not self.apple:
                    self.setup_dashboard(r)
                    self.apple = True
                    self.accountno = r[1]
                    found = True
                    break

        if not found:
            self.show_message("Login failed", "Incorrect username or password.")

    def deposit(self):
        amount, ok = QInputDialog.getDouble(self, "Deposit Amount", "Enter amount to deposit:", 0, 0, 1000000, 2)
        if ok:
            self.update_balance(amount)
            self.show_message("Deposit", f"Successfully deposited ₹{amount}")

    def check_balance(self):
        text = self.deposit_label.text()
        # "Account Balance: ₹<value>"
        bal_str = text.split("Account Balance: ₹")[-1].strip()
        self.show_message("Balance", f"You have ₹{bal_str} in your account")

    def withdraw(self):
        amount, ok = QInputDialog.getDouble(self, "Withdraw amount", "Enter amount to withdraw:", 0, 0, 1000000, 2)
        if ok:
            self.update_balance(-amount)
            self.show_message("Withdraw", f"Successfully withdrew ₹{amount}")

    def _safe_float_from_label(self, text, prefix):
        # helper to parse numbers from labels safely
        try:
            value = text.split(prefix)[-1].strip()
            # remove currency symbol if present
            value = value.replace("₹", "").replace(",", "").strip()
            return float(value) if value != "" else 0.0
        except Exception:
            return 0.0

    def update_balance(self, amount):
        current_balance = self._safe_float_from_label(self.deposit_label.text(), "Account Balance: ₹")
        new_balance = current_balance + float(amount)
        # keep two decimals
        self.deposit_label.setText(f"Account Balance: ₹{new_balance:.2f}")

    def update_credit(self):
        """Randomly update credit points"""
        random_range = random.randrange(0, 10)
        self.credit_label.setText(f"Credit Points: {random_range}")

    def update_credit_score(self):
        random_range = random.randrange(0, 100)
        self.credit_score_label.setText(f"Credit Score: {random_range}")

    def invest(self):
        amount, ok = QInputDialog.getDouble(self, "Invest Amount", "Enter amount to invest:", 0, 0, 1000000, 2)
        if ok:
            self.update_balance(-amount)
            self.update_investment(amount)
            self.show_message("Investment", f"Successfully invested ₹{amount} in bullion.")

    def show_message(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("QLabel { color: white; } QMessageBox { background-color: black; }")
        msg.exec()

    def update_investment(self, amount):
        current_invested = self._safe_float_from_label(self.invest_label.text(), "invested amount: ")
        new_balance = current_invested + float(amount)
        self.invest_label.setText(f"invested amount: {new_balance:.2f}")

    def logout(self):
        """Save current user's updated data back to CSV and go to login screen"""
        # gather current displayed values
        b = f"{self._safe_float_from_label(self.deposit_label.text(), 'Account Balance: ₹'):.2f}"
        c = str(self.credit_label.text().split(": ")[-1])
        d = f"{self._safe_float_from_label(self.invest_label.text(), 'invested amount: '):.2f}"
        e = str(self.credit_score_label.text().split(": ")[-1])

        if not os.path.exists(file_path):
            self.show_message("Error", "User data file missing.")
            return

        temp = []
        # Read all rows, keeping those not matching current username
        with open(file_path, mode="r", newline='') as file1:
            data = csv.reader(file1)
            rows = list(data)
            # handle header
            header = None
            if rows and rows[0] and rows[0][0] == 'Name':
                header = rows[0]
                rows = rows[1:]

            for r in rows:
                if len(r) < 3:
                    continue
                if r[0] != self.username:
                    temp.append(r)

        # rewrite file: header then current user then the others
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['Name', 'Account number', 'Password', 'Account Balance', 'Credit Score', 'Credit Points', 'Investment']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            # write current user with updated values
            writer.writerow({
                "Name": self.username,
                "Account number": self.accountno,
                "Password": self.passwd,
                "Account Balance": b,
                "Credit Score": e,
                "Credit Points": c,
                "Investment": d
            })
            # write others
            for i in temp:
                # ensure length
                while len(i) < 7:
                    i.append("0")
                writer.writerow({
                    "Name": i[0],
                    "Account number": i[1],
                    "Password": i[2],
                    "Account Balance": i[3],
                    "Credit Score": i[4],
                    "Credit Points": i[5],
                    "Investment": i[6]
                })

        # For debug: print the CSV rows to console
        with open(file_path, mode="r", newline='') as file1:
            data = csv.reader(file1)
            for r in data:
                print(r)

        self.username = ""
        self.passwd = ""
        self.apple = False
        self.login_create()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BankingSystemGUI()
    ex.show()
    sys.exit(app.exec())