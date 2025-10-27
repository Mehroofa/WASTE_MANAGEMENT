import psycopg2
from tabulate import tabulate

def view_collection_requests(collector_id):
    try:
        conn = psycopg2.connect(
            host = "localhost",
            username = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        cursor.execute("select name,user_id,waste_type,location,landmark,status from assign__collections where collector_id = %s",(collector_id, ))
        requests = cursor.fetchall()


        print("\n --Collection requests are--")
        if not requests:
            print("No collection requests are uploaded!")
        else:
            headers = ["name","user_id","waste_type","location","landmark","status"]
            print(tabulate(requests,headers,tablefmt="grid"))

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

view_collection_requests(104)