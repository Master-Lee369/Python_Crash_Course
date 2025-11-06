from printing_functions import car_info


def display_message():
    # function body 
    print("Working on functions,Lets blast\n")


display_message()

def fav_book(book_name):
    print(f"my favorite book is {book_name}\n")

fav_book("The book of secrets\n")

def make_shirt(size, text):
    print(f"The shirt size is {size},' {text} 'is the message printed on it\n")

make_shirt(32,"iam a python developer")
make_shirt(size = 34, text = "i am a genius")

def make_shirt(text= "i love python",size = "large"):
    print(f"The shirt size is {size}, '{text}'is the message\n")

    
make_shirt()
make_shirt(size= "medium")
make_shirt(text= "Just Do it\n")

def describe_city(city,country = "india"):
    print(f"The {city} is in {country}\n")

describe_city("kerala",)
describe_city("Amsterdam","canada")
describe_city("manali",)

def city_country(city,country):
    value = f"{city}, {country}"
    return value

result1 = city_country("Santiago","Chile")
result2 = city_country("kerala","India")
result3 = city_country("Paris","France")
result4 = city_country("Manchester","England")

print(result2)
print(result3)
print(result1)
print(result4)

def make_album(artist_name,album_title,make_album = None):
    dictn = {"aritst" : artist_name, "album" :album_title}
    if make_album:
        dictn["song_count"] = make_album
    return dictn

dict_value1 = make_album("Pink Floyd","The Dark Side Of the Moon")
dict_value2 = make_album("The Beatles","Abbey Road",5)
dict_value3 = make_album("Nirvana","Nevermind")
dict_value4 = make_album("Daft Punk","Random Access Memory",13)
dict_value5 = make_album("Kendrik Lamar","To Pimp a Butterfly")


print(dict_value4)
print(dict_value5)
print(dict_value1)
print(dict_value2)
print(dict_value3)

while True:
    artist_name = input("Please Enter your favorite album's artist name\n")
    album_title = input("Enter your favorite album name\n")
    exit_value = input("please enter 'q' to stop \n")
    result = make_album(artist_name,album_title)
    if exit_value == "q":
        break



def show_messages(message):
    for msg in messages:
        print(f"The messages are \n")
        print(f"{msg}\n")


messages = [
    "Hey! What’s up?",
    "Did you see the news today?",
    "On my way!",
    "Just finished work.",
    "Lunch break! 🍔",
    "Call me when you’re free.",
    "LOL, that was funny!",
    "Let’s meet at 6?",
    "How’s your project going?",
    "Need help with anything?",
    "Can’t talk right now, ttyl.",
    "Got your message, thanks!",
    "See you soon!",
    "Any updates?",
    "Let me know if you’re coming."
]

show_messages(messages)

messages_copy = messages[:]
sent_messages = []

def send_messages(messages):
    while messages:
        message = messages.pop()
        print(f"{message}")
        sent_messages.append(message)


send_messages(messages_copy)
print(messages)
print(sent_messages)
# calling with copy of the list
show_messages(messages_copy)
# The messages are retained because copy of messages has been passed to the function.
print(messages)

    

def items(*arb):
    for i in arb:
        print(f"The sandwich contains {i}\n")



items("pepper")
items("pepperoni, mushroom, paneer")



def build_profile(first_name, last_name,**user_info):
    """ Build a function containing everything we know about everything"""
    user_info['first_name'] = first_name
    user_info["last_name"]  = last_name
    return user_info

user_info = build_profile("Master", "Lee", Position = "Life coach", Place = "Trivandrum", Passion = "creativity")
    
print(user_info)


car = car_info("land_rover","defender",color="green", year="2018")
print(car)