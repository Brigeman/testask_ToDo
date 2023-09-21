import psycopg2
from psycopg2 import sql
import configparser

def connect_to_database():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Указываем путь к вашему конфигурационному файлу
    db_config = config['database']

    conn = psycopg2.connect(
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )
    return conn

def add_task(task_text):
    conn = connect_to_database()
    cur = conn.cursor()
    insert_query = sql.SQL("INSERT INTO tasks (task_text) VALUES ({})").format(sql.Literal(task_text))
    cur.execute(insert_query)
    conn.commit()
    conn.close()

def get_tasks():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY id")
    tasks = cur.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = connect_to_database()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        print(f"Задача с ID {task_id} успешно удалена")
    except psycopg2.Error as e:
        print("Ошибка при удалении задачи:", e)
    finally:
        cur.close()
        conn.close()

