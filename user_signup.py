import psycopg2
import re
from getpass import getpass

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
        email = input("Enter your email: ")
        password = getpass("Enter your password: ")
        address = input("Enter your address: ")
        phno = input("Enter yur phone number:")
        if not re.fullmatch(r'\d{10}', phno):
            print("This is not an invalid phone number! It must be exactly 10 digits.")
            return
    
        location = input("Enter your location: ")
        status = input("What is the current status of the user: ")

        # Checking if entered email_id is already existing

        cursor.execute("SELECT * FROM management_users WHERE email = %s", (email,))
        if cursor.fetchone():
            print("Email is already registered.")
        else:
            cursor.execute("INSERT INTO management_users (name, email, password, address, phno, location, status ) VALUES (%s, %s, %s, %s, %s, %s,%s)" , (name,email,password,address,phno,location,status, ))
            conn.commit()
            print("You are signed up successfully!")

    except psycopg2.Error as e:
        print("❌ Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
signup()
