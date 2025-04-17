#NAME: KASHISH GUPTA 231P081/09 SECOMPS A
"""WAP to demonstrate CRUD (create,read,update,delete) operation on database using sqlite3
import sqlite3"""
import sqlite3
n = 0
while n != 7:
    print("1. Create\n2. Insert\n3. Select\n4. Update\n5. Delete\n6. Drop Table\n7. Exit")
    n = int(input("Enter your operation: "))
    if n == 1:
        # Create table in database
        conn = sqlite3.Connection("Test.db")
        print("Opened database successfully")
        # Creating the table if it doesn't exist already
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Factory (
            ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL
        );
        """)
        print("Table created successfully")
        conn.close()
    elif n == 2:
        # Insert into database
        conn = sqlite3.Connection("Test.db")
        print("Opened database successfully")        
        # Insert some records into the table
        conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (1, 'Virat Kohli', 28, 'RCB', 2000000.0)")
        conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (2, 'Rohit Sharma', 30, 'MI', 4000000.0)")
        conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (3, 'Mohd Shami', 32, 'KXIP', 6000000.0)")
        conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (4, 'Bhuvneshwar', 27, 'SH', 6000000.0)")       
        conn.commit()
        print("Insert operation done successfully")
        conn.close()   
    elif n == 3:
        # Select from database
        conn = sqlite3.Connection("Test.db")
        print("Opened database successfully")
        cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM Factory")    
        for row in cursor:
            print(f"ID = {row[0]}")
            print(f"NAME = {row[1]}")
            print(f"AGE = {row[2]}")
            print(f"ADDRESS = {row[3]}")
            print(f"SALARY = {row[4]}\n")
        print("Select done successfully")
        conn.close()
    elif n == 4:
        # Update database
        conn = sqlite3.Connection("Test.db")
        print("Opened database successfully")
        conn.execute("UPDATE Factory SET SALARY = 2500000.0 WHERE ID = 1")
        conn.commit()
        print(f"Total number of rows updated: {conn.total_changes}")
        cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM Factory")
        for row in cursor:
            print(f"ID = {row[0]}")
            print(f"NAME = {row[1]}")
            print(f"AGE = {row[2]}")
            print(f"ADDRESS = {row[3]}")
            print(f"SALARY = {row[4]}\n")
        print("Update done successfully")
        conn.close()
    elif n == 5:
        # Delete from database
        conn = sqlite3.Connection("Test.db")
        print("Opened database successfully")
        conn.execute("DELETE FROM Factory WHERE ID = 2")
        conn.commit()      
        cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM Factory")
        for row in cursor:
            print(f"ID = {row[0]}")
            print(f"NAME = {row[1]}")
            print(f"AGE = {row[2]}")
            print(f"ADDRESS = {row[3]}")
            print(f"SALARY = {row[4]}\n")        
        print("Delete done successfully")
        conn.close()
    elif n == 6:
        # Drop table in database
        conn = sqlite3.Connection("Test.db")
        print("Opened database successfully")
        conn.execute("DROP TABLE IF EXISTS Factory")
        print("Table deleted successfully")
        conn.close()
    elif n == 7:
        print("Exiting program...")
        print("\nThank You \nName: KASHISH GUPTA \nUIN:231P081 \nRoll no:09 \n")
