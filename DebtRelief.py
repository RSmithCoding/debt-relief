""" This is a small console application using curses ans sqlite. Would like the user to put in their bank balance and 
log all their monthly direct debits and bills. The application will store and display the debts. It will also show up 
coming debts based on the current day and give a minimum required bank balance.
"""

from contextlib import nullcontext
import os
import sqlite3
from turtle import update
from typing import ParamSpec

bank_balance = 0

ADD_DEBT = "INSERT INTO Debts (debt_name, debt_date) VALUES (?,?)"


# Function to clear the screen
def clear():
    os.system('clear')

def create_database():
    con = sqlite3.connect('DebtRelief.db')
    cur = con.cursor()

    cur.execute(""" CREATE TABLE Debts(
                debt_id integer primary key,
                debt_name text,
                debt_date text)
    """)
    con.close()

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

    print("     ID     Debt Description           Payment Date")
    print()

    while record < row_count:
        print("     {:<7}{:<27}{:<39}".format(all_debts[record][0],all_debts[record][1],all_debts[record][2]))
#        print(all_debts[record][0],all_debts[record][1],all_debts[record][2])
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
    
    params = (debt_name, debt_date)

    cur.execute("INSERT INTO Debts VALUES (NULL,?,?)", params)
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

    print("     ID     Debt Description           Payment Date")
    print()

    while record < row_count:
        print("     {:<7}{:<27}{:<39}".format(all_debts[record][0],all_debts[record][1],all_debts[record][2]))
#        print(all_debts[record][0],all_debts[record][1],all_debts[record][2])
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
        if todel == "q":
            check = 1
        else:
            cur.execute("DELETE FROM Debts WHERE debt_id=?",todel)

            con.commit()
    
    

    print()
    input("Press Any Key to Return to Main Menu")    
    con.close()
    mainmenu(bank_balance)

def upcoming_debt_check():
    
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
            upcoming_debt_check()
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
    print("Database Exists...")
    print()
    input("Press Any Key to Continue...")
    mainmenu(bank_balance)
else:
    print("Creating New Database...")
    print()
    input("Press Any Key to Continue...")
    create_database()



