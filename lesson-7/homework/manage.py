class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")

    @staticmethod
    def view_all_employees():
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    @staticmethod
    def find_employee_by_id(employee_id):
        employees = EmployeeManager.view_all_employees()
        for record in employees:
            if record.startswith(employee_id):
                return record.strip()
        return None

    @staticmethod
    def delete_employee(employee_id):
        employees = EmployeeManager.view_all_employees()
        updated_employees = [emp for emp in employees if not emp.startswith(employee_id)]
        with open(EmployeeManager.FILE_NAME, "w") as file:
            file.writelines(updated_employees)

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        employees = EmployeeManager.view_all_employees()
        updated_employees = []
        for record in employees:
            if record.startswith(employee_id):
                parts = record.strip().split(", ")
                if name:
                    parts[1] = name
                if position:
                    parts[2] = position
                if salary:
                    parts[3] = salary
                updated_employees.append(", ".join(parts) + "\n")
            else:
                updated_employees.append(record)
        with open(EmployeeManager.FILE_NAME, "w") as file:
            file.writelines(updated_employees)
