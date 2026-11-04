
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("student_registration.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@app.route("/")
def home():
    conn = get_db()
    students = conn.execute("SELECT * FROM Students").fetchall()
    courses = conn.execute("SELECT * FROM Courses").fetchall()

    registrations = conn.execute("""
        SELECT Registrations.registration_id,
               Students.name,
               Courses.course_name
        FROM Registrations
        JOIN Students ON Registrations.student_id = Students.student_id
        JOIN Courses ON Registrations.course_id = Courses.course_id
    """).fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students,
        courses=courses,
        registrations=registrations
    )


@app.route("/add_student", methods=["POST"])
def add_student():
    conn = get_db()
    conn.execute(
        "INSERT INTO Students (name, email, department) VALUES (?, ?, ?)",
        (request.form["name"], request.form["email"],
         request.form["department"])
    )
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/add_course", methods=["POST"])
def add_course():
    conn = get_db()
    conn.execute(
        "INSERT INTO Courses (course_name, credits) VALUES (?, ?)",
        (request.form["course_name"], request.form["credits"])
    )
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/register", methods=["POST"])
def register():
    conn = get_db()
    conn.execute(
        "INSERT INTO Registrations (student_id, course_id) VALUES (?, ?)",
        (request.form["student_id"], request.form["course_id"])
    )
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/update_student", methods=["POST"])
def update_student():
    conn = get_db()
    conn.execute(
        "UPDATE Students SET email = ? WHERE student_id = ?",
        (request.form["email"], request.form["student_id"])
    )
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/delete/<int:registration_id>")
def delete_registration(registration_id):
    conn = get_db()
    conn.execute(
        "DELETE FROM Registrations WHERE registration_id = ?",
        (registration_id,)
    )
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
