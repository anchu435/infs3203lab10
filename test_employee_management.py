import unittest
import employee_management

class TestEmployeeManagement(unittest.TestCase):
    def test_add_employee(self):
        management = employee_management.EmployeeManagement()
        employee = employee_management.Employee("John Doe", 30, 1)
        management.add_employee(employee)
        self.assertIn(employee, management.employees)
    
    def test_get_employee_by_id(self):
        management = employee_management.EmployeeManagement()
        employee = employee_management.Employee("John Doe", 30, 1)
        management.add_employee(employee)
        employee_id = management.get_employee_by_id(1)
        self.assertIsNotNone(employee_id)
    
    def test_get_employee_by_id_not_found(self):
        management = employee_management.EmployeeManagement()
        employee = employee_management.Employee("John Doe", 30, 1)
        management.add_employee(employee)
        employee_id = management.get_employee_by_id(100)
        self.assertIsNone(employee_id)
    
    def test_delete_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John Doe", 30, 1)
        employee2 = employee_management.Employee("Doe", 30, 2)
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.delete_employee(2)
        getemployee = management.get_employee_by_id(2)
        self.assertIsNone(getemployee)
    
    def test_delete_employee_not_employee(self):
        management = employee_management.EmployeeManagement()
        employee1 = employee_management.Employee("John Doe", 30, 1)
        employee2 = employee_management.Employee("Doe", 30, 2)
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.delete_employee(200)
        getemployee = management.get_employee_by_id(2)
        self.assertIsNotNone(getemployee)
    



if __name__ == '__main__':
    unittest.main()