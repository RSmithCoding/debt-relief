""" This is a small console application using curses ans sqlite. Would like the user to put in their bank balance and 
log all their monthly direct debits and bills. The application will store and display the debts. It will also show up 
coming debts based on the current day and give a minimum required bank balance.
"""

from contextlib import nullcontext
from io import DEFAULT_BUFFER_SIZE
import os
import sqlite3
from turtle import update
from typing import ParamSpec
import datetime

bank_balance = 0

ADD_DEBT = "INSERT INTO Debts (debt_name, debt_date) VALUES (?,?)"


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
                debt_cost TEXT)
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
#    print(all_debts)
    row_count = len(all_debts)
    record = 0

    print("     ID     Debt Description           Payment Date      Cost")
    print()

    while record < row_count:
        print("     {:<6} {:<26} {:<17} {:<45}".format(all_debts[record][0],all_debts[record][1],all_debts[record][2],all_debts[record][3]))
        #print(all_debts[record][0],all_debts[record][1],all_debts[record][2],all_debts[record][3])
        record = record + 1
#    for item in all_debts:
#        print(item)

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
    debt_date = input("Please Enter the Debt Payment Date... ")
    print()
    debt_cost = input("Please Enter the Debt Cost... ")

    params = (debt_name, debt_date,debt_cost)

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
    print("**" + " " * 43 + "REMOVE A DEBT" + " " * 44 + "**")
    print("**" + " " * 96 + "**")
    print("*" * 100)
    print("*" * 100)
    print("""
    """ * 3)
    
    cur.execute("SELECT * FROM Debts")

    con.commit()

    all_debts = cur.fetchall()
#    print(all_debts)
    row_count = len(all_debts)
    record = 0

    print("     ID     Debt Description           Payment Date      Cost")
    print()

    while record < row_count:
        print("     {:<6} {:<26} {:<17} {:<45}".format(all_debts[record][0],all_debts[record][1],all_debts[record][2],all_debts[record][3]))
#       print(all_debts[record][0],all_debts[record][1],all_debts[record][2])
        record = record + 1
#    for item in all_debts:
#        print(item)

    print()
    print()
    check = 0
    while check != "1":

        todel = input("Please Enter the ID of the Debt to Delete or 'q' to Return to Main Menu... ")
        print(todel)
        input()
        if str(todel) == "q":
            check = 1
            break
        else:
            cur.execute("DELETE FROM Debts WHERE debt_id=?",todel)

            con.commit()
    
    

    input("Press Any Key to Return to Main Menu")    
    con.close()
    mainmenu(bank_balance)

def upcoming_debt_check(bank_balance):
    clear()
    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()

    days_list = []
    
    # get todays date
    current_date = datetime.date.today()
    
    # Get the number of days ahead that you would like to check for debts
    days_ahead = input("How Many Days Ahead... ")

    # Get the new date from adding days from input
    new_date = current_date + datetime.timedelta(days=float(days_ahead))

    # Get days inbetween dates
    other_date = new_date - current_date

    # Get list of days in date range
    for i in range(other_date.days + 1):
        day = current_date + datetime.timedelta(days=i)
        days_list.append(str(day.day))
    
    #print(other_date)
    #print(other_date.days)

    # Get all the debts from the database
    all_debts = cur.execute("SELECT * FROM Debts")
    con.commit()

    records = cur.fetchall()
    
    # Lists the debts in the date range
    print("The Following Debts Are Within The Selected Date Range:")
    print()
    print("Debt             Date Due")
    print()

    for record in records:
        if record[2] in days_list:
            print(f"{record[1]}              {record[2]}")

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
    """ * 13)
    new_bank_balance = input("Please Enter Your Bank Balance... ")
    bank_balance = new_bank_balance
    print(bank_balance)
    input()
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
    
    choice = input(f"       Current Balance... £{bank_balance}                              Please Make a Selection... ")

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
# Check to see if database already exist or not

file_exists = os.path.exists('DebtRelief.db')

clear()

if file_exists:
    mainmenu(bank_balance)
else:
    print("Creating New Database...")
    print()
    input("Press Any Key to Continue...")
    create_database()



