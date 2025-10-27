import psycopg2

def add_centers():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )

        cursor = conn.cursor()
        name = input("enter the name of the center:")
        location = input("enter the spot where center is located:")
        waste_type = input("enter the waste type:")
        landmark = input("enter an area nearer to the waste center:")

        cursor.execute("insert into collection__spots (name,location,waste_type,landmark)values(%s,%s,%s,%s)", (name, location, waste_type,landmark, ))
        conn.commit()
        print("New Collection center is added successfully!")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

add_centers()