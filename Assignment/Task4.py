class Employee:
    def working(self):
        print("Employee is working")
        
class Manager(Employee):
    def working(self):
        print("Manager is managing the team.")  
        
class Developer(Employee):
    def working(self):
        print("Developer is writing code.") 
        
#example
manager = Manager()
developer = Developer()
manager.working()
developer.working()