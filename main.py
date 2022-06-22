class Restaurant:
    """Creating restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        """Initializing restaurant name and cuisine"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Describing info """
        print(f"Restaurant name is {self.name}")
        print(f"The cuisine is {self.type}")

    def number_total(self):
        print(f"Total clients served during business day is {self.number_served}")


    def set_number_served(self,clients):
        self.clients = clients
        print(f"The number of clients served in the morning {self.clients}")

    def open_restaraunt(self):
        print(f"{self.name} is open")

    def increment__number_served(self,total):
        """Adding total number of clients served during business day"""
        self.number_served += total
        
restaraunt = Restaurant('Burger King','fast food')
print(f"Restaurant name is {restaraunt.name}")
print(f"Cuisine type {restaraunt.type}")
restaraunt.describe_restaurant()
restaraunt.open_restaraunt()

class User:
    def __init__ (self,first_name,last_name):
        self.name = first_name
        self.last = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.name} {self.last} added to the database")

    def total_login_attempts(self):
        print(f"Total login attempts are {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hello {self.name} {self.last}!")

user_n = User('Rachel','Love')
print(f"User {user_n.name} {user_n.last} logged in")
user_n.describe_user()
user_n.greet_user()
# 9-4 page 167
print(f"{restaraunt.name.title()} served {restaraunt.number_served} clients today")
restaraunt.set_number_served(25)
restaraunt.increment__number_served(485)
restaraunt.number_total()
restaraunt.increment__number_served(48)
restaraunt.number_total()
restaraunt.increment__number_served(55)
restaraunt.number_total()
# 9-5 page 167
user_n.total_login_attempts()
user_n.increment_login_attempts()
user_n.total_login_attempts()
user_n.increment_login_attempts()
user_n.increment_login_attempts()
user_n.total_login_attempts()
user_n.reset_login_attempts()
user_n.total_login_attempts()
# 9-6 page 173
class IceCreamStand(Restaurant):
    def __init__(self,restaraunt_name,cuisine_type):
        """Initialize attributes of parent class"""
        super().__init__(restaraunt_name,cuisine_type)
        self.flavor = ['vanilla','blueberry','hazelnut']

    def flavor_list(self):
        print(f"{self.name.title()} has following ice cream flavors: {self.flavor}")

ice_cream = IceCreamStand('Starbucks','ice cream')
print(ice_cream.describe_restaurant())
ice_cream.flavor_list()
# 9-7
class Privileges:
    def __init__(self,admin_privileges):
        """Initialize admin privileges"""
        self.admin_privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(f"Admin has following privileges {self.admin_privileges}")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()
    def show_privileges(self):
        print(f"Admin {self.name.title()} {self.last.title()} has the following privileges {self.admin_priviliges}")
admin_user = Admin('fer','fswefhu')
print(admin_user.describe_user())
admin_user.show_privileges()
