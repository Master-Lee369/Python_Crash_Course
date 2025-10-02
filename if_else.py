alien_color = "green"

if alien_color == "green":
    print("The player earned 5 points\n")

alien_color = "red"

if alien_color == "green":
    print("The player earned 5 points")

alien_color = "green"

if alien_color == "green":
    print("player just earned 5 points for shooting the alien\n")
else:
    print("Player just earned 10 points\n")

alien_color = "blue"

if alien_color == "green":
    print("player just earned 5 points for shooting the alien\n")
else:
    print("player just earned 10 points\n")

alien_color = "green"

if alien_color == "green":
    print("Player just earned 5 points for shooting the green alien\n")
elif alien_color == "yellow":
    print("Player just earned 10 points for shooting the yellow alien\n")
else:
    print("Player just earned 15 points for shooting the red alien\n ")


alien_color = "yellow"

if alien_color == "green":
    print("Player just earned 5 points for shooting the green alien\n")
elif alien_color == "yellow":
    print("Player just earned 10 points for shooting the yellow alien\n")
else:
    print("Player just earned 15 points for shooting the red alien\n ")


alien_color = "red"

if alien_color == "green":
    print("Player just earned 5 points for shooting the green alien\n")
elif alien_color == "yellow":
    print("Player just earned 10 points for shooting the yellow alien\n")
else:
    print("Player just earned 15 points for shooting the red alien\n ")


age = 27

if age < 2:
    print("The person is a baby\n")
elif age >= 2 and age < 4:
    print("The person is a toddler\n")
elif age >= 4 and age < 13:
    print("The person is a kid\n")
elif age >= 13 and age < 20:
    print("The person is a teenager\n")
elif age >= 20 and age < 65:
    print("The person is an adult\n")
else:
    print("The person is an elder\n")

favorite_fruits = ["pappaya","mango","apple","orange","promogranade","banana"]

if "pappaya" in favorite_fruits:
    print("i really like pappaya\n")
if "apple" in favorite_fruits:
    print("i really like apple\n")
if "mango" in favorite_fruits:
    print("i really like orange\n")


usernames = ["sooraj", "Ritwik", "Ajay", "Hari", "Aditya", "Amarnath","Admin"]

for user in usernames:
    if user is "Admin":
        print("Hello admin would you like to see a status report\n")
    else:
        print(f"Hello {user} thank you for logging in again\n")


usernames = []


if user in usernames:

    for user in usernames:
        if user is "Admin":
            print("Hello admin would you like to see a status report\n")
        else:
            print(f"Hello {user} thank you for logging in again\n")
else:
    print("We need to add some users\n")


current_users = ["alice", "bob", "charlie", "david", "EMMA"]
lcase_users = []

for user in current_users:
    lcase_users.append(user.lower())

print(lcase_users)


new_users = ["frank", "george", "alice", "hannah", "emma"]

for user in new_users:
    if user in lcase_users:
        print(f"The {user} has to enter a new username\n")
    else:
        print("The username is available\n")

for num in range(1,10):
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
print("All numbers has been printed\n")


    
