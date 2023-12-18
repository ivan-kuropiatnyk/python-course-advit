import pygame#import biblio for game programming
import random#import biblio for random digits
import sys#import biblio for system commands
import time#import bibliotheque for a delay(lower speed of snowfall), line time.sleep(0.02)

MAX_X = 800#length of screen
MAX_Y = 600#width of screen
MAX_SNOW = 100#maximal quantity of snows on the screen
SNOW_SIZE = 37#size of image loaded

class Snow():#class discribes snows
    def __init__(self, x, y):#ititialize it as itself on the position x,y
        self.x = x#it's initial posizion by x on the screen
        self.y = y#it's initial posizion by y on the screen
        self.speed = random.randint(1, 3)#initialize a speed of fall wi random digit from 1 to 3
        self.img_num = random.randint(1, 6)#initialize a number of the image which is loaded
        self.image_filename = "goblet" + str(self.img_num) + ".png"#define the name of the image loaded: name+number+format of the file
        self.image = pygame.image.load(self.image_filename).convert()#loads files which is using as images of snows
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))#transform this images to the same size

    def move_snow(self):#describe a function of movements by y (fall)
        self.y = self.y + self.speed#the movement is equal y + speed
        if self.y < 0:
            self.y = (0 + SNOW_SIZE)

        i = random.randint(1, 3)
        if i == 1:#move right
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 2:#move left
            self.x -= 1
            if self.x <= 0:

            if self.x > MAX_X - SNOW_SIZE:
                self.x = MAX_X - SNOW_SIZE

    def draw_snow(self):#method of drawing snows
        screen.blit(self.image, (self.x, self.y))

def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, MAX_X)
        yy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx, yy))

def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()

# ----MAIN GAME LOOP----:
pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 50, 0)
snowfall = []


initialize_snow(MAX_SNOW, snowfall)
while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.02)
    pygame.display.flip()