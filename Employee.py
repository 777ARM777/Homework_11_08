class Employee:
    employee_id = 1

    def __init__(self, name):
        self.name = name
        self.emp_id = Employee.employee_id
        Employee.employee_id += 1

    def set_data(self):
        self.name = input('Please input name: ')
        self.emp_id = Employee.employee_id
        Employee.employee_id += 1

    def put_data(self):
        print(f'Name: {self.name}. ID: {self.emp_id}')


emp1 = Employee('Bob')
emp2 = Employee('James')
emp3 = Employee('Jude')
emp4 = Employee('Aram')
emp3.set_data()

for i in (emp1, emp2, emp3, emp4):
    i.put_data()

