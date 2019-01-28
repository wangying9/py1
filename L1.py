import math
A=1
print(A)
phrase="Apple"
test="Work"
print(test)
print(phrase)
print(phrase.index("App"))
print("hello")
Is_male=True
print(Is_male)
print("Aplle\nApple") #change line
print("Aplle\"Apple") #add "

#function
print(phrase.lower()) #change to lower case
print(phrase.upper())
print(phrase.upper().isupper())#return true or false
print(len(phrase))#length
print(phrase[0])#start with 0, ask the letter at 0 position
print(phrase.index("ple")) #ask for the index
print(phrase.replace("A","B"))#does not change the phrase variable, just for print
print(phrase)

#number
print(-2.98)
print(2*5+3.42)#more calculations
print(10 % 3)#modulate operator
print(str(5))#change number to
print(str(5)+"Apple")
Num=-5
print(abs(Num))#absolute number
print(pow(3,2)) #3^2
print(max(4,6))
print(round(32.8))
print(math.floor(3.7))#take lower one
print(math.ceil(3.2))#round to 4
print(math.sqrt(36))
x=int("3")#cast a string to int
print(type(x))
y=float("3.2")
print(y)
z=str(2)
print(type(z))

#input: interaction with user
from math import *
#input data
name=input("Enter your name: ")
print("Hello " +name+"!")
print("enter your name: ")
s=input()
print("Hello, "+s)


#Built calculater
num1=input("enter a number: ")#it is string
num2=input("enter another number: ")
result=(int(num1)+int(num2))
print(result)
result2=float(num1)+float(num2)#any number
print(result2)
if 5>2:
    print("Five is greater than two!")
print(type(result))#data type
t1=1j
print(type(t1))#numeric as complex

#index
a="Hellow, World"
print(a[2:5])
b="  Apple"
print(b.strip())
print(a.replace("low","lo"))
print(a.split(",")) #return ['Hellow', ' World']
#list
mylist=["Apple","orange","banana"]
print(mylist[1])
mylist.insert(1,"cherry")
print(mylist)
#function
def my_function():
    print("Aplle","Orange")#input details into the function
my_function()
def f1(fun):
    print(fun + " Orange")
f1("Apple")
def f2(func):
    print(func + "Apple")
f2("Apple")

def my_function(fname):
    print(fname + " refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

bing=2
print(bing)