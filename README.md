# 🗂️ Student CRUD Management System — PostgreSQL + Python

This project is a **simple and practical CRUD (Create, Read, Update, Delete)** application built using **Python** and **PostgreSQL**, created for practice and learning purposes.

---

## 📌 Project Purpose

> This project is part of my personal learning journey to understand database interactions using **Python** and **PostgreSQL**.  
> It implements a complete CLI-based CRUD system that securely manages student records and demonstrates the use of parameterized queries, database connections, and user input handling.

---

## 🧠 Key Features

- ➕ Insert new student records  
- 📖 View all students  
- ✏️ Update specific fields (name, age, address, phone number)  
- ❌ Delete a student record with confirmation  
- 🧱 Create table (if not already created)

---

## 🔐 Database Configuration

Ensure the following PostgreSQL connection details match your local environment:

| Parameter  | Value (default)      |
|------------|----------------------|
| `dbname`   | `studentdb`          |
| `user`     | `postgres`           |
| `password` | `8984`               |
| `host`     | `localhost`          |
| `port`     | `5432`               |

You can modify these values directly in the Python script if your setup is different.

---

## ⚙️ How to Run This Project (Step-by-Step)

### 1️⃣ Install PostgreSQL
Download and install PostgreSQL from [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

### 2️⃣ Create the Database

Open **pgAdmin** or use the **psql terminal**, then run:

### 3️⃣ Install Python and Required Library
Install psycopg2-binary using pip:
pip install psycopg2-binary

### 4️⃣ Clone the Repository
git clone https://github.com/codetush7/CrudStudentMangSys.git

cd CrudStudentMangSys

### 5️⃣ Run the Python File
python main.py
(🔁 Replace main.py with your actual script filename if different.)

💡 Pro Tip: While the application works well, but to make our application more robust, always use `try-except-finally` blocks around PostgreSQL operations — this keeps our code clean, safe, and error-resilient.

```python
try:
    conn = psycopg2.connect(...)
    cur = conn.cursor()
    # Perform DB operations
except Exception as e:
    print("Database connection failed:", e)
finally:
    conn.commit()
    conn.close()
```
🛑 Errors are caught and handled

✅ Database connections are always closed

⚙️ Code is easier to debug and maintain


