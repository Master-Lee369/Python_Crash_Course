prompt = "Enter the pizza toppings that you wish to add in your pizza :\n"
prompt += "\n Enter quit if you want to stop "

pizza_toppings = ""
while pizza_toppings != "quit":
    pizza_toppings = input(prompt)
    if pizza_toppings != "quit":
        print(f"I will add {pizza_toppings} toppings to pizza\n")


age = input("Enter your age to check for the ticket prize\n")
age = int(age)

active = True

while age :
    if age < 3:
        print("The ticket is free\n")
        break
    elif age >= 3 and age <= 12:
        print("The ticket rate is $10\n")
        break
    elif age > 12:
        print("The ticket rate is $15\n")
        break
    else:
        break

age = input("Enter your age to check for the ticket prize\n")
age = int(age)

active = True

while active :
    if age < 3:
        print("The ticket is free\n")
        active = False
    elif age >= 3 and age <= 12:
        print("The ticket rate is $10\n")
        active = False
    elif age > 12:
        print("The ticket rate is $15\n")
        active = False
    else:
        active = False



sandwich_orders = ["BLT","pastrami","Club Sandwich","Grilled Cheese","Philly Cheesesteak", "Po' Boy","pastrami","Meatball Sub","Veggie Sandwich","Shawarma Wrap","Tuna Melt","pastrami"]



finished_sandwiches = []
print("Sorry pastrami is out of order \n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made {current_sandwich} for you\n")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"The finished sandwiches are : {sandwich}")


dream_places = {}

poll_active = True
print("If you could visit one place in the world where would you go?\n")
while poll_active:
    name = input("Enter your name to enter into the poll\n")
    fav_destination = input("Enter your favorite destination\n")

    dream_places[name] = fav_destination
    response = input("if you would like other person to enter into the poll say 'yes' otherwise 'no'\n")
    if response == "no":
        poll_active = False
    
    print("The person and their fav places\n")

    for name,destination in dream_places.items():
        print(f"{name} likes to visit {destination}\n")

    


    


    

