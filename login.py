from db_connection import get_connection

def login(user_type):
    conn = get_connection()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")

    if user_type == 'admin':
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
    else:
        cursor.execute("SELECT * FROM staff WHERE username=%s AND password=%s", (username, password))

    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
