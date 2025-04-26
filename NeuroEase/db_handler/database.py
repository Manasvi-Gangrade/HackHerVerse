import sqlite3
from config.config import Config

def create_db():
    conn = sqlite3.connect(Config.DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, mood TEXT)''')
    conn.commit()
    conn.close()

def save_task(task, mood):
    conn = sqlite3.connect(Config.DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, mood) VALUES (?, ?)", (task, mood))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(Config.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks
