#Digital_Vault_System

class Vault:
    def __init__(self, password):
        self.__password = password
        self.__is_locked = True

    def unlock(self, password):
        if password == self.__password:
            self.__is_locked = False

    def lock(self):
        self.__is_locked = True

    def is_opened(self):
        return not self.__is_locked
    
v1 = Vault("1234")
v1.unlock("0000")
print( v1.is_opened())

#Online_Store

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def get_discounted_price(self):
        discount = (self.discount_percent / 100) * self.price
        return self.price - discount
    
p1=DiscountedProduct("laptop",1000,20)
print(p1.get_discounted_price())

#Smart_Assistant

class Speaker:
    def speak(self, message):
        return f"Speaking: {message}"

class Scheduler:
    def schedule(self, task, time):
        return f"Scheduled {task} at {time}"

class SmartAssistant(Speaker, Scheduler):
    pass

c1=SmartAssistant()
print(c1.speak("Hello"))
print(c1.schedule("meeting","10:00 AM"))

#Space_Missions

class Robot:
    def communicate(self):
        return "Beep beep."

class ExplorerRobot(Robot):
    def communicate(self):
        return "Exploring new planets!"

r = Robot()
e = ExplorerRobot()
print(r.communicate())
print(e.communicate())
