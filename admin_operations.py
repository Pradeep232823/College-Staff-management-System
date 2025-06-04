from db_connection import get_connection

def add_staff():
    conn = get_connection()
    cursor = conn.cursor()
    staff_id=int(input("Enter staff id: "))
    name = input("Enter Name: ")
    gender = input("Gender: ")
    phone = input("Phone: ")
    email = input("Email: ")
    qualification = input("Qualification: ")
    doj = input("Date of Joining (YYYY-MM-DD): ")
    department = input("Department: ")
    salary = float(input("Salary: "))
    username = email
    password = email
    assigned_class = input("Assigned Class: ")
    
    cursor.execute("""
        INSERT INTO staff (staff_id,name, gender, phone, email, qualification, doj, department, salary, username, password, assigned_class)
        VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (staff_id,name, gender, phone, email, qualification, doj, department, salary, username, password, assigned_class))
    conn.commit()
    print("Staff added successfully.")
    cursor.close()
    conn.close()

def update_staff():
    conn = get_connection()
    cursor = conn.cursor()

    staff_id = input("Enter Staff ID to update: ")

    field_map = {
        '1': 'name',
        '2': 'phone',
        '3': 'department',
        '4': 'salary',
        '5': 'assigned_class',
        '6': 'qualification',
        '7': 'email'
    }

    print("Choose fields to update (comma separated):")
    for key, field in field_map.items():
        print(f"{key}. {field.replace('_', ' ').title()}")

    choices = input("Enter your choices (e.g., 1,3,5): ").replace(" ", "").split(',')

    # Validate choices
    valid_choices = [c for c in choices if c in field_map]

    if not valid_choices:
        print("No valid choices selected.")
        cursor.close()
        conn.close()
        return

    update_fields = []
    update_values = []

    for choice in valid_choices:
        new_value = input(f"Enter new value for {field_map[choice]}: ")
        update_fields.append(f"{field_map[choice]} = %s")
        update_values.append(new_value)

    update_values.append(staff_id)

    query = f"UPDATE staff SET {', '.join(update_fields)} WHERE staff_id = %s"

    cursor.execute(query, tuple(update_values))
    conn.commit()
    print("Staff details updated successfully.")

    cursor.close()
    conn.close()


def remove_staff():
    conn = get_connection()
    cursor = conn.cursor()
    staff_id = input("Enter Staff ID to remove: ")
    cursor.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
    conn.commit()
    print("Staff removed.")
    cursor.close()
    conn.close()

def total_staff_display():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM staff"
    cursor.execute(query)
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

def salary_report():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Total salary of all staff
    cursor.execute("SELECT SUM(salary) FROM staff")
    total_salary = cursor.fetchone()[0] or 0
    print(f"\nTotal Salary Paid to All Staff: {total_salary:.4f}\n")

    # 2. Department-wise salary summary
    cursor.execute("SELECT department, SUM(salary) FROM staff GROUP BY department")
    dept_salaries = cursor.fetchall()
    print("Department-wise Salary Summary:")
    print(f"{'Department':<20} {'Total Salary':>15}")
    print("-" * 35)
    for dept, total in dept_salaries:
        print(f"{dept:<20} {total:>15.2f}")
    print()
    cursor.close()
    conn.close()

def monthly_attendance_management():
    conn = get_connection()
    cursor = conn.cursor()
    staff_id = input("Enter Staff ID: ")
    attendance = int(input("Enter number of days present this month: "))
    cursor.execute("UPDATE staff SET monthly_attendance = %s WHERE staff_id = %s", (attendance, staff_id))
    conn.commit()
    print("Attendance updated.")
    cursor.close()
    conn.close()

def assigning_classes():
    conn = get_connection()
    cursor = conn.cursor()
    staff_id = input("Enter Staff ID: ")
    assigned_class = input("Enter Assigned Class: ")
    cursor.execute("UPDATE staff SET assigned_class = %s WHERE staff_id = %s", (assigned_class, staff_id))
    conn.commit()
    print("Assignment updated.")
    cursor.close()
    conn.close()
