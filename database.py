import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

def save_prediction(text: str, predicted_class: str, inference_time: float):
    
    with psycopg.connect(host=host,
                        port=port,
                        dbname=dbname,
                        user=user,
                        password=password
                        ) as conn:

        query = """
        INSERT INTO predictions (text, predicted_class, inference_time_ms)
        VALUES (%s, %s, %s);
        """
        conn.execute(query, (text, predicted_class, inference_time))
