# 📚 Library Management System (LMS) using Python & MySQL

A simple console-based Library Management System built with **Python** and connected to a **MySQL** database using the `mysql-connector` library. This system supports basic book management functions like adding, issuing, submitting, updating, deleting, and viewing books, along with tracking issue and submission status.

---

## 🔧 Features

- ➕ Add new books to the library
- 📤 Issue books to students
- 📥 Submit returned books
- 🔄 Update book quantity
- 🗑️ Delete book records
- 📖 View all available books
- 📋 View issued and submitted books
- 🔐 Password-protected access

---

## 💻 Technologies Used

- **Python 3.x**
- **MySQL** (Relational Database)
- `mysql-connector-python` (for database connectivity)

---

## 📁 Table Structure (MySQL)

Before running the program, ensure you have the following tables in your MySQL database:

```sql
CREATE DATABASE library;

USE library;

CREATE TABLE book (
    bname VARCHAR(100),
    bcode VARCHAR(20) PRIMARY KEY,
    total INT,
    subject VARCHAR(100)
);

CREATE TABLE issuebook (
    name VARCHAR(100),
    regno VARCHAR(20),
    bcode VARCHAR(20),
    idate DATE
);

CREATE TABLE submitbook (
    name VARCHAR(100),
    regno VARCHAR(20),
    bcode VARCHAR(20),
    sdate DATE
);
```

---

## 🔐 Setup Instructions
Clone the Repository:

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
Install MySQL Connector:
```
```bash
pip install mysql-connector-python
Configure MySQL Connection:
```

Update the connection settings in the script:
```python
con = a.connect(host='localhost', user='root', passwd='your_password', database='library')
Run the Application:
```
```bash
python library_manager.py
```
Password Prompt:
You’ll be asked for a password on startup. Make sure it matches the one hardcoded in the `pswd()` function or consider replacing it with a secure prompt.

---

### ✅ Optional Files to Include:
- `library_manager.py` – your main script
- `.gitignore` – to exclude files like `.pyc`, `.env`, etc.
- `requirements.txt` – with `mysql-connector-python`
- `LICENSE` – if you’re applying a license (MIT recommended)

---

## 👨‍💻 Author
Sarvagya Chaturvedi
[Sarvagya-24-chaturvedi](https://github.com/Sarvagya-24-chaturvedi)

---
