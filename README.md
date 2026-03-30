# Bank-management-system

🏦 Banking System GUI (PyQt6)
Introduction

Banking System GUI is a desktop-based banking application built using Python and PyQt6. It provides a graphical user interface that allows users to:

Create an account
Log in securely
Deposit and withdraw funds
Check account balance
Invest money
View and update credit points
View credit score
Persist account data using a CSV file

The application uses a simple CSV-based storage system (user_data.csv) to maintain user account records.

Table of Contents
Features
Installation
Dependencies
Usage
Configuration
Project Structure
Data Storage Format
Examples
Troubleshooting
Future Improvements
License
Features
🔐 User Registration with password confirmation
🔑 Secure Login system
💰 Deposit funds
💸 Withdraw funds
📊 Real-time balance display
📈 Investment tracking
🎯 Randomized credit points system
🏆 Randomized credit score system
💾 Persistent data storage using CSV
🚪 Logout with automatic data saving
🎨 Dark-themed GUI interface
Installation
1. Clone or Download the Project
git clone <your-repository-url>
cd banking-system-gui

Or simply download the .py file.

2. Install Required Dependencies

Make sure Python 3.9+ is installed.

Install PyQt6:

pip install PyQt6
Dependencies
Python 3.x
PyQt6
Built-in Python modules:
sys
csv
random
os
Usage

Run the application:

python banking_system.py

(Replace banking_system.py with your actual filename.)

Application Flow
Launch App
Choose:
Login
Create
If creating:
Enter name
Enter password (twice)
Register
If logging in:
Enter username
Enter password
Access dashboard
Dashboard Options
Deposit
Withdraw
Check Balance
Invest
Check Credit Points
Check Credit Score
Logout
Configuration

The system stores user data in:

user_data.csv

This file is automatically created in the same directory as the script if it does not exist.

No additional configuration is required.

Project Structure
project-folder/
│
├── banking_system.py
├── user_data.csv (auto-generated)
└── README.md
Data Storage Format

The CSV file uses the following structure:

Name	Account number	Password	Account Balance	Credit Score	Credit Points	Investment

Example row:

John,12345,pass123,3000,0,0,0
Examples
Creating an Account
Click Create
Enter name
Enter password (twice)
Click Register
Account starts with:
₹3000 balance
0 Credit Score
0 Credit Points
0 Investment
Deposit Example
Enter ₹500
Balance updates instantly on dashboard
Investment Example
Invest ₹1000
Balance decreases
Investment amount increases
Troubleshooting
❌ Login Failed
Ensure username and password match exactly
Ensure user_data.csv exists
Make sure account was registered successfully
❌ Data Not Saving
Always use Logout to ensure updated data is written to CSV
Check file permissions in the project directory
❌ PyQt6 Not Installed

Install it using:

pip install PyQt6
Security Notice

⚠️ This project stores passwords in plain text inside a CSV file.

For production use, consider:

Hashing passwords (e.g., bcrypt)
Using a database instead of CSV
Implementing authentication best practices
Future Improvements
🔒 Password hashing
🗄 Database integration (SQLite/MySQL)
💳 Transaction history
📊 Real credit score logic
🎨 Improved UI/UX
🏦 Unique account number validation
💰 Interest calculations for investments
🧾 Admin panel
License

This project is open-source and free to use for educational purposes.

You may modify and distribute it as needed.