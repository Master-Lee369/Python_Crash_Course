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
