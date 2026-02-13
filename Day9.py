#Animal_Sound_System

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()

#Decorator_Permission

def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper


@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard")

dashboard("admin")

dashboard("user")

#Student_College_System

class Student:
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("-------------------")

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Aegon", 101)
s2 = Student("Duncan", 102)

s1.display()
s2.display()

Student.change_college("XYZ Engineering College")

s1.display()
s2.display()

print("Aegon Result:", Student.is_pass(78))
print("Duncan Result:", Student.is_pass(30))
