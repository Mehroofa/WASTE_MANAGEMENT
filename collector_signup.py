import psycopg2
import re
from getpass import getpass
import stdiomask
def signup():
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="admin",
            database="management"
        )
        cursor = conn.cursor()

        id = input("Enter your ID:")
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            print("Your email is an invalid one!")
            return

        password = stdiomask.getpass("Enter your password: ",mask = "*") #hides password and display stars
        place = input("Enter your place: ")
        phno = input("Enter your phone number:")
        if not re.fullmatch(r'\d{10}', phno):
            print("This is not an invalid phone number! It must be exactly 10 digits.")
            return

        # Checking if entered email_id is already existing

        cursor.execute("SELECT * FROM waste__collectors WHERE email = %s", (email,))
        if cursor.fetchone():
            print("Email is already registered.")
        else:
            cursor.execute("INSERT INTO waste__collectors (id, name, email, password, place, phno) VALUES (%s, %s, %s, %s, %s,%s)" , (id,name,email,password,place, phno ))
            conn.commit()
            print(" You are signed up successfully!")

    except psycopg2.Error as e:
        print(" Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
signup()
