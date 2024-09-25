import sqlite3
from data_dict import random_users

# Function to create a member in the database
def create_member(data):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, first_name TEXT)')
        cur.execute("INSERT INTO members (id, first_name) VALUES (?, ?)", (data['id'], data['first_name']))
        conn.commit()

# Function to get all members from the database
def get_all_members():
    members = []
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM students')
        for i in cur.fetchall():
            members.append({'id': i[0], 'name': i[1]})
    return members

