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

def introduce(name):
    print ("Hello,",name,"!")
introduce("Cal")
introduce("John")

def favorite_food(food1):
    print("I love",food1)

favorite_food("Pizza")
favorite_food("Sushi")
favorite_food("Chocolate")

import random
foods = random.choice(food)
print("I like",foods,"!") 

food.append("sushi")

def favorite_food(foods):
    print ("I love",foods)

for foods in food: 
    favorite_food(foods)

picked_food = random.choice(food)
print("AI picked",picked_food,"for me")

activities = ["Reading", "Coding", "Gaming", "Walking"]

def recommended_activity(activity_list):
    choice = random.choice(activity_list)
    print("AI recommends:",choice)

recommended_activity(activities)



