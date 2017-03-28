class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
 
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
 
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])
 
class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])
 
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
         
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Thump", "Crash"])
         
    def combust(self):
        for i in range (1, 5):
            print(i)
        print("IM EXPLODING")
 
class Band(Musician):
     
    def __init__(self):
         self.members = []
         self.drummer = None
         
    def hire(self, musician):
        if isinstance(musician, Drummer):
            self.drummer = musician
        else:
            self.members.append(musician)
        
    def fire(self, musician):
        self.members.remove(musician)
        
    def solo(self, length):
        self.drummer.solo(length)
        self.drummer.combust()
        for musician in self.members:
            musician.solo(length)