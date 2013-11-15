class Purchase(object):
    def __init__(self, money):
        self.money = money
        self.food = 0
        self.bullets = 0
        self.oxen = 0
        self.clothing = 0
        self.tongues = 0
        self.wheels = 0
        self.axels = 0
    def purchase(self):
        def buy_food():
            print "You currenly have " + str(self.food) + " pounds of food and " + str(self.money) + " dollars to spend."
            added_food = int(raw_input("How much food would you like?  It is $0.5 per pound."))
            self.money -= (added_food * .5)
            self.food += added_food
            return self.food, self.money
        def buy_bullets():
            print "You currently have " +str(self.bullets) + " bullets and " + str(self.money) + " dollars to spend."
            added_bullets = int(raw_input("How many bullets would you like?  It is $0.10 per bullet."))
            self.money = self.money - (added_bullets * .1)
            self.bullets += added_bullets
            return self.bullets, self.money
        def buy_oxen():
            print "You currently have " +str(self.oxen) + " oxen."
            added_oxen = int(raw_input("How many oxen would you like?  It is $20 per oxen."))
            self.money -= (added_oxen * 20)
            self.oxen += added_oxen
            return self.oxen, self.money
        def buy_clothing():
            print "You currently have " +str(self.clothing) + " pairs of clothing."
            added_clothing = int(raw_input("How many sets of clothing would you like?  It is $10 per set."))
            self.clothing += added_clothing
            self.money -= (added_clothing * 10)
            return self.clothing, self.money
        def buy_spare_parts():
            print "You currently have " +str(self.tongues) + " tongues, " + str(self.wheels) + " wheels, and " + str(self.axels) + " axels."
            added_tongues = int(raw_input("How many spare wagon tongues would you like?  It is $10 per tongue."))
            added_wheels = int(raw_input("How many spare wheels would you like?  It is $15 per wheel."))
            added_axels = int(raw_input("How many spare axels would you like?  It is $10 per axel."))
            self.tongues += added_tongues
            self.wheels += added_wheels
            self.axels += added_axels
            self.money -= ((added_tongues*10) + (added_wheels*15) + (added_axels*10))
            return self.tongues, self.wheels, self.axels, self.money

        loop = 0
        while loop == 0:
            store_choice = int(raw_input("What would you like to buy? \n\n 1: Food \n 2: Bullets \n 3: Oxen \n 4: Clothing \n 5: Spare Parts \n 6: Leave Store"))
            if store_choice <1 or store_choice > 6:
                print "This is not a valid choice.  Please choose again!"
            if store_choice == 6:
                print "You have left the store.  You have the following items with you: \nFood: " +str(self.food) + " pounds \nBullets: " +str(self.bullets) + " rounds \nOxen: " +str(self.oxen) + "\nClothing: " +str(self.clothing) + " pairs \nTongues: " +str(self.tongues) + "\nWheels: " +str(self.wheels) + "\nAxels: " +str(self.axels) + "\nMoney: " + str(self.money)
                loop += 1
            if store_choice == 1:
                food, money = buy_food()
                print "You now have " + str(self.food) + " pounds of food."
                print "You have " + str(self.money) + " dollars remaining."
            if store_choice == 2:
                bullets, money = buy_bullets()
                print "You now have " + str(self.bullets) + " bullets."
                print "You have " + str(self.money) + " dollars remaining."
            if store_choice == 3:
                oxen, money = buy_oxen()
                print "You now have " + str(self.oxen) + " oxen. \n" "You have " + str(self.money) + " dollars remaining."
            if store_choice == 4:
                clothing, money = buy_clothing()
                print "You now have " + str(self.clothing) + " sets of clothing. \n You have " + str(self.money) + " dollars remaining."
            if store_choice == 5:
                tongues, wheels, axels, money = buy_spare_parts()
                print "You now have " +str(self.tongues) + " wagon tongues, " + str(self.wheels) + " wheels, and " + str(self.axels) + " axels. \nYou have " + str(self.money) + " dollars remaining."
            
        
