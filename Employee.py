class Employee:
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print "Total Number of Employee = %d" %Employee.empCount
        
    def displayDetails(self):
        print "Employee Name = ", self.name, "Employee Salary = ", self.salary
        
emp1 = Employee("Deepak", "10000000")
emp2 = Employee("S", "120000")
emp1.displayDetails()
emp2.displayDetails()
emp1.displayCount()
#print "Total Number of Employees = %d", Employee.empCount
