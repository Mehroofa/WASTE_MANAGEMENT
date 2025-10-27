import psycopg2

def update_complaint_status():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        u_id= input("enter collector's id:")
        status = input("enter the status(solved/pending):")

        cursor.execute("update user__complaints set status = %s where u_id = %s", (status, u_id))
        conn.commit()
        print("Complaint status is updated successfully!")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

update_complaint_status()