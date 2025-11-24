#INITIALTE A CLASS
class employee:
    #special method/magic method/ dunder method --- constructor
    def __init__(self):
        print("Started initializing the attribute/data")
        self.id = 123
        self.salary =  50000
        self.designation = "developer"
        print("attribute/data have beem initiated")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now traveling to {destination}")

#creating an object/instance of the class
sam = employee()

#printing the attributes
#print(sam.id)
#print(sam.salary)

#calling a method
sam.travel("Kerala")