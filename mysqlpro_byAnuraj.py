from tabulate import tabulate
import mysql.connector
hoe=str(input("enter host name i.e if localhost or anyother : "))
usero=str(input('Enter username i.e if root , admin or something else  : '))
paass=str(input('Enter password : '))
databae=str(input('Enter the database name that you want to create or use :  '))
mydb = mysql.connector.connect(host=hoe,
                               user=usero,
                               password=paass,
                               database=databae)
cur = mydb.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS admin')
cur.execute('CREATE TABLE IF NOT EXISTS admin_log(id varchar(50) primary key not null,name varchar(50) not null,password varchar(6) not null)')
cur.execute('CREATE TABLE IF NOT EXISTS book(id int unique not null,name varchar(50) not null,price int not null)')
cur.execute('CREATE TABLE IF NOT EXISTS issue(id int unique not null,name varchar(50) not null,DATE varchar(100) not null,b_name varchar(45) not null)')
cur.execute('CREATE TABLE IF NOT EXISTS lib_log(id int  primary key not null,name varchar(50) not null,password varchar(50) not null)')
cur.execute('CREATE TABLE IF NOT EXISTS stu_log(id int primary key not null,name varchar(50) not null,password varchar(6) not null)')
def lib_check(f):
    s = "select * from lib_log"
    cur.execute(s)
    r = cur.fetchall()
    for x in r:
        if x[0] == f[0]:
            return True
            break
        else:
            continue
            return False


def admin_check(f):
    s = "select * from admin_log"
    cur.execute(s)
    r = cur.fetchall()
    for x in r:
        if x == f:
            return True
            break
        else:
            continue
            return False


def stu_check(f):
    s = "select * from stu_log"
    cur.execute(s)
    r = cur.fetchall()
    for x in r:
        if x == f:
            return True
            break
        else:
            continue
            return False


def search_insert(f):
    s = "select * from book"
    cur.execute(s)
    r = cur.fetchall()
    r = list(r)
    for x in r:
        if x[0] == f:
            return True
            break
        else:
            continue
            return False


def issue_check(f):
    s = "select * from issue"
    cur.execute(s)
    r = cur.fetchall()
    r = list(r)
    for x in r:
        if x[0] == f:
            return True
            break
        else:
            continue
            return False


def search_book(f):
    s = "select * from book"
    cur.execute(s)
    r = cur.fetchall()
    r = list(r)
    for x in r:
        if x[1] == f:
            return True
            break
        else:
            continue
            return False
