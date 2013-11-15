class Professions(object):
    def profession(self):
        loop = 0
        while loop == 0:
            choice = int(raw_input("1: Banker from Boston \n 2: Carpenter from Virginia \n 3: Farmer from Kentucky"))
            if choice <1 or choice >3:
                print "please enter a valid number between 1 and 3"
            else:
                loop += 1
        return choice
