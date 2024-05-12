
""" The following program will use sqlite to read form books.db database
1. The database will be populated with the ebooks table.
2. Create functions for the following menu options;
< Add a book
< Update a book
< Search for a book
< Delete a book
"""

import sqlite3
from tabulate import tabulate

try:
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
except Exception as e:
    print("Error connecting to database")
finally:
    print("Connected to database")


def create_table():
    """ Creating our table for Ebooks"""
    # Connecting to database and creating a cursor
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebooks(id INTEGER PRIMARY KEY,Title TEXT,
                   	Author TEXT, Qty INTEGER)
''')
    # Commit execute function and closing database
    db.commit()
    db.close()



# List of books to be added to database
books = [
    (3001,'A tale of two cities','Charles Dickens', 30),
    (3002,'Harry Potter and the Philosophers Stone','J.K.Rowling', 40),
    (3003,'The Lion the Witch and the Wardrobe','C.S.Lewis', 21),
    (3004,'The Lord of the Rings','J.R.R. Tolkien', 37),
    (3005,'Alice in Wonderland','Lewis Caroll', 12),
    (3006,'Pillars of the Earth','Ken Follet', 25)]


def populate_table():
    """Filling our Ebooks table with our books list of values"""
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.executemany("INSERT OR REPLACE INTO ebooks VALUES (?,?,?,?)", books)
    db.commit()
    db.close()


def read_data():
    '''This will read the table in the database and display in an easy-to-read
    manner'''
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    data = cursor.execute("SELECT * FROM ebooks")
    data = cursor.fetchall()
    
    headers = [i[0] for i in cursor.description]  # Extract column names as headers
    
    print(tabulate(data, headers=headers, tablefmt="grid"))  
    
    db.commit()
    db.close()


def add_book(id,title,author,qty):
    """When the user wants to add another book to Ebooks table"""
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO ebooks VALUES (?,?,?,?)",
                   (id,title,author,qty),)
    rows = cursor.fetchall()
    print(f"ID {id} and Title {title} added to database")
    for row in rows:
        print(row)
   

    db.commit()
    db.close()


def delete_records(id):
    """When the user wants to delete a book from Ebooks table"""
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute("DELETE FROM ebooks WHERE id=(?)", (id,))
    row = cursor.fetchone()
    print(f"Deleting info for Book with ID: {id}")
    print(row)

    db.commit()
    db.close()


def search_books(id):
    """The user enters the book id to search for a book"""
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ebooks WHERE id = (?)", (id,))
    rows = cursor.fetchall()
    print(f"Displaying info for ID: {id}")
    for row in rows:
        print(row)

    db.commit()
    db.close()


def update_book(id, qty, title, author):
    """Update the quantity, title, and author of a book in Ebooks table"""
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute("UPDATE ebooks SET Qty=?, Title=?, Author=? WHERE id=?",
                   (qty, title, author, id))
    db.commit()
    db.close()
    print(f"""For Book ID: {id}, the new quantity is: {qty}, the new title is:
        {title}, and the new author is: {author}""")



print("=" * 100)
print("Welcome to 'READ-A-WHILE' Books")
print()
while True:
    try:
        menu = int(input('========== MENU OPTIONS ==========\n'
                         '1 - Add Book to Database\n'
                         '2 - Update Book\n'
                         '3 - Search Book\n'
                         '4 - Delete Book from Database\n'
                         '0 - Exit Menu\n'))
    except ValueError:
        print("Please enter only the NUMBER from the MENU options, thank you")
        print()
        continue

    if menu == 1:
        try:
            id = int(input('Enter Book ID:\n'))
            qty = int(input('Enter quantity received of this book\n'))
        except ValueError:
            print("Enter only numbers for ID and Quantity")
            print()
            continue
        title = input('Enter Book Title\n').title()
        author = input('Enter Book Author\n').title()
        add_book(id, title, author, qty)
        
    elif menu == 2:
        read_data()
        try:
            id = int(input('Enter ID to update book\n'))
            qty = int(input('Enter new quantity \n'))
        except ValueError:
            print("Enter the correct NUMBERS for ID and Quantity")
            print()
            continue
        title = input('Enter Book Title\n').title()
        author = input('Enter Book Author\n').title()
        update_book(id, qty, title, author)
        
    elif menu == 3:
        read_data()
        try:
            id = int(input('Enter Book ID to search for a Book\n'))
        except ValueError:
            print("Enter the correct NUMBER for Book ID")
            print()
            continue
        search_books(id)
        
    elif menu == 4:
        read_data()
        try:
            id = int(input('Enter Book ID to delete a Book\n'))
        except ValueError:
            print("Enter the correct NUMBER for Book ID")
            print()
            continue
        delete_records(id)
        
    elif menu == 0:
        print("Thank you for using  'READ-A-WHILE' Books")
        print()
        print('=' * 15 + 'HAPPY READING!!' + '=' * 15)
        print()
        break
    else:
        print('Please Enter a valid MENU option')
        print()
        continue

