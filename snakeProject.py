#This is a simple snake game written in python using the pygame module
#The snake is a list which can be controlled by arrow keys
#After scoring, the speed of snake increases by increasing the framerate
#I have also added features:
#1. full-screen mode 
#2. bonus food(purple) which gives additional 15 points. It should be taken fast as it might disappear

#importing pygame modules
import pygame 
import random

pygame.init()

#defining colors
background_colour = (234, 212, 252)
white = (255, 255, 255)
red = (194, 24, 7)
steelBlue = (0, 137, 252)
greyBlack = (23, 23, 23)
purple = (102, 51, 153)

#Dimensions of window
screenDim = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('Snake Game using PyGame')
clock = pygame.time.Clock()

#defining food_count to give bonus food at every 5th position
food_count = 0
xB = 0
yB = 0
score = 0
frame_count = 0
snake_speed = 10

#defining fonts
font_style = pygame.font.Font("EvilEmpire.ttf", 50)
font_style_score = pygame.font.Font("EvilEmpire.ttf", 35)
font_style_subscore = pygame.font.Font("EvilEmpire.ttf", 20)

#function to print updated score on window
def print_score(color, score, xB, yB):
    msg = "Your Score: "+ str(score)
    mesg = font_style_score.render(msg, True, color)
    screenDim.blit(mesg, [xB+20, yB+20])
    msg2 = "Use arrow keys to move the snake"
    mesg2 = font_style_subscore.render(msg2, True, color)
    screenDim.blit(mesg2, [xB+20, yB+55])
 
#prints 'you lost' when game ends with options
def message(msg,color, xB, yB, _score):
    mesg = font_style.render(msg, True, color)
    screenDim.blit(mesg, [xB+300, yB+275])
    score_display = "Your Score: "+str(_score)
    mesg2 = font_style_score.render(score_display, True, white)
    screenDim.blit(mesg2, [xB+295, yB+330])
    option1 = "q: Quit"
    option2 = "r: Replay" 
    mssg1 = font_style_subscore.render(option1, True, white)
    mssg2 = font_style_subscore.render(option2, True, white)
    screenDim.blit(mssg1, [xB+340, yB+390])
    screenDim.blit(mssg2, [xB+340, yB+420])

#finds the position of every food circle
def updateFood(xB, yB, snake_block):
    global food_count
    x = xB + round(random.randrange(50, (800 - (snake_block+2))) / 10.0) * 10.0
    y = yB + round(random.randrange(100, (600 - (snake_block+2))) / 10.0) * 10.0
    food_count = food_count + 1
    return x, y

#the snake game function
def game_function():
    #declaring variables
    global screenDim
    global food_count
    global screenDim 
    running = True
    global snake_speed
    global frame_count
    global xB
    global yB
    x1 = 400
    y1 = 300
    tempX = -5
    tempY = -5
 
    xFull = 0
    yFull = 0
    x1_change = 0       
    y1_change = 0
    snake_block = 10
    addNode = 0
    global score 

    #the snake is a list which initially contains 1 element
    snake_list = []
    snake_list.append([x1, y1]) 
    foodx, foody=updateFood(xB, yB, snake_block) 
    
    #execution of game
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #the game works in full screen due to this if condition :)
            if event.type == pygame.VIDEORESIZE:
                screenDim = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                screenDim.fill(background_colour) 
                w, h = pygame.display.get_surface().get_size()
                #adjusting position of snake
                if w!=800:
                     xB = (w-800)/2
                     yB = (h-600)/2
                     snake_list[0][0] = snake_list[0][0]+(w-800)/2
                     snake_list[0][1] = snake_list[0][1]+(h-600)/2
                     xFull = w
                     yFull = h
                     foodx = foodx + xB
                     foody = foody + yB
                else:
                    xB = 0
                    yB = 0
                    snake_list[0][0] = snake_list[0][0] -(xFull-w)/2
                    snake_list[0][1] = snake_list[0][1] -(yFull-h)/2
                    foodx-=(xFull-w)/2
                    foody-=(yFull-h)/2
            #responds when a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        #end condition, boundaries for the snake
        if(snake_list[0][0]<=xB or snake_list[0][0]>=(xB+800) or snake_list[0][1]<=yB or snake_list[0][1]>=(yB+600)):
            running = False
            break

        #updating values for snake so that it moves in a regular fashion
        for i in range(len(snake_list)-1, -1, -1):
            point = snake_list[i]
            if(i == range(len(snake_list)-1)):
                tempX=point[0]
                tempY=point[1]
            if(i == 0):
                point[0]+=x1_change
                point[1]+=y1_change
            else:
                prev_point = snake_list[i-1]
                point[0]=prev_point[0]
                point[1]=prev_point[1]
        #a block is added each time snake eats a food circle
        if(addNode == 1):
            snake_list.append([tempX, tempY])
            addNode = 0  

        #drawing everything on the screen
        screenDim.fill(greyBlack)
        pygame.draw.rect(screenDim, background_colour, pygame.Rect(xB, yB, 800, 600))
        pygame.draw.rect(screenDim, greyBlack, pygame.Rect(xB, yB, 800, 600), 3)
        #bonus food also present
        if(food_count%5 == 0):
            pygame.draw.rect(screenDim, purple, [foodx, foody, snake_block, snake_block], 0, 5)
            frame_count+=1
        else:
            pygame.draw.rect(screenDim, steelBlue, [foodx, foody, snake_block, snake_block], 0, 5) 
        for i in range(len(snake_list)):
            pygame.draw.rect(screenDim, greyBlack, pygame.Rect(snake_list[i][0], snake_list[i][1], snake_block, snake_block),  0, 2) 
        print_score(greyBlack, score, xB, yB)
 
        #updating display with changes
        pygame.display.update()
        #increasing speed of snake
        clock.tick(snake_speed)

        #when snake eats food circle
        if(snake_list[0][0]==foodx and snake_list[0][1]==foody):
            if(food_count%5 == 0):
                score = score + 25
            else:
                score = score +10 
            snake_speed+=2
            foodx, foody=updateFood(xB, yB, snake_block)
            addNode = 1
        elif((food_count%5 == 0) and (frame_count == 300)):
            frame_count = 0
            foodx, foody=updateFood(xB, yB, snake_block)

    screenDim.fill(greyBlack)
    message("You lost", red, xB, yB, score)
    pygame.display.update()

#calling the game
game_function()
gameover = 0
#asking the user if they want to replay or quit
while(gameover == 0):  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = False
        if event.type == pygame.VIDEORESIZE:
            screenDim = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screenDim.fill(background_colour) 
            if(event.w!=800):
                xB = (event.w-800)/2
                yB = (event.h-600)/2
            else:
                xB = 0
                yB = 0
            screenDim.fill(greyBlack)
            message("You lost", red, xB, yB, score)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameover = 1
            if event.key == pygame.K_r:
                score = 0
                snake_speed = 10
                game_function()
    pygame.display.update()
pygame.quit()
quit() 