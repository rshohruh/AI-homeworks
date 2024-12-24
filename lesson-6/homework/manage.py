def employee_manager():
    def add_employee():
        with open("employees.txt", "a") as file:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            file.write(f"{emp_id}, {name}, {position}, {salary}\n")
            print("Employee record added successfully.")

    def view_employees():
        try:
            with open("employees.txt", "r") as file:
                records = file.readlines()
                if not records:
                    print("No records found.")
                else:
                    print("Employee Records:")
                    for record in records:
                        print(record.strip())
        except FileNotFoundError:
            print("No records found. Please add employees first.")

    def search_employee():
        emp_id = input("Enter Employee ID to search: ")
        try:
            with open("employees.txt", "r") as file:
                for record in file:
                    if record.startswith(emp_id + ","):
                        print("Employee Found:", record.strip())
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    def update_employee():
        emp_id = input("Enter Employee ID to update: ")
        try:
            with open("employees.txt", "r") as file:
                records = file.readlines()
            updated = False
            with open("employees.txt", "w") as file:
                for record in records:
                    if record.startswith(emp_id + ","):
                        name = input("Enter New Name: ")
                        position = input("Enter New Position: ")
                        salary = input("Enter New Salary: ")
                        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                        updated = True
                    else:
                        file.write(record)
            print("Employee updated successfully." if updated else "Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    def delete_employee():
        emp_id = input("Enter Employee ID to delete: ")
        try:
            with open("employees.txt", "r") as file:
                records = file.readlines()
            deleted = False
            with open("employees.txt", "w") as file:
                for record in records:
                    if record.startswith(emp_id + ","):
                        deleted = True
                    else:
                        file.write(record)
            print("Employee deleted successfully." if deleted else "Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    while True:
        print("""
        1. Add new employee record
        2. View all employee records
        3. Search for an employee by Employee ID
        4. Update an employee's information
        5. Delete an employee record
        6. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting Employee Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

employee_manager()
