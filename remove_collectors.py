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

        id = input("Enter the id of the user you want to remove: ")

        cursor.execute("select * from waste__collectors where id=%s" , (id, ))
        user=cursor.fetchone()

        if not user:
            print("id is not registered!")
            return
        
        cursor.execute("delete from waste__collectors where id=%s",(id, ))
        conn.commit()
        print("User is been removed")

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

remove_user()
        