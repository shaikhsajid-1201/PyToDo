from utility import mysqlconn
from termcolor import colored

# Creating Cursor()
cursor = mysqlconn.auth.cursor()

scriptpath = "/myapp/script.sql"

# Create table in MySQL 
def create_table(path):
    with open(path, "r") as sql:
        script = sql.read()
    cursor.execute(script)

# create_table(r"C:\Users\shaik\OneDrive\Desktop\MyFolders\Study Material\Python Projects\PYSQL_Todo\script.sql")
create_table(scriptpath)

# Task functions 
def write_todo(id, title, description):
    sql = "INSERT INTO todolist(id, title, description) VALUES (%s, %s, %s);"
    values = (id, title, description)
    cursor.execute(sql, values)
    mysqlconn.auth.commit()

def check_task(id):
    # Checking id is available or not. 
    sql_check = "SELECT COUNT(*) FROM todolist WHERE id = %s"  
    cursor.execute(sql_check, (id,))
    record_count = cursor.fetchone()[0]
    count = 0

    if record_count == True:
        count += 1
    
    return count

def read_todo(id):
    sql = "SELECT * FROM todolist WHERE id = %s"
    values = (id)
    cursor.execute(sql, (values,))
    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("Record not found..:(")

def show_all():
    sql = "SELECT * FROM todolist;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

def update_todo(*args):
    sql = "UPDATE todolist SET title = %s, description = %s WHERE id = %s"
    values = (title, description, id)
    cursor.execute(sql, values)
    mysqlconn.auth.commit()

def delete_todo(id):
    sql = "DELETE FROM todolist WHERE id = %s"
    values = (id)
    cursor.execute(sql, (values,))
    mysqlconn.auth.commit()
    
# Task Management
while True:
    print("Please select your option?")
    print("1. Write tasks")
    print("2. Read tasks")
    print("3. Show all tasks")
    print("4. Update task")
    print("5. Delete task")
    print("0. Quit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        id = int(input("Enter taskID : "))
        title = input("Enter your title : ")
        description = input("Enter your description : ")
        write_todo(id, title, description)
        print("-" * 30)
        print(colored("Successfully added..", "green"))
        print("-" * 30)
    elif choice == 2:
        id = int(input("Enter your taskID : "))
        print("-" * 30)
        read_todo(id)
        print("-" * 30)
    elif choice == 3:
        print("-" * 30)
        show_all()
        print("-" * 30)
    elif choice == 4:
        id = int(input("Enter taskID : "))
        result = check_task(id)
        if result == 1:
            id = int(input("Enter taskID : "))
            title = input("Enter title : ")
            description = input("Enter description : ")
            update_todo(id, title, description)
            print("-" * 30)
            print(colored("Task updated successfully", "green"))
            print("-" * 30)
        else:
            print("-" * 30)
            print(colored("Invalid taskID", "red"))
            print("-" * 30)
    elif choice == 5:
        id = int(input("Enter taskID : "))
        delete_todo(id)
        print("-" * 30)
        print(colored("Your task deleted successfully..", "green"))
        print("-" * 30)
    elif choice == 0:
        break
    else:
        break

cursor.close()
mysqlconn.auth.close()