from Profession import Professions
from Store import Purchase
from Movement import Movement
from Movement import RateofFoodConsumption
from Movement import RateofMovement
from Movement import Storage
from Movement import RandomEvent
import time
import random

day = 0

# Choosing Profession

profession = Professions()
profession_object = profession.profession()

#Money based upon chosen profession

if profession_object == 1:
    money = 800
elif profession_object == 2:
    money = 600
else:
    money = 400

# Making initial purchases at store

store = Purchase(money)
store.purchase()

# Storage object for money, food, bullets, etc.

storage = Storage(store)

#Movement and possibility of random event

add_a_day = Movement(storage) # creates object that moves the wagon

rate = RateofMovement() # creates object that determines the rate of movement of wagon
rate.choose_rate() # Allows user to choose the rate of movement

eat = RateofFoodConsumption() # Creates object that determines the rate of food consumption
eat.choose_rate() # Allows user to choose the rate of food consumption

event = RandomEvent(rate, eat) # Creates object for a random event

while True:
    add_a_day.add_one_day(rate, eat)
    print "Day: " + str(add_a_day.date)
    print str(add_a_day.miles_to_go) + "miles to go"
    print str(add_a_day.food) + "food remaining"
    if random.random() > .1:
        event.event()
    time.sleep(2)
