from PIL import Image  #library to work the project with images of complaints
import imagehash  #library to detect the digital fingerprint of images uploaded
import os  #library to check image file already exists in db
import psycopg2

def complaints_with_images():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        complaint_area = input("enter your complaint:")
        image_path = input("enter your image's path:")

        #to check file exists
        if not os.path.exists(image_path):
            print("file is not existing")

        #to create an unique hash for the image
        img = Image.open(image_path)
        image_hash = str(imagehash.average_hash(img))

        #to check if the hash is already existing
        cursor.execute("select name from complaints where image_hash=%s", (image_hash, ))
        duplicate = cursor.fetchall()

        if duplicate:
            print("Duplicate image detected! No new complaint filed!")

        #if no duplicates recieved insert new complaint with image
        cursor.execute("insert into complaints (complaint_area,image_hash)values(%s,%s)",( complaint_area, image_hash))
        conn.commit()
        print("Complaint filed successfully!!")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

complaints_with_images()
