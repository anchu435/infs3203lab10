class Employee:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age 
        self.id = id

class EmployeeManagement:
    def __init__(self):
        self.employees = []
    
    def add_employee(self,employee):
        if not employee.name or not employee.age or not employee.id:
            print("Name, age and id cannot be empty.")
            return
        if not isinstance(employee.age, int) or employee.age < 0:
            print("Age must be a positive integer.")
            return

        if not isinstance(employee.id, int) or employee.id < 0:
            print("Employee ID must be a positive integer.")
            return
        
        self.employees.append(employee)
        print("Employee created successfully")
    
    def get_employee_by_id(self,emp_id):

        if not isinstance(emp_id, int) or emp_id < 0:
            print("Employee ID must be a positive integer.")
            return None

        for employee in self.employees:
            if employee.id == emp_id:
                return employee
        print("Not Found")
    
    def delete_employee(self,id):
        if not isinstance(id, int) or id < 0:
            print("Employee ID must be a positive integer.")
            return None
        
        for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)
                print("Employee deleted successfully")
        print("Employee not found")



# Creating new employees
emp1 = Employee("John Doe", 30, 1)
emp2 = Employee("Jacob", 20, 2)
emp3 = Employee("George", 24, 3)
management = EmployeeManagement()
management.add_employee(emp1)
management.add_employee(emp2)
management.add_employee(emp3)
management.get_employee_by_id(1)
management.delete_employee(2)