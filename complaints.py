import psycopg2
import os
from PIL import Image
import imagehash
import re

def user_complaints():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            username = "postgres",
            password = "admin",
            database = "management"
        )
        cursor = conn.cursor()

        print("\n ---To file a complaint of user---")
        name = input("enter your name:")
        location = input("enter your current location:")
        phno = input("enter a valid phone number:") 
        if not re.fullmatch(r'\d{10}', phno):
            print("This is not an invalid phone number! It must be exactly 10 digits.")
            return
    
        complaint_area = input("enter your complaint here:")
        status = input("SOLVED/PENDING ?:")
        add_image = input("Do you want to attach any image of the scene? (y/n): ").lower()

        image_path = None
        img_hash = None

        if add_image == 'y':
            image_path = input("Enter your image's file path: ").strip()
            
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img_hash = str(imagehash.average_hash(img))
                cursor.execute("select u_id FROM user__complaints where img-_hash = %s", (img_hash,))
                if cursor.fetchone():
                    print("Duplicate image is detected! Complaint cannot be filed, SORRY")
                    return
            else:
                print("File can't reach. You can continue without image.")
                image_path = None


        cursor.execute("insert into user__complaints(name, location, complaint_area, status, add_image)values(%s,%s,%s,%s,%s)", (name, location, complaint_area, status, add_image))
        conn.commit()
        print("Your Complaint is filed successfully,Thank you!")

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

user_complaints()



