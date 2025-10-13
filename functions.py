def display_message():
    """ function body """
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
