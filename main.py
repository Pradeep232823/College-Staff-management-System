from login import login
from admin_operations import *
from staff_operations import staff_menu

def main():
    while True:
        print("\n=== College Staff Management System ===")
        print("1. Admin Login")
        print("2. Staff Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user = login('admin')
            if user:
                admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == '2':
            user = login('staff')
            if user:
                staff_menu(user[9])  # username at index 9
            else:
                print("Invalid staff credentials.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Staff")
        print("2. Update Staff")
        print("3. Remove Staff")
        print("4. Total Staff Display")
        print("5. Salary Report")
        print("6. Monthly Attendance Management")
        print("7. Assign Classes")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_staff()
        elif choice == '2':
            update_staff()
        elif choice == '3':
            remove_staff()
        elif choice == '4':
            total_staff_display()
        elif choice == '5':
            salary_report()
        elif choice == '6':
            monthly_attendance_management()
        elif choice == '7':
            assigning_classes()
        elif choice == '8':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
