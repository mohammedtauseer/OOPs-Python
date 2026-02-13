#Abstraction

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass



class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key ignition.")



class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with self-start button.")



class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started with heavy diesel ignition.")



car = Car()
bike = Bike()
bus = Bus()


car.start_engine()
bike.start_engine()
bus.start_engine()

#Polymorphism

class Payment:
    def pay(self):
        print("Processing generic payment...")



class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay.")



class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe.")



class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card.")



p1 = Payment()
p2 = GooglePay()
p3 = PhonePe()
p4 = CreditCard()


p1.pay()
p2.pay()
p3.pay()
p4.pay()
