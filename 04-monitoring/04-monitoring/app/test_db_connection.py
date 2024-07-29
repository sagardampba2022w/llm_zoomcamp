import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST', 'postgres'),
    database=os.getenv('POSTGRES_DB', 'course_assistant'),
    user=os.getenv('POSTGRES_USER', 'your_username'),
    password=os.getenv('POSTGRES_PASSWORD', 'your_password'),
    port=os.getenv('POSTGRES_PORT', 5432)
)
print("Connection successful")
