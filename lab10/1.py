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
    with open(filename, 'lab10/list.csv') as file:
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

# Example usage
#insert_from_csv("list.csv")
# insert_from_console()
#update_data("Saniya", new_phone="9876543210")
#query_data("Nan")
delete_data("Beka")
insert_from_console()  # Call the function to prompt user for input

# Close the cursor and connection
cur.close()
conn.close()
