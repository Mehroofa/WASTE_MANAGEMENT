import psycopg2
import re

def block_user():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            username = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()
        
        email = input("enter user's email Id to block:")
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            print("The entered email is not a valid one!")
            return
        
        cursor.execute("update management_users set status='blocked' where email =%s", (email, ))
        conn.commit()
        print("User is blocked suceesfully!")
        
    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

block_user()



