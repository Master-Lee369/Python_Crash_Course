import user_import

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self,):
        print(f"The privileges of and Admin are\n")
        for privilege in self.privileges:
            print(f"{privilege}")

    
class Admin(user_import.User):
    def __init__(self,first_name, last_name, age, gender, country,privileges):
        super().__init__(first_name, last_name, age, gender, country)
        self.privileges = privileges
        self.privilege = Privileges(privileges)


