""" This is a small console application using curses ans sqlite. Would like the user to put in their bank balance and 
log all their monthly direct debits and bills. The application will store and display the debts. It will also show up 
coming debts based on the current day and give a minimum required bank balance.
"""

import os
import sqlite3
from turtle import update
from typing import ParamSpec



bank_balance = 0

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
    pass

def add_debt():
    
    pass

def list_all_debts():
    
    pass

def remove_debt():
    
    pass

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
    mainmenu(new_bank_balance)

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
    
    choice = input(f"   Current Balance... £{bank_balance}                                       Please Make a Selection... ")

    while choice != 1 or 2 or 3 or 4 or 5 or 6:
        if choice == "1":
            add_debt()
        if choice == "2":
            remove_debt()
        if choice == "3":
            list_all_debts()
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



