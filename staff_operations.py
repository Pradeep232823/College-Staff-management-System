from db_connection import get_connection

def staff_menu(username):
    while True:
        print("\nStaff Menu:")
        print("1. View Personal Details")
        print("2. View Assigned Classes")
        print("3. View Monthly Attendance Report")
        print("4. View Salary Report")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_personal_details(username)
        elif choice == '2':
            view_assigned_classes(username)
        elif choice == '3':
            view_attendance(username)
        elif choice == '4':
            view_salary(username)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def view_personal_details(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff WHERE username = %s", (username,))
    rows = cursor.fetchall()

    print(f"\nTotal staff: {len(rows)}\n")
    print("-" * 160)
    print(f"{'ID':<3} {'Name':<15} {'Gen':<4} {'Phone':<12} {'Email':<16} {'Qual':<10} {'DOJ':<13} {'Dept':<10} {'Sal':<12} {'User':<17} {'pass':<15} {'Class':<10} {'Att':<4}")
    print("-" * 160)

    for row in rows:
        print(f"{row[0]:<3} {row[1]:<15} {row[2]:<4} {row[3]:<12} {row[4]:<16} {row[5]:<10} {str(row[6]):<13} {row[7]:<10} {row[8]:<12.4f} {row[9]:<17} {row[10]:<15} {row[11]:<10} {row[12]:<4}")

    print("-" * 160)
    cursor.close()
    conn.close()

def view_assigned_classes(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT assigned_class FROM staff WHERE username = %s", (username,))
    data = cursor.fetchone()
    print("Assigned Class:", data[0])
    cursor.close()
    conn.close()

def view_attendance(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT monthly_attendance FROM staff WHERE username = %s", (username,))
    data = cursor.fetchone()
    print("Monthly Attendance:", data[0])
    cursor.close()
    conn.close()

def view_salary(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT salary FROM staff WHERE username = %s", (username,))
    data = cursor.fetchone()
    print("Salary:", data[0])
    cursor.close()
    conn.close()
