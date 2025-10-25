import psycopg2
from getpass import getpass
import stdiomask
def collector_login():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()
        id = input("enter your id:")
        email = input("enter your email-id:").strip()
        password = stdiomask.getpass("enter your pass to log:").strip()

        cursor.execute("select * from waste__collector where id=%s and email=%s and password=%s",(id, email, password, ))
        collector = cursor.fetchone()

        if collector:
            print("You are successfully logined")
        else:
            print("Invalid details!")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()
collector_login()


