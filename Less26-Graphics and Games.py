import pygame

max_X = 800
max_Y = 600
game_over = False
bg_color = (0, 10, 0)#set a background color to BLACK 0-red 10-green 0-blue

pygame.init()

screen = pygame.display.set_mode((max_X, max_Y), pygame.FULLSCREEN)#set a dimentions of the screen
pygame.display.set_caption("My First PyGame: i)")#name of the widow

#pygame understand just png format
myimage = pygame.image.load("home.png")#load an image ProcessorI7.png, convert - its something what accelerate a loading of an image
pygame.transform.scale(myimage,(10,10)) #transforms loaded image to dimensions 100x100

x = 400#coord X where image will be loaded
y = 300#coord Y where image will be loaded

# ----MAIN GAME LOOP----:
while game_over == False:#during a game_over is't set

    for event in pygame.event.get():#receive some event
        if event.type == pygame.KEYDOWN:#event 1 is press of button
            if event.key == pygame.K_ESCAPE:#if pressed ESC than game_over True, means it will work
                game_over = True
            if event.key == pygame.K_LEFT:#if pressed LEFT button than move image to left 100 by X
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y += 10
            if event.key == pygame.K_DOWN:
                y -= 10

        if event.type == pygame.MOUSEBUTTONDOWN:#event 2 is a press mouse button
            x, y = event.pos#once mouse button pressed, than move image to a position where was pressed button of the mouse

    screen.fill(bg_color)#fill the screen with bg_color every time when image position changed
    screen.blit(myimage, (x,y))#load image to X Y position
    pygame.display.flip()#It allows only a portion of the screen to be updated, instead of the entire area