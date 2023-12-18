#LESSON17 Class
print('============Lesson17-Class===============')
class hero(): #create class hero for our game
    def __init__(self, name, level, race): #first function in a class is always __init__
        #self means this object (or same object)
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
# in the first=init function we discribe parameters for that and in
## the next functions we create if it moves or some another actions of it
    def show_hero(self):
        "print all parameters of this hero"
        description = (self.name + ' Level is ' + str(self.level) + ' Race is ' + self.race + ' Health is ' + str(self.health))
        print(description)
    def level_up(self):
        "upgrade level of hero"
        self.level += 1
    def move(self):
        print(self.name + "...start moving...")
    def set_health(self, new_health):
        self.health = new_health
#-----------MAIN hero------------------
myhero1 = hero("Vurdalak", 5, "Orc")
myhero2 = hero("Alex", 5, "Human")
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()

print('============Lesson18-Class part2===============')
"class to create => SuperHero"
class SuperHero(hero): #create subclass SuperHero of class hero
    def __init__(self, name, level, race, magiclevel):
        "Initiate our SuperHero from class hero"
        super().__init__(name, level, race) #this string take data of upper layer
        self.magiclevel = magiclevel
        self.__magic = 100
    def makemagic(self):
        "Use magic"
        self.__magic -= 10
    def showhero(self):
        description = (self.name + ' Level is ' + str(self.level) + ' Race is ' + self.race + ' Health is ' + str(self.health) + ' Magic is ' + str(self.__magic)).title()
        print(description)
#-----------MAIN SuperHero------------------
mysuperhero = SuperHero("Moisey", 27, "Human", 5)
mysuperhero.showhero()
mysuperhero.makemagic()
mysuperhero.showhero()
mysuperhero.magic = 10 # the direct indication of parameter magic
# doesn't work as with __ we blocked the possibilitie to indicate it directly
mysuperhero.showhero()
