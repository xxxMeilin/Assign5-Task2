import psycopg2

def connect():
    conn = psycopg2.connect(database='Assign2', user='postgres', password='Aa20030802', host='localhost', port='5432')
    return conn

def read(student_number):
    conn = connect()
    cur = conn.cursor()
    sql = 'SELECT * FROM student WHERE sno = %s'
    cur.execute(sql, (student_number,))
    info = cur.fetchall()
    cur.close()
    conn.close()

    return info

def insert(number, name, age, gender, department):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO student (sno, sname, sage, sgender, sdept) VALUES (%s, %s, %s, %s, %s)",
                (number, name, age, gender, department))
    print("New student information inserted successfully.\n")

    conn.commit()
    cur.close()
    conn.close()

def update():
    student_number = input("Enter student number: \n")
    info = read(student_number)
    if info:
        print("Current student information:")
        for row in info:
            print(row)
    else:
        print("No student found with the given student number.\n")
        return

    conn = connect()
    cur = conn.cursor()

    new_name = input("Enter new name: ")
    new_age = input("Enter new age: ")
    new_gender = input("Enter new gender: ")
    new_department_name = input("Enter new department name: ")
    cur.execute("UPDATE student SET sname = %s, sage = %s, sgender = %s, sdept = %s WHERE sno = %s",
                (new_name, new_age, new_gender, new_department_name, student_number))
    print("Student information updated successfully.\n")

    conn.commit()
    cur.close()
    conn.close()

    info = read(student_number)
    print("Updated student information:")
    for row in info:
        print(row)

def delete():
    conn = connect()
    cur = conn.cursor()
    student_number = input("Enter student number: \n")

    cur.execute("SELECT * FROM sc WHERE sno = %s", (student_number,))
    enrollment_records = cur.fetchall()

    if enrollment_records:
        cur.execute("DELETE FROM sc WHERE sno = %s", (student_number,))
    cur.execute("DELETE FROM student WHERE sno = %s", (student_number,))
    print("Student deleted successfully. \n")

    conn.commit()
    cur.close()
    conn.close()


while True:
    print("Menu:\n1. Read student information\n2. Insert new student information\n3. Update student information\n4. Delete student information\n5. Exit")
    choice = input("Enter your choice (1-5): \n")
    if choice == '1':
        student_number = input("Enter student number: \n")
        info = read(student_number)
        if info:
            for row in info:
                print(row)
                print(' ')
        else:
            print("No student found with the given student number.\n")
    elif choice == '2':
        while True:
            number = input("Enter student number: \n")
            info = read(number)
            if info:
                print("Student number already exists. Please enter a different student number.\n")
            else:
                name = input("Enter the student's name: \n")
                age = int(input("Enter the student's age: \n"))
                gender = input("Enter the student's gender(F/M): \n")
                department = input("Enter the student's department name: \n")
                insert(number, name, age, gender, department)
                break
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

