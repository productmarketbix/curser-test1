print("Hello, I am a venemous Python myself")
name = "Cal" 
age = 20
city = "London"
print("My name is",name,"and I am",age,"years old and I live in",city)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
fruits.append("fig")
print("I like",fruits)
for fruit in fruits:
    print("I like",fruit)
food = ["pizza", "hamburger", "hotdog"]
for foods in food:
    print("I like",foods)

age = 20
if age>= 18: 
    print("You are an adult")
else:
    print("You are a minor")

if food[0]=="pizza":
    print("I love",food[0])
else:
    print("I love",food[1])

for foods in food:
    if foods == "pizza":
        print("I found",foods,"in the list")
    else:
        print("I found",foods,"in the list instead")


