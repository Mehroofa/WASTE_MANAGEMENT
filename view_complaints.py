import psycopg2
from tabulate import tabulate

def view_complaints():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()
        cursor.execute("select name,u_id,location,phno,complaint_area,status,image_hash from user__complaints")
        complaints = cursor.fetchall()

        if not complaints:
            print("No complaints are filed")
        else:
            headers = ["name","u_id","location","phno","complaint_area","status","image_hash"]
            print(tabulate(complaints, headers, tablefmt = "grid"))

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

view_complaints()




