a=2
b=10
if b > a:
    print("b is greater than a")
x=lambda a: a+10
print(x(5))
x=lambda a,b:a*b
print(x(10,5))
x=lambda a, b,c: a+b+c
print(x(1,2,3))

#function
def my_function():
    print("Hello World")
my_function()
def F1(fname1): #set parameter
    print(fname1+"Apple")
F1("New ")
F1("Old ")
F1("Buy ")
#class, property and object
class Myclass:
    x=5
p1=Myclass()
print(p1.x)

class Vehicle:
    name=""
    kind="car"
    coloe=""
    value=100.00
    def description(self):
        desc_str="%s is a %s worth $%.2f" %(self.name,self.color,self.kind,self.value)
        return desc_str
    car1=Vehicle()
    car1.name="fer"
    car1.color="red"
    car1.kind="convertible"
    car1.value=100000.00
    car2.Vehicle()
    car2.name="Love"
    car2.coloe="white"
    car2.kind="truke"
    car2.value=50000.00
    print(car1.description())
    print(car2.description())