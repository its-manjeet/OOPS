# initiate a class
class employee:
    #Special Method/ Magic Method or Dunder Method.
    def __init__(self):
        print("Started executing Attributes or Data:")
        self.id = 123
        self.designation = "SDE"
        self.salary = "5000000"
        print("Attributes and Data have been initiated.")

    def travel(self, heaven):
        print("This travel function was called manually")
        print(f"Employees are now travelling to {heaven}")

#creating an obj/instance of the class:
sham = employee()

#Printing the Attributes:
# print(sham.salary)
# print(sham.id)
# print(sham.designation)

sham.travel("jannat")  ##Calling the Method

print(type(sham))
 
a = "x"
b = "y"
print(a+b)  ##There are no algebraic Data Types created in here.










