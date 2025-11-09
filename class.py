class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 21

    def describe_restaurant(self,):
        print(f"The famous {self.restaurant_name} contains {self.cuisine_type} cuisine\n")

    def open_restaurant(self,):
        print("The Restaurant is open\n")
    def set_number_served(self,served_number):
        if served_number > self.number_served:
            self.number_served = served_number
            print(f"The number of people have been served by the restaurant is {self.number_served}\n")
    def increment_number_served(self,day_in_customers):
        self.number_served += day_in_customers
        print(f"The total number of cutomers served is {self.number_served}\n")
restaurant = Restaurant("Paragan", "kerala")

restaurant.describe_restaurant()
print(f"The restaurant has served {restaurant.number_served} people\n")
restaurant.open_restaurant()
restaurant.set_number_served(33)
restaurant.increment_number_served(39)

restrnt = Restaurant("Taj", "Mumbai")
restrnt.describe_restaurant()
restnt = Restaurant("Burdell", "Okaland")
restnt.describe_restaurant()


class User:
    def __init__(self,first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age       =  age
        self.gender    =  gender
        self.country   =  country
        self.login_attempts = 0 

    def describe_user(self,):
        print(f"{self.gender} {self.first_name}{self.last_name} has age {self.age} comes from {self.country} ")

    def greet_user(self,):
        print(f"Hi {self.first_name } welcome to the Elite club\n")

    def increment_login_attempt(self,):
        self.login_attempts += 1
    
    def reset_login_attempt(self,):
        self.login_attempts = 0


        
user_obj1 = User("Amrutha", "Sathiyan",28,"female","India")
user_obj2 = User("Tom", "Cruise",49,"male","US")
user_obj3 = User("lavo_se", "tung",57,"male","China")

user_obj1.describe_user()
user_obj1.greet_user()
user_obj2.describe_user()
user_obj2.greet_user()
user_obj3.describe_user()
user_obj3.greet_user()
 
user_obj = User("Master", "Lee", 27, "male", "Bharat")
user_obj.increment_login_attempt()
user_obj.increment_login_attempt()
user_obj.increment_login_attempt()
user_obj.increment_login_attempt()
user_obj.increment_login_attempt()
user_obj.increment_login_attempt()
print(f"The number of login attempts are {user_obj.login_attempts}\n")
user_obj.reset_login_attempt()

print(f"The number of login attempts are {user_obj.login_attempts}\n")


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavours):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = flavours

    def display_flavors(self,):
        print(f"The Flavors are \n")
        for flavor in self.flavours:
            print(f" {flavor}\n")

ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream",
    "Butterscotch",
    "Mango",
    "Pistachio",
    "Caramel Swirl"
]
IceCream_restrnt = IceCreamStand("Mcdonals","US",ice_cream_flavors)
IceCream_restrnt.display_flavors()
privileges = ["can add post", "can delete post", "can ban user", "can change database"]

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self,):
        print(f"The privileges of and Admin are\n")
        for privilege in self.privileges:
            print(f"{privilege}")

    
class Admin(User):
    def __init__(self,first_name, last_name, age, gender, country,privileges):
        super().__init__(first_name, last_name, age, gender, country)
        self.privileges = privileges
        self.privilege = Privileges(privileges)



admin_obj = Admin("Master","Lee",27,"male","India",privileges)
admin_obj.privilege.show_privileges()