lol = "y"
while lol == 'y' :
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("||  Type  login   ||")
  print("||  Type register (only for students) ||")
  print("||  Type exit  ||")
  task = input("Enter the task name")

  if task == 'login':
    print("Login as Admin...?")
    print("Login as Librarian...?")
    print("Login as Student...?")
    task = input("Enter your designation ")
    if task == "Admin":
        a = input("Enter your admin ID")
        b = input("Enter your name")
        c = input("Enter your passowrd")
        d = (a, b, c)
        if admin_check(d):
            con = 'y'
            while con == 'y':
                print("~~~~~~~~~~~~~~~~~~~WELCOME ADMIN~~~~~~~~~~~~~~~~~~~")
                print("1. Insert New Book")
                print("2. View All Book")
                print("3. Search a Book")
                print("4. Issuing a Book")
                print("5. To view whole issue list")
                print("6. Delete Book")
                print("7. Update Book Price")
                print("8. Deleting Names from issuing database")
                print("9. View all liberian list")
                print("10.View all student list")
                print("11. Add/remove Librarian")
                print("12. Add/remove student")
                print("13. Exit Program")
                a = input("Enter the task number")

                if a == "1":
                    z = "INSERT INTO book(id , name , price)Values(%s,%s,%s)"
                    n = input("enter the Book name")
                    try:
                        i = int(input("enter the unique book Id"))
                        if search_insert(i):
                            print("this book already exist")
                        else:
                            p = input("Enter the book price")
                            b = (i, n, p)
                            cur.execute(z, b)
                            mydb.commit()
                            print("book inserted")
                    except ValueError:
                        print("please enter correct data try again")

                elif a == "2":
                    z = ["ID","Book_Name","Price"]
                    s = "select * from book"
                    cur.execute(s)
                    l=[]
                    result = cur.fetchall()
                    for x in result :
                       l.append(list(x))
                    l.insert(0,z)
                    print(tabulate(l,headers="firstrow" ,tablefmt="psql"))

                elif a == "3":
                    f = input("enter the book name you want to search")
                    s = "select * from book"
                    cur.execute(s)
                    r = cur.fetchall()
                    r = list(r)
                    try:
                        for x in r:
                            if x[1] == f:
                                z = x
                        l=[["ID", "Book_Name", "Price"]]
                        l.append(list(z))
                        print(tabulate(l, headers="firstrow", tablefmt="psql"))

                    except NameError:
                        print("That book isn't available")

                elif a == "4":
                    a = input("enter the book you want to issue")
                    if search_book(a):
                        try:
                            s = "INSERT INTO issue(id , name , date ,b_name)Values(%s,%s,%s,%s)"
                            i = int(input("enter your student Id"))
                            if issue_check(i):
                                print("You have already issued a book!")
                            else:
                                n = input("enter the your name")
                                d = input("enter the date in yyyy-mm-dd format")
                                b = (i, n, d, a)
                                cur.execute(s, b)
                                mydb.commit()
                                print("Book Issued !")

                        except ValueError:
                            print("please enter data correctly")
                    else:
                        print("That book isnt availabe")
                elif a == "5":
                    z=["ID","Name","Date","Book name"]
                    s = "select * from issue"
                    cur.execute(s)
                    l = []
                    result = cur.fetchall()
                    for x in result:
                        l.append(list(x))
                    l.insert(0, z)
                    print(tabulate(l, headers="firstrow", tablefmt="psql"))
                elif a == "6":
                    a = input("Enter the book name which you want to delete")
                    b = (a,)
                    s = "delete from book where name = %s"
                    cur.execute(s, b)
                    mydb.commit()
                    print("Book deleted")

                elif a == "7":
                    x = 'y'
                    while x == 'y':
                        a = int(input("enter amount to update "))
                        b = input("enter the book name you want to increase/decrease price")
                        if search_book(b):
                            s = 'update book set price=price+%s where name = %s'
                            c = (a, b)
                            cur.execute(s, c)
                            mydb.commit()
                            print("book price updated")
                            x = input("enter y to continue.....")
                        else:
                            print("That book doesnt exist")
                elif a == "8":
                    x = 'y'
                    while x == 'y':
                        a = int(input("Enter the ID which you want to delete from issuing list"))
                        b = (a,)
                        s = "delete from issue where id = %s"
                        cur.execute(s, b)
                        mydb.commit()
                        print("deleted!")
                        x = input("enter the y to continue..")
                elif  a == "9" :
                    z = ["ID","Lib_Name","Password"]
                    s = "select * from lib_log"
                    cur.execute(s)
                    l = []
                    result = cur.fetchall()
                    for x in result:
                        l.append(list(x))
                    l.insert(0, z)
                    print(tabulate(l, headers="firstrow", tablefmt="psql"))
                elif a== "10" :
                    z = ["ID","Stu_Name","Password"]
                    s = "select * from stu_log"
                    cur.execute(s)
                    l = []
                    result = cur.fetchall()
                    for x in result:
                        l.append(list(x))
                    l.insert(0, z)
                    print(tabulate(l, headers="firstrow", tablefmt="psql"))
                elif a == "11":
                    a = input("Enter your Lib ID")
                    b = input("Enter your name")
                    c = input("Enter your passowrd")
                    d = (int(a), b, c)
                    print("add or remove????")
                    v = input("enter the task name")
                    if v == 'remove':
                        if lib_check(d):
                            z = (b,)
                            s = "delete from lib_log where name = %s"
                            cur.execute(s, z)
                            mydb.commit()
                            print("removed")
                        else:
                            print("That ID doesn't exist ")
                    if v == 'add':
                        if lib_check(d):
                            print("That ID already exist")
                        else:
                            s = "INSERT INTO lib_log(ID , name , password )Values(%s,%s,%s)"
                            cur.execute(s, d)
                            mydb.commit()
                            print("ID created!")
                elif a == "12":
                    a = input("Enter your student ID")
                    b = input("Enter your name")
                    c = input("Enter your passowrd")
                    d = (int(a), b, c)
                    print("add or remove????")
                    v = input("enter the task name")
                    if v == 'remove':
                        if stu_check(d):
                            z = (b,)
                            s = "delete from stu_log where name = %s"
                            cur.execute(s, z)
                            mydb.commit()
                            print("removed")
                        else:
                            print("That ID doesn't exist ")
                    elif v == 'add':
                        if stu_check(d):
                            print("That ID already exist")
                        else:
                            s = "INSERT INTO stu_log(id , name , password )Values(%s,%s,%s)"
                            cur.execute(s, d)
                            mydb.commit()
                            print("ID created!")
                    else:
                        print("entered data is invalid")
                        continue
                elif a == "13":
                    con = input("press any key except y to exit")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Exiting~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("you entered wrong number try again!")
                    continue

        else:
            print("Your entered data is not correct , access denied!")
    elif task == "Librarian":
        a = input("Enter your Lib ID")
        b = input("Enter your name")
        c = input("Enter your passowrd")
        d = (int(a), b, c)
        if lib_check(d):
            con = 'y'
            while con == 'y':
                print(
                    "```````````````````````````````````````````````Welcome Librarian```````````````````````````````````````````````")
                print("1. Insert New Book")
                print("2. View All Book")
                print("3. Search a Book")
                print("4. Issuing a Book")
                print("5. To view whole issue list")
                print("6. Delete Book")
                print("7. Update Book Price")
                print("8. Deleting Names from issuing database")
                print("9. Exit Program")
                a = input("Enter the task number")

                if a == "1":
                    z = "INSERT INTO book(id , name , price)Values(%s,%s,%s)"
                    n = input("enter the Book name")
                    try:
                        i = int(input("enter the unique book Id"))
                        if search_insert(i):
                            print("this book already exist")
                        else:
                            p = input("Enter the book price")
                            b = (i, n, p)
                            cur.execute(z, b)
                            mydb.commit()
                            print("book inserted")
                    except ValueError:
                        print("please enter correct data try again")

                elif a == "2":
                    z = ["ID", "Book_Name", "Price"]
                    s = "select * from book"
                    cur.execute(s)
                    l = []
                    result = cur.fetchall()
                    for x in result:
                        l.append(list(x))
                    l.insert(0, z)
                    print(tabulate(l, headers="firstrow", tablefmt="psql"))

                elif a == "3":
                    f = input("enter the book name you want to search")
                    s = "select * from book"
                    cur.execute(s)
                    r = cur.fetchall()
                    r = list(r)
                    try:
                        for x in r:
                            if x[1] == f:
                                z = x
                        l = [["ID", "Book_Name", "Price"]]
                        l.append(list(z))
                        print(tabulate(l, headers="firstrow", tablefmt="psql"))

                    except NameError:
                        print("That book isn't available")

                elif a == "4":
                    a = input("enter the book you want to issue")
                    if search_book(a):
                        try:
                            s = "INSERT INTO issue(id , name , date ,b_name)Values(%s,%s,%s,%s)"
                            i = int(input("enter your student Id"))
                            if issue_check(i):
                                print("You have already issued a book!")
                            else:
                                n = input("enter the your name")
                                d = input("enter the date in yyyy-mm-dd format")
                                b = (i, n, d, a)
                                cur.execute(s, b)
                                mydb.commit()
                                print("Book Issued !")

                        except ValueError:
                            print("please enter data correctly")
                    else:
                        print("That book isnt availabe")
                elif a == "5":
                    z = ["ID", "Name", "Date", "Book name"]
                    s = "select * from issue"
                    cur.execute(s)
                    l = []
                    result = cur.fetchall()
                    for x in result:
                        l.append(list(x))
                    l.insert(0, z)
                    print(tabulate(l, headers="firstrow", tablefmt="psql"))
                elif a == "6":
                    a = input("Enter the book name which you want to delete")
                    b = (a,)
                    s = "delete from book where name = %s"
                    cur.execute(s, b)
                    mydb.commit()
                    print("Book deleted")

                elif a == "7":
                    x = 'y'
                    while x == 'y':
                        a = int(input("enter amount to update "))
                        b = input("enter the book name you want to increase/decrease price")
                        if search_book(b):
                            s = 'update book set price=price+%s where name = %s'
                            c = (a, b)
                            cur.execute(s, c)
                            mydb.commit()
                            print("book price updated")
                            x = input("enter y to continue.....")
                        else:
                            print("That book doesnt exist")
                elif a == "8":
                    x = 'y'
                    while x == 'y':
                        a = input("Enter the name which you want to delete from issuing list")
                        b = (a,)
                        s = "delete from issue where name = %s"
                        cur.execute(s, b)
                        mydb.commit()
                        x = input("enter the y to continue..")

                elif a == "9":
                    con = input("press any key except y to exit")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Exiting~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("You're entering wrong data please try again")
                    continue
        else:
            print("Your entered data is not correct , access denied!")

    elif task == "Student":
        id_ = input("Enter your student ID")
        nm = input("Enter your name")
        p = input("Enter your passowrd")
        d = (int(id_), nm, p)
        if stu_check(d):
            con = 'y'
            while con == "y":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome Student~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("1. See book list")
                print("2. Search a book")
                print("3. Check if you have issued a book")
                print("4. Issue a book")
                print("5. Exit ")
                a = input("Enter the task number")
                if a == "1":
                    z = ["ID", "Book_Name", "Price"]
                    s = "select * from book"
                    cur.execute(s)
                    l = []
                    result = cur.fetchall()
                    for x in result:
                        l.append(list(x))
                    l.insert(0, z)
                    print(tabulate(l, headers="firstrow", tablefmt="psql"))
                elif a == "2":
                    f = input("enter the book name you want to search")
                    s = "select * from book"
                    cur.execute(s)
                    r = cur.fetchall()
                    r = list(r)
                    try:
                        for x in r:
                            if x[1] == f:
                                z = x
                        l = [["ID", "Book_Name", "Price"]]
                        l.append(list(z))
                        print(tabulate(l, headers="firstrow", tablefmt="psql"))

                    except NameError:
                        print("That book isn't available")
                elif a == "3":
                    s = "select * from issue"
                    cur.execute(s)
                    r = cur.fetchall()
                    r = list(r)
                    for x in r:
                        if x[0] == int(id_):
                            l = [["Stu_ID","Stu_Name","Date","Book_Name"]]
                            l.append(list(x))
                            print(tabulate(l, headers="firstrow", tablefmt="psql"))
                            break
                        else:
                            continue
                            print("You havent issed any book")
                elif a == "4":
                    a = input("enter the book you want to issue")
                    if search_book(a):
                        try:
                            s = "INSERT INTO issue(id , name , date ,b_name)Values(%s,%s,%s,%s)"
                            if issue_check(int(id_)):
                                print("You have already issued a book!")
                            else:
                                d = input("enter the date in yyyy-mm-dd format")
                                b = (int(id_), nm, d, a)
                                cur.execute(s, b)
                                mydb.commit()
                                print("Book Issued !")

                        except ValueError:
                            print("please enter data correctly")
                    else:
                        print("That book isnt availabe")
                elif a == "5":
                    con = "exit"
                    print("Exiting......")
                else:
                    print("Enter correct task number!")
    else:
        print("Program is case sensitive please try again")
  elif task == "register":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Register as Student~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    a = input("Enter your student ID")
    b = input("Enter your name")
    c = input("Enter your passowrd")
    d = (int(a), b, c)
    if stu_check(d):
        print("That ID already exist")
    else:
        s = "INSERT INTO stu_log(id , name , password )Values(%s,%s,%s)"
        cur.execute(s, d)
        mydb.commit()
        print("ID created!")
  elif task == "exit" :
      print("Exiting..........")
      lol = "exit"
  else:
    print("Program is case sensitive please try again")

