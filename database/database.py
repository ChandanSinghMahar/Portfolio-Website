import psycopg
import os
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg.connect(DATABASE_URL)

def load_projects_from_db():
    conn = get_connection()

    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM projects ORDER BY id ASC")
        projects = cur.fetchall()
        return projects