import psycopg2

def searching_centers():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )

        cursor = conn.cursor()
        print("\n ----search nearby collection_centers----")
        print("1.search by location")
        print("2.search by type of waste")
        choice = input("enter your choice(1 or 2):")

        if choice == '1':
            location = input("enter your location:")
            cursor.execute("select name,location,waste_type,landmark from collection_spots where location = %s", (location, ))
        elif choice == '2':
            waste_type = input("enter your waste_type(garbage,food waste,e-waste):")
            cursor.execute("select name,location,waste_type,landmark from collection_spots where waste_type = %s", (waste_type, ))
        else:
            print("Invalid choice")

        result = cursor.fetchall()
        if not result:
            print("No Collection centers are found")
        else:
            for name,location,waste_type,landmark in result:
                print(f"{name} - {location} - {waste_type} - {landmark}")

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

searching_centers()
        



