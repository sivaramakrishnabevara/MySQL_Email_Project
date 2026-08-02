# 📊 Employee Report Automation System

An automated Python-based project that connects to a **MySQL database (using DBeaver)**, retrieves employee data, generates an **Excel report**, and automatically sends it via **Gmail**.

---

## 📌 Project Overview

This project eliminates the need for manually creating employee reports. It automates the complete workflow from database to email using Python.

### Workflow

```text
DBeaver (MySQL Database)
          │
          ▼
     Python Script
          │
          ▼
 Execute SQL Query
          │
          ▼
 Retrieve Employee Data
          │
          ▼
 Generate Excel Report
          │
          ▼
 Send Report via Gmail
```

---

# 🚀 Features

* ✅ Connects to MySQL Database
* ✅ Retrieves employee data using SQL queries
* ✅ Converts data into an Excel report
* ✅ Automatically sends the report via Gmail
* ✅ Includes exception handling
* ✅ Simple and easy to customize

---

# 🛠 Technologies Used

* Python 3.x
* MySQL
* DBeaver
* Pandas
* MySQL Connector
* OpenPyXL
* SMTP (Gmail)

---

# 📂 Project Structure

```text
Employee-Report-Automation/
│
├── main.py                  # Fetch employee data from MySQL
├── email_sender.py          # Send Excel report via email
├── Employee_Report.xlsx     # Generated Excel file
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/sivaramakrishnabevara/MySQL_Email_Project.git

cd MySQL_Email_Project
```

---

## Install Dependencies

```bash
pip install pandas
pip install openpyxl
pip install mysql-connector-python
```

Or

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Configuration

Update the database credentials inside the Python script.

```python
host="localhost"
port=3306
user="root"
password="YOUR_PASSWORD"
database="YOUR_DATABASE"
```

---

# 📧 Gmail Configuration

Create a Gmail App Password and update:

```python
sender_email="your_email@gmail.com"
receiver_email="receiver@gmail.com"
app_password="Your_16_Character_App_Password"
```

> **Note:** Never upload your real password or Gmail App Password to GitHub. Use environment variables or a `.env` file instead.

---

# ▶️ Run the Project

### Step 1

Generate the Employee Report

```bash
python main.py
```

### Step 2

Send the Email

```bash
python email_sender.py
```

---

# 📸 Output

✔ Employee data fetched from MySQL

✔ Excel report generated automatically

✔ Email sent with Excel attachment

---

# 📈 Future Improvements

* Add a graphical user interface (GUI)
* Schedule automatic report generation
* Export reports to PDF
* Support multiple email recipients
* Add charts and dashboards
* Secure credentials using environment variables

---

# 👨‍💻 Author

**Bevara Siva Rama Krishna**

B.Tech – Artificial Intelligence & Data Science

Aspiring Data Analyst | Python Developer | SQL | Power BI | Automation Enthusiast

---

# ⭐ If you found this project useful, please give it a Star!
