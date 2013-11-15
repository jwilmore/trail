from Store import Purchase
import random

class Storage(Purchase):
    def __init__(self, store):
        self.money = store.money
        self.food = store.food
        self.bullets = store.bullets
        self.oxen = store.oxen
        self.clothing = store.clothing
        self.tongues = store.tongues
        self.wheels = store.wheels
        self.axels = store.axels

class RateofMovement(object):
    def choose_rate(self):
        while True:
            self.choice = int(raw_input("Choose Rate of Travel: \n1: Steady Pace (15mi / day) \n2: Faster Rate (20mi / day) \n3: Super Fast Rate (25mi / day)"))
            if self.choice < 1 or self.choice > 3:
                print "Invalid choice, please choose again"
            else:
                break
        if self.choice == 1:
            self.rate = 15
            self.wagon_health = 1
        elif self.choice == 2:
            self.rate = 20
            self.wagon_health = 2
        else:
            self.rate = 25
            self.wagon_health = 3
class RateofFoodConsumption(object):
    def choose_rate(self):
        while True:
            self.choice = int(raw_input("Choose a rate of Food Consumption: \n1: Filling (15lbs / day) \n2: Meager (10lbs / day) \n3: Bare Bones (5lbs / day)"))
            if self.choice < 1 or self.choice > 3:
                print "Invalid choice, please choose again"
            else:
                break
        if self.choice == 1:
            self.eating = 15
            self.food_health = 1
        elif self.choice == 2:
            self.eating = 10
            self.food_health = 2
        else:
            self.eating = 5
            self.food_health = 3

class Movement(RateofMovement, RateofFoodConsumption, Storage):
    date = 0
    def __init__(self, storage):
        self.miles_to_go = 2500
        self.food = storage.food
    def add_one_day(self, rate, eat):
        self.date += 1
        self.rate = rate.rate
        self.miles_to_go -= self.rate
        self.food -= eat.eating


class RandomEvent(RateofFoodConsumption, RateofMovement, Storage):
    def __init__(self, rate, eat):
        self.health_event = eat.food_health
        self.wagon_event = rate.wagon_health
    def event(self):
        if random.random() > .1:
            if random.random() > .5:
                if random.random() * self.health_event > .8:
                    print "A mamber has died"
                else:
                    print "There was a health scare, but everyone is fine"
            else:
                if random.random() * self.wagon_event > .8:
                    if random.random() > .8:
                        print "Wagon busted"
                    else:
                        print "You almost broke the wagon"
                
        else:
            pass
            
