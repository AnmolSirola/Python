class Employee:

# Constructor 
    def __init__(self):
        self.id = 123
        self.salary = 5000
        self.designation = "SDE"
    
    def travel(self, destination):
        print(f"Employee is going to black town called: {destination}")

# Instance of a class
sam = Employee()

print(sam.id)

# Calling a method
sam.travel("Kerela")