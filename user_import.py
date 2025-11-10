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
