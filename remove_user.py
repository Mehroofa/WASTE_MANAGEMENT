import psycopg2

def remove_user():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        email = input("Enter the email of the user you want to remove: ")

        cursor.execute("select * from collection_users where email=%s" , (email, ))
        user=cursor.fetchone()

        if not user:
            print("Email is not available!")
            return
        
        cursor.execute("delete from collection_users where email=%s",(email, ))
        conn.commit()
        print("User is been removed")

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

remove_user()
        