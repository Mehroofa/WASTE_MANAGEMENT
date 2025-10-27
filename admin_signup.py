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

        name = input("Enter your name: ")
        password = stdiomask.getpass("Enter your password: ") #this will hide your password 
        
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            print("Your email is an invalid one!")
            return
        email = input("Enter your email: ")
        place = input("Enter your place: ")
        address = input("Enter your address: ")

        # Checking if entered email_id is already existing

        cursor.execute("SELECT * FROM management__admins WHERE email = %s", (email,))
        if cursor.fetchone():
            print("Email is already registered.")
        else:
            cursor.execute("INSERT INTO  management__admins(name, password, email, place, address ) VALUES (%s, %s, %s, %s, %s)" , (name,password,email,place,address, ))
            conn.commit()
            print(" You are signed up successfully!")

    except psycopg2.Error as e:
        print(" Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
signup()
