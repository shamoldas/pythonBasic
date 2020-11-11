class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

   # def displayCount(self):
      # print("total Employee:%d" Employee.empCount)

    def displayEmployee(self):
        print("name:",self.name,",salary:",self.salary)

    emp1=Employee("zara",500)
    emp2=Employee("das",3200)
    emp1.displayEmployee()
    print(emp1)
