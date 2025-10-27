import psycopg2

def user_complaints(collector_id):
    try:
        conn = psycopg2.connect(
            host = "localhost",
            username = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()
        
        user_id = input("enter the user's id that requested to collect waste:")
        cursor.execute("update assign__collections set status='resolved' where user_id=%s and collector_id=%s", (user_id, collector_id, ))
        conn.commit()
        print("Request status is updated successfully")

    except psycopg2.Error as e:
        print("❌ Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

user_complaints(108)
