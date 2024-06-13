import sqlite3

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, amount REAL)''')
    connection.commit()

def add_cost(connection, date, amount):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO expenses (date, amount) VALUES (?, ?)", (date, amount))
    connection.commit()

def show_costs(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    result = cursor.fetchall()
    for row in result:
        print(row)

def delete_cost(connection, expense_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    connection.commit()

def main():
    cnt = sqlite3.connect('expense.db')
    create_table(cnt)

    while True:
        print("1. Add cost")
        print("2. Show costs")
        print("3. Delete cost")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == '1':
            date = input("Enter the date of deposit: ")
            amount = float(input("Enter amount of money: "))
            add_cost(cnt, date, amount)
            print("Successfully added")
        elif option == '2':
            show_costs(cnt)
        elif option == '3':
            expense_id = int(input("Enter ID of deposit: "))
            delete_cost(cnt, expense_id)
            print("Successfully deleted")
        elif option == '4':
            break
        else:
            print("Wrong option, try again")

    cnt.close()

if name == "main":
    main()