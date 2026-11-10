""" This is a small console application using sqlite. Would like the user to put in their bank balance and 
log all their monthly direct debits and bills. The application will store and display the debts. It will also show up 
coming debts based on the current day and give a minimum required bank balance.
"""



import os
import sqlite3
import datetime

bank_balance = float(0)


# Function to clear the screen
def clear():
    os.system('clear')

def create_database():
    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()

    cur.execute(""" CREATE TABLE Debts(
                debt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                debt_name TEXT,
                debt_date TEXT,
                debt_cost REAL)
    """)
    con.close()
    mainmenu(bank_balance)

def list_all_debts(bank_balance):
    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()
    clear()
    print("*" * 100)
    print("*" * 100)
    print("**" + " " * 96 + "**")
    print("**" + " " * 41 + "LIST ALL DEBTS" + " " * 41 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 3)
    
    cur.execute("SELECT * FROM Debts")

    con.commit()

    all_debts = cur.fetchall()

    row_count = len(all_debts)
    record = 0

    print("     ID     Debt Description           Payment Date      Cost")
    print()

    while record < row_count:
        print("     {:<6} {:<26} {:<17} {:<45.2f}".format(all_debts[record][0],all_debts[record][1],all_debts[record][2],all_debts[record][3]))

        record = record + 1

    print()
    input("Press Any Key to Return to Main Menu")    
    con.close()
    mainmenu(bank_balance)
    

def add_debt(bank_balance):
    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()
    clear()
    print("*" * 100)
    print("*" * 100)
    print("**" + " " * 96 + "**")
    print("**" + " " * 44 + "ADD DEBT" + " " * 44 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 13)
    debt_name = input("Please Enter the Debt Name... ")
    print()
    while True:
        
            debt_date = input("Please Enter the Debt Payment Day of the Month...1 - 31 ")
            try:
                day = int(debt_date)
                if 1 <= day <= 31:
                    print()
                    break
                else:
                    print("This needs to be a vaule between 1 - 31..")
            except ValueError:
                print("Please enter a vaild number between 1 - 31..")

    while True:

        try: 
            debt_cost = float(input("Please Enter the Debt Cost...£ "))
            break
        except ValueError:
            print("Please enter a valid value..")


    params = (debt_name, debt_date, debt_cost)

    cur.execute("INSERT INTO Debts VALUES (NULL,?,?,?)", params)
    con.commit()
    con.close()
    mainmenu(bank_balance)

def remove_debt(bank_balance):
    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()
    clear()
    print("*" * 100)
    print("*" * 100)
    print("**" + " " * 96 + "**")
    print("**" + " " * 41 + "REMOVE A DEBT" + " " * 42 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 3)
    
    cur.execute("SELECT * FROM Debts")

    con.commit()

    all_debts = cur.fetchall()

    row_count = len(all_debts)
    record = 0

    print("     ID     Debt Description           Payment Date      Cost")
    print()

    while record < row_count:
        print("     {:<6} {:<26} {:<17} {:<45.2f}".format(all_debts[record][0],all_debts[record][1],all_debts[record][2],all_debts[record][3]))

        record = record + 1


    print()
    check = 0
    while check != "1":

        todel = input("Please Enter the ID of the Debt to Delete or 'q' to Return to Main Menu... ")
        
        if str(todel) == "q":
            check = 1
            break
        else:
            cur.execute("DELETE FROM Debts WHERE debt_id=?", (todel,))
            con.commit()
            break
    
    
    print()
    input("Press Any Key to Return to Main Menu")    
    con.close()
    mainmenu(bank_balance)

def upcoming_debt_check(bank_balance):
    clear()
    print("*" * 100)
    print("*" * 100)
    print("**" + " " * 96 + "**")
    print("**" + " " * 38 + "UPCOMING DEBT CHECK" + " " * 39 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 3)

    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()

    days_list = []
    total_cost = float(0)
    new_balance = float(0)
    # get todays date
    current_date = datetime.date.today()
    
    # Get the number of days ahead that you would like to check for debts
    days_ahead = input("How Many Days Ahead... ")
    print()
    # Get the new date from adding days from input
    new_date = current_date + datetime.timedelta(days=float(days_ahead))

    # Get days inbetween dates
    other_date = new_date - current_date

    # Get list of days in date range
    for i in range(other_date.days + 1):
        day = current_date + datetime.timedelta(days=i)
        days_list.append(str(day.day))
    

    # Get all the debts from the database
    all_debts = cur.execute("SELECT * FROM Debts")
    con.commit()

    records = cur.fetchall()
    
    # Lists the debts in the date range
    print("The Following Debts Are Within The Selected Date Range:")
    print()
    print("Debt             Date Due            Debt Cost")
    print()


    for record in records:
        if record[2] in days_list:
            print("{:<16} {:<20} {:<16.2f}".format(record[1],record[2],record[3]))
     
            total_cost = total_cost + (record[3])
            
    new_balance = bank_balance - total_cost        

    # Get all debt costs total and take them from bank balance into new balance to display to screen
    print()
    print(f"You will need £{total_cost:.2f} in the bank to cover debts")
    print()
    print(f"Based on your current balance you will have £{new_balance:.2f} left")
    print()
    
    input("Press 'Enter' to return to the Main Menu...")

    con.close()
    mainmenu(bank_balance)
    pass

def bank_balance_update():
    clear()
    print("*" * 100)
    print("*" * 100)
    print("**" + " " * 96 + "**")
    print("**" + " " * 42 + "DEBT RELIEF" + " " * 43 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 18)

    while True:

        try:
            new_bank_balance = float(input("Please Enter Your Bank Balance... "))
            bank_balance = new_bank_balance
            break
        except ValueError:
            print("Please enter a valid amount..")

    mainmenu(bank_balance)

# Main Menu - Add Debt / List All Debts / Remove Debts / Upcoming Debts Check / Bank Balance Update
def mainmenu(bank_balance):
    clear()
    print("*" * 100)
    print("*" * 100)
    print("**" + " " * 96 + "**")
    print("**" + " " * 42 + "DEBT RELIEF" + " " * 43 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 3)
    print("     (1)  Add Debt                                           (2)  Remove Debt")
    print()
    print("     (3)  List All Debts                                     (4)  Upcoming Debt Check")
    print()
    print("     (5)  Bank Balance Update                                (6)  Quit")
    print("""
    """ * 5)
    
    choice = input(f"       Current Balance... £{bank_balance:.2f}                              Please Make a Selection... ")

    while choice != 1 or 2 or 3 or 4 or 5 or 6:
        if choice == "1":
            add_debt(bank_balance)
        if choice == "2":
            remove_debt(bank_balance)
        if choice == "3":
            list_all_debts(bank_balance)
        if choice == "4":
            upcoming_debt_check(bank_balance)
        if choice == "5":
            bank_balance_update()
        if choice == "6":
            quit()
        else:
            mainmenu(bank_balance)        


file_exists = os.path.exists('DebtRelief.db')

clear()

if file_exists:
    mainmenu(bank_balance)
else:
    print("Creating New Database...")
    print()
    input("Press Any Key to Continue...")
    create_database()



