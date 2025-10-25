import psycopg2

def connection():
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="admin",
        database="management"
    )
