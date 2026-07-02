import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="futbet",
        user="postgres",
        password="senha123", 
        host="localhost"
    )