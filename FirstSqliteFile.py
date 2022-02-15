import sqlite3

from sqlite3 import Error


def sql_connection():   #Establish a connection
    try:                #Exception handling (try,except,finally)
        conn = sqlite3.connect('SalesManEmp.db') #Create or Open existing database
        return conn
    except Error:
        print(Error)

def sql_Createtable(conn):  #SalesManEmp.db
    cursorObj = conn.cursor() #points to the database Sales.db
    # Create the table in Sales.db
    cursorObj.execute("CREATE TABLE salesEmp(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
    print("table create\n")
def readTable(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT name,city FROM salesEmp WHERE salesman_id > 1003 ") #name and city columns ->where id>1003
    cursorObj.execute("SELECT * FROM salesEmp  ") #*-> all columns from tablename
   #  cursorObj.execute("SELECT * FROM salesEmp WHERE salesman_id > 1003 ")# * -> all columns ->WHERE CLAUSE-SELECTED ROWS
    rows = cursorObj.fetchall()  # rows-> all the records in the salesman table
    print("Agent details:")
    for row in rows:
        print(row)

def InsertRecords(conn):
    Obj = conn.cursor()
    # Insert records
    Obj.executescript("""
        INSERT INTO salesEmp VALUES(1002,'Sam', 'Wgl', 34.15);
        INSERT INTO salesEmp VALUES(1003,'Ram', 'kmr', 12.25);
        INSERT INTO salesEmp VALUES(1004,'Avi', 'Bhpl', 24.15);
        INSERT INTO salesEmp VALUES(1005,'Amy', 'kmm', 89.35);
        INSERT INTO salesEmp VALUES(1006,'Ven', 'Ngl', 67.45);
        """)
    # conn.commit()  # STORE THE DATA PERMANENTLY
    print("values inserted")
def RecordUpdate(conn):
    Obj = conn.cursor()
    Obj.execute("UPDATE salesEmp SET salesman_Id = 1500,city = 'Hyd' WHERE name = 'Ven'; ")
    #changes the id = 1008 and city = hyd where name ven
    print("record updated\n")
def RecordDelete(conn):
    Obj = conn.cursor()
    Obj.execute("Delete from salesEmp where city = 'Hyd'; ") #delete the row where city = Hyd
    print("record deleted")
def DeleteTable(conn):
    Obj = conn.cursor()
    Obj.execute("Drop table salesEmp ")  # delete the row where city = Ngl
    print("table is deleted")
def CountRows(conn):
    Obj = conn.cursor()
    rows = Obj.execute("select * from salesEmp")
    print("number of records are ",len(rows.fetchall()))

sqlite_conn = sql_connection()
# sql_Createtable(sqlite_conn)
# InsertRecords(sqlite_conn)
# RecordUpdate(sqlite_conn)
# RecordDelete(sqlite_conn)
readTable(sqlite_conn)
CountRows(sqlite_conn)
# DeleteTable(sqlite_conn)
if (sqlite_conn):
    sqlite_conn.close()
    print("\nThe SQLite connection is closed.")