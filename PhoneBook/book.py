import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="StopDomesticViolence"
)

cur = conn.cursor()

def inputData():
    name = input("Please enter the person's name: ")
    number = input("Please enter the phone number: ")
    cur.execute('INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES(%s, %s);', (name, number))

def importFromCSV():
    filepath = r'C:\Users\ADMIN\OneDrive\Рабочий стол\azamat\lab10\fil.csv'
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES(%s, %s);', (personName, phoneNumber))

def update_contact(personName, phoneNumber):
    cur.execute('UPDATE postgres.public.phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s;', (phoneNumber, personName))

def queryData():
    cur.execute('SELECT * FROM postgres.public.phone_book')
    data = cur.fetchall()
    path = r"C:\Users\ADMIN\OneDrive\Рабочий стол\azamat\lab10\a.txt"
    with open(path, "w") as f:
        for row in data:
            f.write("Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")

def deleteData():
    personName = input("Please enter the name of the contact you want to delete: ")
    cur.execute(f'DELETE FROM postgres.public.phone_book WHERE "PersonName" = \'{personName}\';')

def deleteAllData():
    cur.execute('DELETE FROM postgres.public.phone_book;')

done = False
while not done:
    print("""
    What would you like to do?
    1. Input a new contact
    2. Import contacts from a CSV file
    3. Update an existing contact
    4. Query all contacts and save to a file
    5. Delete a contact by name
    6. Delete all contacts
    7. Exit
    """)
    try:
        choice = int(input("Please enter the number of your choice (1-7): "))
        
        if choice == 1:
            inputData()
        elif choice == 2:
            importFromCSV()
        elif choice == 3:
            name = input("Please enter the name of the contact you want to update: ")
            newNumber = input("Please enter the new phone number: ")
            update_contact(name, newNumber)
        elif choice == 4:
            queryData()
        elif choice == 5:
            deleteData()
        elif choice == 6:
            deleteAllData()
        elif choice == 7:
            done = True
        conn.commit()
    except ValueError:
        print("Please enter a valid number (1-7).")

cur.close()
conn.close()
