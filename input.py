rental_car = input("What kind of Rental car you would like to Ride\n")
print(f"let me see if i can find you a {rental_car}")



no_people = input("Tell us how many people are in your dinning group\n")

no_people = int(no_people)

if no_people > 8:
    print("Sorry to inform you will have to wait for the table\n")
else:
    print("Happy to inform you, your table is ready\n")


number = input("Enter a number\n")

number = int(number)

if number % 10 == 0:
    print("The number is a multiple of 10\n")
else:
    print("The number is not a multiple of 10\n")