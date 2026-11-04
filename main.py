
import sqlite3

# Connect to database
conn = sqlite3.connect("student_registration.db")
cursor = conn.cursor()

# Create Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    department TEXT
)
""")

# Create Courses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    credits INTEGER
)
""")

# Create Registration table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)
""")

conn.commit()


# Add Student
def add_student():
    name = input("Enter student name: ")
    email = input("Enter email: ")
    department = input("Enter department: ")

    cursor.execute(
        "INSERT INTO Students (name, email, department) VALUES (?, ?, ?)",
        (name, email, department)
    )

    conn.commit()
    print("Student added successfully!")


# Add Course
def add_course():
    course = input("Enter course name: ")
    credits = int(input("Enter course credits: "))

    cursor.execute(
        "INSERT INTO Courses (course_name, credits) VALUES (?, ?)",
        (course, credits)
    )

    conn.commit()
    print("Course added successfully!")


# Display Students
def show_students():
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()

    print("\n--- STUDENT DETAILS ---")

    for row in records:
        print(row)


# Display Courses
def show_courses():
    cursor.execute("SELECT * FROM Courses")
    records = cursor.fetchall()

    print("\n--- AVAILABLE COURSES ---")

    for row in records:
        print(row)


# Register Student for Course
def register_student():
    show_students()
    student_id = int(input("\nEnter student ID: "))

    show_courses()
    course_id = int(input("\nEnter course ID: "))

    cursor.execute(
        "INSERT INTO Registrations (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )

    conn.commit()
    print("Course registered successfully!")


# Display Registrations
def show_registrations():
    cursor.execute("""
    SELECT Students.name, Courses.course_name
    FROM Registrations
    JOIN Students ON Registrations.student_id = Students.student_id
    JOIN Courses ON Registrations.course_id = Courses.course_id
    """)

    records = cursor.fetchall()

    print("\n--- STUDENT COURSE REGISTRATIONS ---")

    for row in records:
        print("Student:", row[0], "| Course:", row[1])


# Delete Registration
def delete_registration():
    registration_id = int(input("Enter registration ID to delete: "))

    cursor.execute(
        "DELETE FROM Registrations WHERE registration_id = ?",
        (registration_id,)
    )

    conn.commit()
    print("Registration deleted successfully!")


# Update Student Email
def update_student():
    student_id = int(input("Enter student ID: "))
    new_email = input("Enter new email: ")

    cursor.execute(
        "UPDATE Students SET email = ? WHERE student_id = ?",
        (new_email, student_id)
    )

    conn.commit()
    print("Student details updated!")


# Main Menu
while True:

    print("\n===== STUDENT COURSE REGISTRATION SYSTEM =====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. View Students")
    print("4. View Courses")
    print("5. Register Student for Course")
    print("6. View Registrations")
    print("7. Update Student Email")
    print("8. Delete Registration")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_course()

    elif choice == "3":
        show_students()

    elif choice == "4":
        show_courses()

    elif choice == "5":
        register_student()

    elif choice == "6":
        show_registrations()

    elif choice == "7":
        update_student()

    elif choice == "8":
        delete_registration()

    elif choice == "9":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Try again.")

conn.close()
