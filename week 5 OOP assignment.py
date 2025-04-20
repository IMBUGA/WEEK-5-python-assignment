# Base Class.
# quiz 1; Design your own class.
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # Battery percentage
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON 🔋({self.battery}%)")
        else:
            print(f"{self.model} is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.model} is now OFF.")
        else:
            print(f"{self.model} is already OFF.")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.model} charged to {self.battery}% 🔌")

    def use_app(self, app_name):
        if self.is_on and self.battery > 0:
            self.battery -= 10
            print(f"Using {app_name} on {self.model}... Battery at {self.battery}% 📱")
        else:
            print(f"{self.model} is off or out of battery! ❌")
            
# Gaming Phones, polymorphic behavior.
# Inherits from Smartphone and overrides the use_app method.
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def use_app(self, app_name):
        if self.is_on and self.battery > 0:
            self.battery -= 15  # Uses more battery
            print(f"Launching high-performance game: {app_name} 🎮")
            print(f"Cooling System: {self.cooling_system} ❄️ | Battery at {self.battery}%")
        else:
            print(f"{self.model} can't run games now. Check power status.")
            
#Example.            
phone1 = Smartphone("Samsung", "Galaxy Note 10+", 80)
phone2 = GamingPhone("Tecno", "Spark XYZ", 100, "Liquid Cooling System 3.0")

phone1.turn_on()
phone1.use_app("LinkedIn")
phone1.charge(15)

phone2.turn_on()
phone2.use_app("Call of Duty Mobile")

#Quiz 2
# Create a program that includes animals or vehicles with the same action (like move()).
#However, make each class define move() differently (for example;
#Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicle:
    def move(self):
        print("The vehicle moves forward.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")
class Motorcycle(Vehicle):
    def move(self):
        print("Zooming through traffic")

vehicles = [Car(), Plane(), Boat(), Motorcycle()]

    # Output:
for v in vehicles:
    v.move()
