# Debt Relief

A command-line budgeting app that keeps track of your monthly bills and direct debits. Tell it how many days ahead to look, and it lists the bills due in that time, totals what you need in the bank to cover them, and shows what you'll have left from your current balance.

## Why I built it

I built this for someone who found it hard to manage their money and often didn't have enough in the bank when direct debits came out. The idea was to make it easy to see exactly what was due in the next few days, and how much needed to be in the account to cover it. I also wanted a project to practise using SQLite from Python.

## Features

- Add and remove monthly bills, each with a name, the day of the month it's paid and the amount in pounds and pence
- List every bill you've saved
- Upcoming bill check: choose how many days ahead to look, and see which bills fall in that period, the total due and your balance afterwards
- Works across the end of a month, because bills are matched by day of the month
- Checks the day, amount and balance as they are entered, so a typo (like `£450` or a day of `0`) asks again instead of crashing
- Bills are saved in a local SQLite database, which is created automatically the first time you run it

## Built with

- Python 3
- SQLite (`sqlite3`, part of Python's standard library)
- `datetime` for working out the date range

## Running it

You need Python 3. No extra packages are required.

```
python3 DebtRelief.py
```

On first run it creates `DebtRelief.db` in the same folder. Choose options from the main menu by number.

## Example

With a balance of £500.50, rent of £450 due today and a phone bill of £25.99 due in two days, checking three days ahead gives:

```
The Following Debts Are Within The Selected Date Range:

Debt             Date Due            Debt Cost

Rent             10                   450.00
Phone            12                   25.99

You will need £475.99 in the bank to cover debts

Based on your current balance you will have £24.51 left
```

## What I learned

- Creating and querying an SQLite database from Python
- Using parameterised queries (`?` placeholders) to insert and delete records safely
- Working with dates and date ranges using `datetime` and `timedelta`
- Building a menu-driven console program with formatted tables
- Validating user input with `try`/`except` and `while` loops

## Ideas for improvement

- Save the bank balance between sessions (it currently resets to £0 each time)
- Use a loop for the main menu instead of each screen calling the menu again