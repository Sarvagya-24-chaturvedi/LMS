import mysql.connector as a

# Connect to MySQL
con = a.connect (host='localhost',user='root',passwd='*******',database='library')

# Create a cursor object to interact with the database
c = con.cursor()

def addbook():
    # Add a new book to the library
    bn = input('Enter  BOOK Name : ')
    c = input('Enter BOOK Code : ')
    t = input('Total Books : ')
    s = input('Enter Subject : ')
    data = (bn,c,t,s)
    # Insert the book into the database
    sql = 'insert into book values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print('>——————————————————————————————–<')
    print('Data Entered Successfully')
    main()
        
def issuebook():
    # Issue a book from the library
    n = input('Enter Name : ')
    r = input('Enter Reg No : ')
    co = input('Enter Book Code : ')
    d = input('Enter Date : ')
    a = 'insert into issuebook values(%s,%s,%s,%s)'
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print('>——————————————————————————————–<')
    print('Book issued to : ',n)
    main()

def submitbook():
    # Submit the issued book to the library
    n = input('Enter Name : ')
    r = input('Enter Reg No : ')
    co = input('Enter Book Code : ')
    d = input('Enter Date : ')
    a = 'insert into submitbook values(%s,%s,%s,%s)'
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print('>——————————————————————————————–<')
    print('Book Submitted from : ',n)
    main()
    
def bookup():
    # Update the quantity of a book in the library
    book_code = int(input("Enter the BOOK CODE of the book to update: "))
    new_quantity = int(input("Enter the new quantity: "))

    # Update the book quantity in the database
    c.execute("UPDATE book SET total = %s WHERE bcode = %s", (new_quantity, book_code))
    con.commit()
    print('>——————————————————————————————–<')
    print("Book quantity updated successfully!")
    main()
    
def dbook():
    # Delete a book from the library
    ac = input('Enter Book Code : ')
    a = 'delete from book where BCODE = %s'
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print('>——————————————————————————————–<')
    print('Data Deleted Successfully')
    main()

def dispbook():
    # Display all the books in the library
    a = 'select * from book'
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:   
        print('Book Name : ',i[0])
        print('Book Code : ',i[1])
        print('Total : ',i[2])
        print('Subject : ',i[3])
        print('>——————————–<')
    main()
    
def issuestatus():
    # Display all the books issued by the library
    a = 'select * from issuebook'
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:   
        print('Name : ',i[0])
        print('Registration no. : ',i[1])
        print('Book Code : ',i[2])
        print('Issue date : ',i[3])
        print('>——————————–<')
    main()
    
def submitstatus():
    # Display all the books submitted to the library
    a = 'select * from submitbook'
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:   
        print('Name : ',i[0])
        print('Registration no. : ',i[1])
        print('Book Code : ',i[2])
        print('Issue date : ',i[3])
        print('>——————————–<')
    main()

# Main menu    
def main():
    print('''

                                    LIBRARY MANAGER

    1. ADD BOOK
    2. ISSUE BOOK
    3. SUBMIT BOOK
    4. UPDATE TOTAL QUANTITY
    5. DELETE BOOK
    6. DISPLAY BOOKS
    7. ISSUE STATUS
    8. SUBMIT STATUS
    ''')

    choice = input('Enter Task No : ')

    print('>——————————————————————————————–<')
    if (choice == '1'):
        addbook()

    elif (choice=='2'):
        issuebook()

    elif (choice=='3'):
        submitbook()

    elif (choice=='4'):
        bookup()

    elif (choice=='5'):
        dbook()

    elif (choice=='6'):
        dispbook()
        
    elif (choice=='7'):
        issuestatus()
        
    elif (choice=='8'):
        submitstatus()

    else :

        print(' Wrong choice……….')

        main()

# Password protection
def pswd():
        ps = input('Enter Password : ')
        if ps == '*******':
                main()

        else:
                print('Wrong Password')
                pswd()
pswd()
