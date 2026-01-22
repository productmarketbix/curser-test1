print("Hello World!")
name = "Kaushik"
age = 17
print("My name is",name,"and I am",age,"years old")
fruits = ["apple","orange","banana","cherry"]
print(fruits[0])
fruits.append("berry")
print(fruits)

for a in fruits:
    print("I like",a)

if age>= 18:
    print("Adult")
else:
    print("Minor")

for b in fruits:
    if b == "apple":
        print ("I found",b)
    else:
        print("No we did not find apples but found",b)

def greet(x1):
    print("Hello",x1)

greet("Kaushik")


def square(b):
    return b*b
print (square(5))





  
