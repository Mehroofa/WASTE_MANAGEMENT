import psycopg2

def remove_centers():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        name = input("Enter the name of the waste center you want to remove: ")

        cursor.execute("select * from collection__spots where name=%s" , (name, ))
        center=cursor.fetchone()

        if not center:
            print("Email is not available!")
            return
        
        cursor.execute("delete from collection__spots where name=%s",(name, ))
        conn.commit()
        print("User is been removed")

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

remove_centers()
        