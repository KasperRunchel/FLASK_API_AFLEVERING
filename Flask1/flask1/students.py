import sqlite3
from data_dict import random_users

def create_database():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)')
        cur.execute("INSERT INTO students VALUES (1, 'Claus')")
        cur.execute("INSERT INTO students VALUES (2, 'Torben')")
        cur.execute("INSERT INTO students VALUES (3, 'Anna')")

def read():
    students = []

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM students')

        for i in cur.fetchall():
            students.append({'id' : i[0], 'name' : i[1]})

    return students


def create_school():
    with sqlite3.connect('school.db') as conn:
        cur = conn.cursor()
        # Create the members table with all necessary fields
        cur.execute('''CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY, 
                        first_name TEXT, 
                        last_name TEXT, 
                        birth_date TEXT, 
                        gender TEXT, 
                        email TEXT, 
                        phonenumber TEXT, 
                        address TEXT, 
                        nationality TEXT, 
                        active BOOLEAN, 
                        github_username TEXT
                      )''')

        # Generate 10 random users
        random_users
        
        # Convert the random user dictionaries into tuples for database insertion
        user_data = [(user['id'], user['first_name'], user['last_name'], user['birth_date'], user['gender'], 
                      user['email'], user['phonenumber'], user['address'], user['nationality'], 
                      user['active'], user['github_username']) for user in random_users]
        
        # Insert the random users into the members table
        cur.executemany('''INSERT INTO members 
                            (id, first_name, last_name, birth_date, gender, email, phonenumber, address, nationality, active, github_username) 
                            VALUES (?,?,?,?,?,?,?,?,?,?,?)''', user_data)

create_database()
create_school()


