import psycopg2
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="sanman8070",
    host="localhost",
    port=5433
)
cur = conn.cursor()

# Create PhoneBook table if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS PhoneBook (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE,
                phone VARCHAR(15)
            )''')
conn.commit()

# Function to insert data from CSV file
def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()

# Function to insert data from console
def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()

# Function to update data
def update_data(username, new_username=None, new_phone=None):
    if new_username:
        cur.execute("UPDATE PhoneBook SET username = %s WHERE username = %s", (new_username, username))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (new_phone, username))
    conn.commit()

# Function to query data
def query_data(filter_option=None):
    if filter_option:
        cur.execute("SELECT * FROM PhoneBook WHERE username LIKE %s OR phone LIKE %s", (filter_option, filter_option))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Function to delete data
def delete_data(username):
    cur.execute("DELETE FROM PhoneBook WHERE username = %s", (username,))
    conn.commit()

# Function to return all records based on a pattern
def search_records(pattern):
    cur.execute("SELECT * FROM PhoneBook WHERE username LIKE %s OR phone LIKE %s", (pattern, pattern))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Procedure to insert or update user
def insert_or_update_user(username, phone):
    cur.execute("SELECT * FROM PhoneBook WHERE username = %s", (username,))
    if cur.fetchone():
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (phone, username))
    else:
        cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()

# Procedure to insert many new users by list of names and phones
def insert_many_users(data):
    incorrect_data = []
    for item in data:
        username, phone = item
        if not phone.isdigit() or len(phone) != 10:
            incorrect_data.append((username, phone))
            continue
        cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    return incorrect_data

# Function to query data with pagination
def query_with_pagination(limit, offset):
    cur.execute("SELECT * FROM PhoneBook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Procedure to delete data from tables by username or phone
def delete_data_by_username_or_phone(username=None, phone=None):
    if username:
        cur.execute("DELETE FROM PhoneBook WHERE username = %s", (username,))
    elif phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()

# Example usage
# insert_from_csv("data.csv")
insert_from_console()
# update_data("John", new_phone="9876543210")
# query_data("John")
# delete_data("John")
#search_records("John")
insert_or_update_user("John", "1234567890")
# incorrect_data = insert_many_users([("John", "1234567890"), ("Jane", "9876"), ("Alice", "1234567890")])
# query_with_pagination(10, 0)
# delete_data_by_username_or_phone(username="John")
# delete_data_by_username_or_phone(phone="1234567890")

# Close the cursor and connection
cur.close()
conn.close()
