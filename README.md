# Student Course Registration System (DBMS PBL Project)

A lightweight, user-friendly *Student Course Registration System* built as a Project-Based Learning (PBL) initiative for a Database Management Systems (DBMS) course. It features both a *Command-Line Interface (CLI)* and a clean *Web Interface* powered by Flask and SQLite.

---

## 🚀 Features
* *Add Students:* Register new students with their name, email, and department.
* *Add Courses:* Create courses along with their credit values.
* *Course Registration:* Register students into specific courses (Many-to-Many relationship).
* *View Records:* Display all students, available courses, and active registrations.
* *Update Records:* Modify student email details using SQL UPDATE.
* *Delete Records:* Remove course registrations using SQL DELETE.

---

## 🛠️ Tech Stack
* *Frontend:* HTML5, CSS3
* *Backend:* Python, Flask
* *Database:* SQLite (Relational Database)

---

## 📂 Project Structure
```text
StudentCourseRegistration/
│
├── static/
│   └── style.css          # Stylesheet for the web dashboard
├── templates/
│   └── index.html         # Main dashboard HTML template
├── app.py                 # Flask web application server
├── main.py                # Command-line interface version & database init
└── student_registration.db# SQLite Database file (auto-generated)
