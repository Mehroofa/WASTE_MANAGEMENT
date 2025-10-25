import psycopg2

def admin_login():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()
        name = input("enter admin's name:")
        password = input("enter admin password:")

        cursor.execute("select * from management_admin where name = %s and password = %s", (name, password, ))
        admin = cursor.fetchall()

        if admin:
            print("You are logined successfully to the system")
        else:
            print("Invalid name and password")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

admin_login()