import psycopg2
from tabulate import tabulate

def view_centers():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )

        cursor = conn.cursor()
        cursor.execute("select * from collection__spots")
        centers = cursor.fetchall()

        print("\n ---Collection Centers are---")
        if not centers:
            print("No Collection centers are found!")
        else:
            headers = ["Name", "Location", "Waste Type", "Landmark"]
            print(tabulate(centers, headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

view_centers()


        




