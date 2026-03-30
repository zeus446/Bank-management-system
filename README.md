# 🏦 Banking System GUI (PyQt6)

## 📌 Project Title
Banking System GUI – A Desktop Banking Application Built with Python and PyQt6

---

## 📖 Introduction

The **Banking System GUI** is a desktop-based banking application developed using **Python** and **PyQt6**.

This application allows users to:

- Create an account  
- Log in securely  
- Deposit and withdraw funds  
- Invest money  
- Track credit points  
- View credit score  
- Persist account data using a CSV file  

It features a clean dark-themed graphical interface and simulates basic banking operations for learning and demonstration purposes.

---

## 📂 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Dependencies](#-dependencies)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Data Storage Format](#-data-storage-format)
- [Application Flow](#-application-flow)
- [Troubleshooting](#-troubleshooting)
- [Security Notice](#-security-notice)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## ✨ Features

- 🔐 Account Registration with password confirmation  
- 🔑 Secure Login System  
- 💰 Deposit Money  
- 💸 Withdraw Money  
- 📊 Real-Time Balance Display  
- 📈 Investment Tracking  
- 🎯 Random Credit Points Generator  
- 🏆 Random Credit Score Generator  
- 💾 Persistent Data Storage using CSV  
- 🚪 Logout with Automatic Save  
- 🎨 Dark Theme GUI  

---

## 🛠 Installation

### 1️⃣ Clone or Download the Project

```bash
git clone <your-repository-url>
cd banking-system-gui
```

Or simply download the `.py` file into a folder.

---

### 2️⃣ Install Required Dependencies

Make sure Python 3.9+ is installed.

Install PyQt6:

```bash
pip install PyQt6
```

---

## 📦 Dependencies

- Python 3.x  
- PyQt6  
- Built-in Python modules:
  - sys  
  - csv  
  - random  
  - os  

---

## ▶️ Usage

Run the application:

```bash
python banking_system.py
```

(Replace `banking_system.py` with your actual filename.)

---

## 🧭 Application Flow

### ➤ Launch Application
You will see two options:
- **Login**
- **Create**

---

### ➤ Create Account

1. Click **Create**
2. Enter your name
3. Enter password (twice for confirmation)
4. Click **Register**

New accounts start with:
- ₹3000 Account Balance  
- 0 Credit Score  
- 0 Credit Points  
- 0 Investment  

---

### ➤ Login

1. Click **Login**
2. Enter username
3. Enter password
4. Access dashboard

---

## 🖥 Dashboard Options

Once logged in, you can:

- 💰 Deposit Money
- 💸 Withdraw Money
- 📊 Check Account Balance
- 📈 Invest Money
- 🎯 Check Credit Points
- 🏆 Check Credit Score
- 🚪 Logout (saves data to CSV)

---

## 📁 Project Structure

```
project-folder/
│
├── banking_system.py
├── user_data.csv  (auto-generated)
└── README.md
```

---

## 🗄 Data Storage Format

The system uses a CSV file named:

```
user_data.csv
```

This file is automatically created in the same directory as the script.

### CSV Structure:

| Name | Account number | Password | Account Balance | Credit Score | Credit Points | Investment |
|------|----------------|----------|----------------|--------------|--------------|------------|

### Example Entry:

```csv
John,12345,pass123,3000,0,0,0
```

---

## 🛑 Troubleshooting

### ❌ Login Failed
- Ensure username and password are correct
- Make sure the account is registered
- Check if `user_data.csv` exists

---

### ❌ Data Not Saving
- Always click **Logout** before closing the application
- Ensure file write permissions are enabled

---

### ❌ PyQt6 Not Installed
Run:

```bash
pip install PyQt6
```

---

## 🔐 Security Notice

⚠️ Passwords are stored in **plain text** inside the CSV file.

This project is intended for **educational purposes only**.

For production-level applications, consider:

- Password hashing (bcrypt or hashlib)
- Using SQLite or another database
- Implementing authentication validation
- Adding transaction logging
- Adding input validation

---

## 🚀 Future Improvements

- 🔒 Password Hashing
- 🗄 Database Integration (SQLite/MySQL)
- 💳 Transaction History
- 📊 Real Credit Score Logic
- 🏦 Unique Account Number Validation
- 💰 Interest Calculation for Investments
- 🧾 Admin Panel
- 🎨 Improved UI/UX Design

---

## 👨‍💻 Contributors

Developed as a Python + PyQt6 learning project.

You are free to modify and expand this project.

---

## 📜 License

This project is open-source and free to use for educational purposes.

You may modify and distribute it as needed.

---

# 🏁 End of README
