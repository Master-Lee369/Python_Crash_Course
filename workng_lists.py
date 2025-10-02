international_pizzas = [
    "Tandoori Chicken", "Butter Chicken", "Paneer Tikka", "Mexican Fiesta",
    "Greek Feta", "Turkish Lahmacun", "Japanese Teriyaki", "Korean BBQ", "Indian Curry", "Lebanese Zaatar"
]

for pizza in international_pizzas:
    print(pizza)
    print(f"i would like to have {pizza}")

print(f"i dont really love pizza but its ok to have pizza . Butter Chicken and Paneer Tikka are my favourite")



animals = ["Dog", "fighter", "Cat", "Parrot", ]

for animal in animals:
    print(animal)
    print(f"{animal} would make a good pet")
print(f"All the animals can make a good pet")

for i in range(1,10):
    print(i )

sum = 0
numbers = []
for num in range(1,100):
    numbers.append(num)
    sum = sum + num
print(numbers)
print(sum)

print(max(numbers))
print(min(numbers))


for i in range(1,21,2):
    print(i)

for mul in range(3,33,3):
    print(mul)

print("Printing the cubes of the numbers\n")
for cube in range(1,11):
    value = cube**3
    print(value)

value = [cube**3 for cube in range(1,11)]

print(value)


print(f"The first three elements in this internationnal_pizzas are {international_pizzas[:3]}")
print(f"Three items from the middle of the list are : {international_pizzas[5:8]}")
print(f"The last three items in the list are {international_pizzas[-3:]}")


friend_pizzas = international_pizzas[:]

international_pizzas.append("pazhampori pizza")
friend_pizzas.append("paneer pizza")

print(f"My favourite Pizzas are\n {international_pizzas}")
print(f"My friend's favourite pizzas are\n {friend_pizzas}")