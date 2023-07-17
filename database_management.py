```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('exec_assistant_app.db') # create a database connection to a SQLite database
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"exec_assistant_app.db"

    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        deadline text,
                                        progress text,
                                        delegate text
                                    ); """

    sql_create_expenses_table = """ CREATE TABLE IF NOT EXISTS expenses (
                                        id integer PRIMARY KEY,
                                        receipt text NOT NULL,
                                        category text,
                                        approval text
                                    ); """

    sql_create_events_table = """ CREATE TABLE IF NOT EXISTS events (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        date text,
                                        location text,
                                        invitees text
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_tasks_table)
        create_table(conn, sql_create_expenses_table)
        create_table(conn, sql_create_events_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```