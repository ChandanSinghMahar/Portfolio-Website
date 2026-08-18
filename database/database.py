import psycopg
import os
from psycopg.rows import dict_row
from dotenv import load_dotenv
from sqlalchemy import text

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

def load_project_from_db(id):
    conn = get_connection()
    
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM projects WHERE id = %s", (id,))
        rows = cur.fetchall()
        if len(rows) == 0:
            return None
        else:
            return rows[0]
        
def add_application_to_db(project_id, data):
    conn = get_connection()
    with conn.cursor() as cur:
        query = """INSERT INTO applications (project_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(%s, %s, %s, %s, %s, %s, %s) """
        cur.execute(query, (project_id, 
                            data['full_name'], 
                            data['email'], 
                            data['linkedin_url'],
                            data['education'],
                            data['work_experience'],
                            data['resume_url']
                            ))
    conn.commit() 