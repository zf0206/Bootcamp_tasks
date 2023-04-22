import sqlite3
import random as rd

# define relevant functions

# view all records in the table
def view_all():
    cursor.execute('''
            SELECT * FROM books''')
    data = cursor.fetchall()
    print(data)

# check information in book
def check_book():
    id_check = int(input("Please enter book ID you'd like to check: "))
    cursor.execute('''
                SELECT * FROM books WHERE book_id = ?''', (id_check,))
    data = cursor.fetchone()
    print('Please find your book information below:\n ', data)

# when adding a book 
def add_book():
    print('Please enter the following information:')
    
    while True:
        # randomly generate a book ID
        id = rd.randint(3006, 9999)
        #id = int(input('Book ID(3006-9999 range): '))
        # check if this id is already existed in the table
        # if exists, keep running the loop to generate a new ID
        # if not, asking for rest inputs of book information and add to the table
        cursor.execute('SELECT rowid FROM books WHERE book_id = ?', (id,))
        data = cursor.fetchall()      
        if len(data) != 0:
            continue
        else:
            break
    title = input('Book title: ')
    author = input('Book author: ')
    qty = input('Book quantity: ')
    cursor.execute('''INSERT INTO books VALUES(?, ?, ?, ?)''', (id, title, author, qty ))
    print('New book added!')
    db.commit()

# update book information
def update_book():
    # call view_all () function to view all the books
    view_all()
    # request input about which book and what the user want to edit
    # it is assumed in the dataset book ID is set up by the system and cannot be edited
    id_select = int(input('Select the ID of the book you would like to edit: '))
    edit_item = input('What would you like to edit? Choose from (title, author, qty):\n')
    # if user want to edit title
    if edit_item == 'title':
        new_title = str(input('Please enter new title of the book:\n'))
        cursor.execute('''
                    UPDATE books SET title = ? WHERE book_id = ?''', (new_title, id_select,))
        print('Book title updated!')
    #if user want to edit author
    elif edit_item == 'author':
        new_author = str(input('Please enter new author of the book:\n'))
        cursor.execute('''
                    UPDATA books SET author = ? WHERE book_id = ?''', (new_author, id_select,))
        print('Book author updated!')
    # if user want to edit quantity
    else:
        new_qty = int(input('Please enter new quantity number for the took:\n'))
        cursor.execute('''
                    UPDATE books SET qty = ? WHERE book_id = ?''', (new_qty, id_select,))
        print('Book quantity updated!')
    db.commit()


# delet a book
def del_book():
    # call view_all () function to view all the books
    view_all()
    # ask user which book they want to delet
    id_select = int(input('Select the ID of the book you would like to delete: '))
    cursor.execute('''
                DELETE FROM books WHERE book_id = ?
                ''', (id_select,))
    print('Book deleted!')
    db.commit()

# create a database ebookstore if nto exists already
db = sqlite3.connect('ebookstore')
cursor = db.cursor()

# as the code will be running again for review purpose
# this line is added to avoid any 'Error' when running repeatly
# this may not be applicable in real applications 
cursor.execute('''DROP TABLE IF EXISTS books''')
cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (book_id INT PRIMARY KEY, title VARCHAR(40), author VARCHAR(30), qty INT)
            ''')
print("database named 'ebookstore' created!")

# save book information into the table named 'books'
table_data = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
            (3002, 'Harry Potter and the Philosopher \'s Stone', 'J.K. Rowling', 40),
            (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
            (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
            (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]
cursor.executemany('''
            INSERT INTO books VALUES(?, ?, ?, ?)''', table_data)
db.commit()

# Ask user what they want to do about the table
while True:
    selection = int(input('''You have options here::\n
        1 - Enter book
        2 - Update book
        3 - Delete book
        4 - Search book
        0 - Exit
        Please input relevant number of your choice(1, 2, 3, 4, 0):\n'''))
    if selection == 1:
        add_book()
    elif selection == 2:
        update_book()
    elif selection == 3:
        del_book()
    elif selection == 4:
        check_book()
    else:
        break
db.commit()
db.close()
print('Connection to database closed')




