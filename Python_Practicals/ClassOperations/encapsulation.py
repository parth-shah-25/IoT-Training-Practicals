employeeSalary = 650000
newSalary = 0

class master:
    def printSalary(self):
        print(employeeSalary)
    
    def increaseSalary(self):
        global newSalary
        newSalary = employeeSalary + (int(employeeSalary*(20/100)))
        # print (employeeSalary + (int(employeeSalary*(20/100))))
        print("Woo Hoo! Salary Increased.. ")

    def employeeInfo(self, name):
        print("Updated Salary of {} is Rs.".format(name), newSalary)


obj1 = master()
obj1.printSalary()
obj1.increaseSalary()
obj1.employeeInfo("Parth")