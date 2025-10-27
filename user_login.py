import psycopg2

def login():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        email = input("enter your email_id:").strip()
        password = input("enter your password:").strip()

        cursor.execute("select * from collection_users where email=%s and password=%s", (email, password, ))
        users = cursor.fetchone()

        if users:
            print("login successfull")
        else:
            print("invalid email and password!")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

login()
