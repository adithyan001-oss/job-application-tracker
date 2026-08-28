import mysql.connector
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def get_connection(database=True):
    config={"host":DB_HOST,"port":DB_PORT,"user":DB_USER,"password":DB_PASSWORD}
    if database:
        config["database"]=DB_NAME
    return mysql.connector.connect(**config)

def initialize_database():
    conn=get_connection(False)
    cur=conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    cur.close(); conn.close()

    conn=get_connection()
    cur=conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INT AUTO_INCREMENT PRIMARY KEY,
            company VARCHAR(100) NOT NULL,
            role VARCHAR(150) NOT NULL,
            location VARCHAR(100),
            application_date DATE NOT NULL,
            status VARCHAR(30) NOT NULL DEFAULT 'Applied',
            source VARCHAR(100),
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close(); conn.close()
