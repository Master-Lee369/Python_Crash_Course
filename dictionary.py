person = {
    "first_name" : "sooraj",
    "last_name"  : "sv",
    "age"        :  27,
    "city"       :  "kannur",
}

print(person)

fav_number = {
    "amrutha" : 369,
    "jishnu"  : 11,
    "sajith"  : 93,
    "mahesh"  : 10,
    "Lybu"    : 12,
    "sachu"   : 8,
}

print(fav_number)

glossarry = {
    "Lists" : "lists are used to store data",
    "Tuple" : "Tuples are used to store data but not dynamic",
    "insert": "insert is used to insert particular value in list",
    "loop"  : "loop is used to iterate through list or any linear data types",
    "if"    : "if is a conditional statement used to check the condition which is true or false",
    "set"   : "set is used to store unique data sets",
    "print" : "print is used to print the desired output",
    
}

for term,value in glossarry.items():
    print(f"{term} : {value}")


rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Danube": "Germany",
    "Ganges": "India",
    "Thames": "United Kingdom",
    "Volga": "Russia",
    "Mekong": "Vietnam",
    "Seine": "France"
}

for key, value in rivers.items():
    print(f"The {key} runs through {value}\n")

for river in rivers.keys():
    print(f"The river is  {river}\n")

for river in rivers:
    print(f"The name of the rivers is {river}\n")

for country in rivers.values():
    print(f"The country in which the river passes through is {country}\n")



favorite_languages = {
    "Alice": "Python",
    "Bob": "JavaScript",
    "Charlie": "C++",
    "Diana": "Rust",
    "Eve": "Go",
    "Frank": "Java",
    "Grace": "Swift",
    "Henry": "TypeScript",
    "Isabel": "Kotlin",
    "Jack": "Ruby"
}


names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry","Isabel", "Jack","sooraj", "Lakshmi", "Ritwik", "adithya","Amrutha" ]

for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you {name} for participating in the pole\n")
    else:
        print(f"Hi we are inviting {name} to take the pole\n") 

 

person_1 = {
    "first_name" : "sooraj",
    "last_name"  : "sv",
    "age"        :  27,
    "city"       :  "kannur",
}
person_2 = {
    "first_name" : "Ritwik",
    "last_name"  : "Adoor",
    "age"        :  25,
    "city"       : "kannur",
}

person_3 = {
    "first_name" : "Hari",
    "last_name"  : "krsihna",
    "age"        :  28,
    "city"       :  "TVM",
} 

person_4 = {
    "first_name" : "Ajith",
    "last_name"  :  "kumar",
    "age"        :  27,
}

 
titles = ["person_1", "person_2", "person_3", "person_4"]

people = [person_1, person_2, person_3, person_4]

for person,title in zip(people,titles):
    print(f"{title}'s details are below\n")
    for key, value in person.items():
        print(f" {key} : {value}")


pet_1 = {
    "animal": "dog",
    "owner": "sooraj",
}

pet_2 = {
    "animal": "cat",
    "owner": "ritwik",
}

pet_3 = {
    "animal": "rabbit",
    "owner": "hari",
}

pet_4 = {
    "animal": "parrot",
    "owner": "ajith",
}

pet_5 = {
    "animal": "hamster",
    "owner": "shreya",
}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
        print(f"{pet['owner']} owns a {pet['animal']}.")

for pet in pets:
    for key , value in pet.items():
        print(f"{key} : {value}")


fav_places = {
    "Mahesh"  : ["manali", "varanasi", "kodaikanal"],
    "adithya" : ["spiti valley", "kedarnath", "Daramshala"],
    "shaija"  : ["munnar", "hariharfort", "rameshwaram"],
}

for key, value in fav_places.items():
     print(f"{key}'s fav places are {value}" )


fav_numbers = {
    "amrutha" : [369,7,4,55,808] ,
    "jishnu"  : [11,66,888,777,768],
    "sajith"  : [93,1111,2222],
    "mahesh"  : [10,741],
    "Lybu"    : [12,0000,369,9999,5555],
    "sachu"   : [8,1001],
}

for key,value in fav_numbers.items():
    print(f"{key}'fav numbers are {value}\n")


cities = {
    "Paris": {
        "country": "France",
        "population": 2140526,
        "fact": "Home to the Eiffel Tower and the Louvre Museum.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "Largest metropolitan area in the world and hosts the Tsukiji fish market.",
    },
    "Sydney": {
        "country": "Australia",
        "population": 5325950,
        "fact": "Famous for its Sydney Opera House and Harbour Bridge.",
    },
        "New York": {
        "country": "United States",
        "population": 8419600,
        "fact": "Known as 'The Big Apple' and home to Times Square and Central Park.",
    },
    "Rio de Janeiro": {
        "country": "Brazil",
        "population": 6748000,
        "fact": "Famous for its Copacabana Beach and the Christ the Redeemer statue.",
    },
    "Mumbai": {
        "country": "India",
        "population": 20185064,
        "fact": "Center of India's Bollywood film industry and built on seven islands.",
    },
    "Cairo": {
        "country": "Egypt",
        "population": 10230350,
        "fact": "Location of the Great Pyramids of Giza and the Nile River.",
    },
    "London": {
        "country": "United Kingdom",
        "population": 8982000,
        "fact": "Known for the Tower of London, Big Ben, and diverse culture.",
    }
}

for city,info in cities.items():
    print(f"{city.upper()}\n")
    print(f"country : {info["country"]}\n")
    print(f"population : {info["population"]}\n")
    print(f"fact : {info["fact"]}\n")

for city, info in cities.items():
    print(f"City: {city}")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
    print()

import json

for city, info in cities.items():
    print(f"{city}:")
    print(json.dumps(info, indent=2))
    print()



