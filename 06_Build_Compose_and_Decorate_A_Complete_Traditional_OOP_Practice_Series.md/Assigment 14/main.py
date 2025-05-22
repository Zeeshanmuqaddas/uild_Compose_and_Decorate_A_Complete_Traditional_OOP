class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __str__(self):
        return f"Employee[ID={self.emp_id}, Name={self.name}]"


class Department:
    def __init__(self, dept_name, employee=None):
        self.dept_name = dept_name
        # Aggregation: Department holds a reference to Employee
        self.employee = employee

    def set_employee(self, employee):
        self.employee = employee

    def __str__(self):
        emp_info = str(self.employee) if self.employee else "No employee assigned"
        return f"Department: {self.dept_name}, Employee: {emp_info}"


# Example usage
emp1 = Employee(101, "Alice")
dept = Department("HR", emp1)

print(dept)  # Department: HR, Employee: Employee[ID=101, Name=Alice]

# The employee exists independently of the department
print(emp1)  # Employee[ID=101, Name=Alice]
