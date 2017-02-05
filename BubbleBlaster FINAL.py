#Bubble Shooter
#Gavin and Jacky
from pygame import*
from math import*
from random import*
import operator
display.set_icon(image.load("images/icon.png"))
##BUTTONS##
playButton = Rect(40,280,190,60) #collide point for play button
instrButton = Rect(55,530,300,40) #collide point for instructions
menuButton = Rect(55,490,290,100) # collide point for menu after victory screen
controllerButton = Rect(140,430,190,100) #collide point for controller in main menu 
##SOUNDS##
mixer.init()
popSound = mixer.Sound("bubblepop.wav") # popping sound
shootSound = mixer.Sound("shoot.wav") #firing sound
themeSong = mixer.Sound("theme.wav")#background song
themeSong.play(-1)

##VARIABLES##
screenWidth = 390
screenHeight = 670
screen=display.set_mode((screenWidth,screenHeight))
halfWidth = screenWidth/2
halfHeight = screenHeight/2
canvasWidth = 330
canvasHeight = 610
halfWidthC = 330//2
halfHeightC = 610//2
ballDiameter = 30
ballRadius = int(ballDiameter//2)
cannonAngle = 90
cannongearAngle = 0
levelCounter=0
bubbleTrue=[]
totalTime=0
levelTime=0

#Fonts#
font.init()
ImpactFont = font.SysFont("Impact", 35)
ImpactFontSmall = font.SysFont("Impact", 16)

##LOADING IMAGES##

background = image.load("images//background.jpg")
victory = image.load("images//victory.jpg")
menuBack = image.load("images//home.jpg")
cannonPointer = image.load("images//cannonPointer.png")
#cannonBase = image.load("images//cannonBase.png")
cannonGear = image.load("images//cannonGear.png")
instructions= image.load("images//instructions.jpg")
orangeBub = image.load("images//orangeBub.png")
yellowBub = image.load("images//yellowBub.png")
blueBub = image.load("images//blueBub.png")
purpleBub = image.load("images//purpleBub.png")
redBub = image.load("images//redBub.png")
greenBub = image.load("images//greenBub.png")
endBub = image.load("images//endBub.png")
                    
##COLOURS##
orange = [255,128,0]
yellow = [255,255,0]
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
black = [0,0,0]
listColours=[1,2,3,4,5,6,7]

##SHOOTING VARIABLES##
X = 0 #x-pos
Y = 1 #y-pos
VX = 2 #x velocity
VY = 3 #y velocity
C = 4 #colour
power=5
cannonX = halfWidth #center cannon in the middle
cannonY = 585 #cannon touches bottom of screen
shotLive=False #flag for if a ball is in air or not
shotf = [halfWidth,cannonY,0,0,choice(listColours)] #variables for bubbles in motion
#Highscore#  We attempted but did not have enough time to finish
##highscores = open("highscores.txt").read().strip().split('\n')
scores=[]
##for line in highscores:
##    n,s=line.strip().split("\t")
##    scores.append([n,s])
userScore=[]

###################
bubFall=[] #bubbles that are to fall
bubblesList=    [[0,0,0,0,0,0,0,0,0,0,0], #bubbleslist manipulated to find value of each ball that is live
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0]]

centersList=    [[0,0,0,0,0,0,0,0,0,0,0], #centerslist made for coordinates to blit too
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0]]
##LEVELS## 
level1= [[2,2,5,5,1,1,1,5,5,2,2], # premade levels 1-10
          [2,2,5,5,1,1,5,5,2,2],
         [3,3,4,4,6,6,6,4,4,3,3],
          [3,3,4,4,6,6,4,4,3,3],
         [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0]]

level2= [[0, 0, 2, 2, 2, 0, 1, 1, 1, 0, 0],
           [0, 2, 0, 0, 2, 1, 0, 0, 1, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           [0, 2, 4, 4, 5, 5, 4, 4, 1, 0],
         [0, 0, 2, 6, 6, 5, 3, 3, 1, 0, 0],
           [0, 0, 2, 6, 6, 3, 3, 1, 0, 0],
         [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0],
           [0, 0, 0, 5, 5, 5, 5, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


level3= [[0, 0, 0, 4, 4, 0, 6, 6, 0, 0, 0],
 [0, 0, 4, 4, 4, 6, 6, 6, 0, 0],
 [0, 0, 0, 4, 4, 3, 6, 6, 0, 0, 0],
 [0, 0, 2, 2, 3, 3, 5, 5, 0, 0],
 [0, 0, 2, 2, 3, 3, 3, 5, 5, 0, 0],
 [0, 2, 2, 3, 3, 3, 3, 5, 5, 0],
 [0, 5, 5, 3, 3, 3, 3, 3, 2, 2, 0],
 [0, 5, 5, 3, 3, 3, 3, 2, 2, 0],
 [0, 0, 5, 5, 3, 3, 3, 2, 2, 0, 0],
 [0, 0, 0, 0, 3, 3, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level4=[[1, 1, 4, 1, 1, 1, 1, 1, 4, 1, 1],
 [2, 2, 4, 2, 2, 2, 2, 4, 2, 2],
 [3, 3, 3, 4, 3, 3, 3, 4, 3, 3, 3],
 [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
 [5, 5, 5, 5, 4, 5, 4, 5, 5, 5, 5],
 [6, 6, 6, 6, 4, 4, 6, 6, 6, 6],
 [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level5=[[4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3],
 [4, 3, 3, 3, 4, 3, 4, 4, 4, 3],
 [4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3],
 [5, 5, 5, 5, 5, 6, 6, 6, 6, 6],
 [5, 6, 6, 6, 6, 5, 6, 5, 5, 5, 6],
 [5, 5, 5, 5, 5, 6, 6, 6, 6, 6],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level6=[[4, 4, 5, 1, 2, 6, 3, 4, 5, 1, 2],
 [4, 5, 1, 2, 6, 3, 4, 5, 1, 2],
 [4, 5, 1, 2, 6, 3, 4, 5, 1, 2, 6],
 [5, 1, 2, 6, 3, 4, 5, 1, 2, 6],
 [5, 1, 2, 6, 3, 4, 5, 1, 2, 6, 6],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level7=[[3, 3, 3, 6, 3, 3, 3, 6, 3, 3, 3],
 [3, 3, 6, 6, 3, 3, 6, 6, 3, 3],
 [3, 3, 3, 6, 3, 3, 3, 6, 3, 3, 3],
 [0, 0, 5, 2, 0, 0, 5, 2, 0, 0],
 [0, 0, 5, 0, 2, 0, 5, 0, 2, 0, 0],
 [0, 5, 0, 0, 2, 5, 0, 0, 2, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level8=[[0, 0, 0, 4, 2, 2, 2, 2, 0, 0, 0],
 [0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 4, 0, 0, 3, 3, 0, 5, 0, 1, 0],
 [4, 0, 0, 0, 3, 6, 5, 6, 1, 6],
 [4, 3, 3, 3, 3, 6, 5, 0, 1, 0, 0],
 [0, 0, 0, 0, 6, 5, 0, 1, 0, 0],
 [0, 0, 0, 0, 6, 5, 6, 1, 6, 0, 0],
 [0, 0, 0, 0, 5, 0, 1, 6, 0, 0],
 [0, 0, 0, 0, 5, 0, 1, 6, 0, 0, 0],
 [0, 0, 6, 5, 6, 1, 6, 0, 0, 0],
 [0, 0, 0, 5, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level9=[[0, 0, 0, 0, 3, 0, 4, 4, 4, 4, 0],
 [0, 0, 0, 3, 0, 4, 0, 0, 4, 0],
 [0, 3, 0, 3, 0, 4, 4, 4, 4, 0, 0],
 [3, 3, 3, 0, 4, 0, 0, 4, 0, 0],
 [0, 0, 5, 5, 5, 5, 0, 2, 0, 0, 0],
 [0, 5, 0, 0, 0, 0, 2, 2, 2, 0],
 [0, 5, 0, 0, 0, 0, 2, 2, 0, 0, 0],
 [5, 5, 5, 5, 0, 2, 0, 2, 0, 0],
 [0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 0],
 [0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level10=[[5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5],
 [6, 3, 3, 3, 3, 3, 3, 3, 3, 6],
 [6, 2, 5, 2, 5, 4, 5, 2, 5, 2, 6],
 [6, 2, 6, 3, 4, 4, 3, 6, 2, 6],
 [6, 2, 1, 1, 1, 4, 1, 1, 1, 2, 6],
 [6, 2, 1, 1, 4, 4, 1, 1, 2, 6],
 [6, 2, 1, 1, 5, 5, 5, 1, 1, 2, 6],
 [6, 2, 1, 5, 5, 5, 5, 1, 2, 6],
 [6, 2, 6, 6, 6, 4, 6, 6, 6, 2, 6],
 [6, 2, 6, 6, 4, 4, 6, 6, 2, 6],
 [6, 2, 3, 3, 3, 4, 3, 3, 3, 2, 6],
 [6, 2, 3, 3, 4, 4, 3, 3, 2, 6],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

levels=[level1,level2,level3,level4,level5,level6,level7,level8,level9,level10] #3d list of the levels
bubblesList=[lev[:] for lev in level1] # make deep copy of the level 1 to start with
levelCounter=0 #start levels at 1

#FINDING CENTERS##
for y in range (0,9):
    for x in range (0,11):
        ypos=y*2 #checks all even rows with *2
        centersList [ypos][x]= (45+30*x),(45+50*y)
for y in range (1,9):
    for x in range (0,10):
        ypos=y*2-1#checks all odd rows with *2-1
        centersList [ypos][x]= (ballRadius+45+30*x),(20+50*y)
        
##FUNCTIONS##
def pickCol (): #choose colour of ball based on the percentage of coloured balls live
    global shotf
    global levelTime
    allCols=[]
    for y in range (0,9):
        for x in range (0,11):
            ypos=y*2
            if bubblesList[ypos][x] != 0: #finds all positions that hold balls
                allCols.append(bubblesList[ypos][x]) #adds the colours of all the balls to a list
    for y in range (1,9):
        for x in range (0,10):
            ypos=y*2-1
            if bubblesList[ypos][x] != 0:
                allCols.append(bubblesList[ypos][x])
    shotf[C]=choice(allCols) #chooses a colour from the list of all the colours (with proper ratios)

    
def gameMenu (): #main menu of the game
    global levelTime
    global totalTime
    running = True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running = False
        screen.blit(menuBack,(0,0)) #blits menu screen
        levelTime=0
        totalTime=0
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[0]==1 and playButton.collidepoint(mx,my): #clicking play starts the game
            main()
        if mb[0]==1 and instrButton.collidepoint(mx,my): #clicking controls starts the instructions menu
            instructMenu()
        if mb[0]==1 and controllerButton.collidepoint(mx,my): #clicking controls starts the instructions menu
            instructMenu()
        display.flip()
        
def instructMenu(): #blits instructions
    running = True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running = False
        keys = key.get_pressed()
        if keys[K_ESCAPE]: #pressing escape brings you to the main menu
            gameMenu()
        screen.blit(instructions,(0,0)) #blits the instructions picture
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        display.flip()
def checkVictory(): #keeps track of the level counter and to check for victory
    global levelCounter
    if levelCounter==10:
        return True
    else:
        return False
    
def victoryMenu():#victory menu telling you total time taken and a back to menu button
    global scores
    global UserScore
    userScore.append(["AAA",str(round(totalTime,2))]) #upon completion of game adds the users TOTAL score to userScore
##    for x in range(10):
##        if  scores[x][1]<userScore[x][1]: #checks for any highscores that have been beaten
##            scores[x][1]=userScore[x][1]  #replaces the time of the highscore
##            scores[x][0]=userScore[x][0]  #replaces the initials of the highscore
##    highscores = open("highscores.txt","w") #opens the highscores txt file
##    for x in range(10):
##        highscores.write(str(scores[x][0])+"\t"+str(scores[x][1])) #writes the highscores to a txt file

    winTime = ImpactFont.render("You took: "+str(round(totalTime,2))+"s" , 1, (0,0,0))
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running = False
        screen.blit(victory,(0,0)) #blits the victory
        screen.blit(winTime,(70,200))
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[0]==1 and menuButton.collidepoint(mx,my):
            gameMenu()
        display.flip()
        

def checkLose(): #checks if you crossed the boundary line
    global bubblesList
    global levelCounter
    global levels
    for x in range (0,11):
        if bubblesList[16][x] != 0: # checks every possition in the 16th row which is past the boundary line
            for y in range (0,9):
                for x in range (0,11):
                    ypos=y*2
                    if bubblesList[ypos][x] != 0:
                        bubblesList[ypos][x]=7 #if a value is found past the boundary line all bubs will turn into bombs
            for y in range (1,9):
                for x in range (0,10):
                    ypos=y*2-1
                    if bubblesList[ypos][x] != 0:
                        bubblesList[ypos][x]=7
            drawScene() #draws the scene with the updated bombs insteaded of bubbles
            display.flip()
            time.wait(500) #waits half a second
            bubblesList= [lev[:] for lev in levels[levelCounter]] #then resets the level
            
            return True
    return False

def checkWin():#checks if the board has been cleared or not
    global bubblesList
    global levelCounter
    global levelTime
    global userScore
    stageClear=True #Starts off by assuming the stage is clear
    for y in range (0,9): #Scans through all positions in bubbles list
        for x in range (0,11):
            ypos=y*2
            if bubblesList[ypos][x] != 0: #if any position in the list has a bubble in it knows the stage is not clear
                stageClear=False
    for y in range (1,9):
        for x in range (0,10):
            ypos=y*2-1
            if bubblesList[ypos][x] != 0:
                stageClear=False
    if stageClear==True:
        screen.blit(background, (0,0))
        userScore.append(["AAA",str(round(levelTime,2))])
        levelTime=0 #time is reset because the level has been beaten
        levelCounter+=1 # if level complete advance to the next level
        if checkVictory()==False:
            bubblesList= [lev[:] for lev in levels[levelCounter]]
        else:
            victoryMenu()#if you passed all 10 levels move on to victoryMenu
    
        
    
def fireShot (): #checks if a ball is shot and at what angle 
    global shotf
    global shotLive
    global cannonAngle
    global cannongearAngle
    keys = key.get_pressed()
    if keys[K_RIGHT]: #user pressing right key subtracts from the cannon angle
        cannonAngle -= 0.5
        cannongearAngle -= 0.5
    elif keys[K_LEFT]: #user pressing left add to the cannon angle
        cannonAngle += 0.5
        cannongearAngle += 0.5
    if cannonAngle==0:cannonAngle=2 #prevents ball from firing horizontally until the end of time
    if cannonAngle==180:cannonAngle=178 #""   ""
    if keys[K_SPACE] and shotLive==False:
        shotf=addShot(360-cannonAngle, power)
        shotLive=True
    moveShots()


def vectToXY(mag, ang): # use trig to solve the angle used to shoot the ball
    rang = radians(ang)
    x = cos(rang) * mag
    y = sin(rang) * mag
    return x,y

def addShot(ang, power):# once the shot is fired add values to the shot to move it across the screen
    global shotf
    shotf[X], shotf[Y] = vectToXY(47,ang)
    shotf[X] += cannonX
    shotf[Y] += cannonY
    shotf[VX], shotf[VY] = vectToXY(power,ang)
    return shotf

def bubbleFall(): #bubbles not attached to the top will fall 
    global bubbleTrue #bubbleTrue will come from floatCheck
    global bubFall
    global bubblesList
    global bubFallC
    for y in range (0,9):
        for x in range (0,11):
            ypos=y*2
            if ((ypos,x)) not in bubbleTrue and bubblesList[ypos][x] !=0: # if a value found that is not true and is not 0 will be changed to 0
                bubblesList[ypos][x]=0
            else:pass
            
    for y in range (1,9):
        for x in range (0,10):
            ypos=y*2-1
            if ((ypos,x)) not in bubbleTrue and bubblesList[ypos][x] !=0:
                bubblesList[ypos][x]=0
            else:pass  

def checkTop(): # checks all bubbles that are currently attached to the top of the screen
    global bubblesList
    global bubbleTrue
    bubbleTrue=[]
    bubbleFloat=[]
    for check in range (0,11):
        if bubblesList[0][check] > 0: # checks top row the 10 bubbles
            bubbleTrue.append((0,check))# if a value if found it must be True so add to bubbleTrue
    for bub in range (len(bubbleTrue)):
        xPos,yPos = bubbleTrue[bub]
        floatCheck(xPos,yPos,bubbleTrue)#each value that is found will be checked in floatcheck for bubbles attached to them 

def floatCheck(x,y,floating): # check if the bubble is connected connected to other bubbles reaching the top 
    global bubblesList
    global bubbleTrue
    bubbleFloat=[]
    for bub in range (len(floating)): #append bubbleFloat list from previous check
        xpos,ypos=floating[bub]
        if (xpos,ypos) not in bubbleTrue: #if value not found append it each time (this is to make sure the same value isn't added several times)
            bubbleTrue.append((xpos,ypos))
    counter=0
    if x==0 and y!= 10 and y!= 0: #special case the bubbles that are not the last bubble in the first row 
        x1,y1=x+1,y-1
        x2,y2=x+1,y
        xVal=[x1,x2]
        yVal=[y1,y2]
    if x==0 and y==10:#special case the last bubble in the first row 
        x1,y1=x+1,y-1
        xVal=[x1]
        yVal=[y1]
    if x==0 and y==0:#special case the first bubble in the first row 
        x1,y1=x+1,y
        xVal=[x1]
        yVal=[y1]
    if (x%2) == 0 and x!=0 and y!=10 and y!=9:#special case for the bubbles that in even rows and not the last or second last bubble
        x1,y1=x-1,y-1
        x2,y2=x-1,y
        x3,y3=x,y+1
        x4,y4=x+1,y
        x5,y5=x+1,y-1
        x6,y6=x,y-1
        xVal=[x1,x2,x3,x4,x5,x6]
        yVal=[y1,y2,y3,y4,y5,y6]
    if (x%2)== 1 and x!=0 and y!=9:#special case for the bubbles that in odd rows and not the last bubble
        x1,y1=x-1,y
        x2,y2=x-1,y+1
        x3,y3=x,y+1
        x4,y4=x+1,y+1
        x5,y5=x+1,y
        x6,y6=x,y-1
        xVal=[x1,x2,x3,x4,x5,x6]
        yVal=[y1,y2,y3,y4,y5,y6]
    elif (x%2) == 0 and y == 10 and x!=0:#special case for the bubbles that in even rows and is the last bubble
        x1,y1=x-1,y-1
        x2,y2=x,y-1
        x3,y3=x+1,y-1
        xVal=[x1,x2,x3]
        yVal=[y1,y2,y3]
    elif (x%2) == 1 and y == 9 and x!=0: #special case for even bubbles that in odd rows and is the last bubble
        x1,y1=x-1,y+1
        x2,y2=x-1,y
        x3,y3=x,y-1
        x4,y4=x+1,y+1
        x5,y5=x+1,y
        xVal=[x1,x2,x3,x4,x5]
        yVal=[y1,y2,y3,y4,y5]
    elif (x%2) == 0 and y == 9 and x!=0: #special case for even bubbles that in even rows and is the second bubble
        x1,y1=x-1,y
        x2,y2=x-1,y-1
        x3,y3=x,y-1
        x4,y4=x+1,y-1
        x5,y5=x+1,y
        x6,y6=x,y+1
        xVal=[x1,x2,x3,x4,x5,x6]
        yVal=[y1,y2,y3,y4,y5,y6]
    for i in range(len(xVal)):
            if bubblesList[xVal[i]][yVal[i]]> 0  and ((xVal[i],yVal[i])) not in bubbleTrue: # if there is a value in bubblesList for a location that is not in bubbleTrue append it
                counter+=1 # flag for if a bubble is added or not
                bubbleTrue.append((xVal[i],yVal[i]))
                if yVal[i] < 0 :# do not allow negative coordinates
                    pass
                else:
                    floatCheck(xVal[i],yVal[i],bubbleTrue)#recursively check all locations that return as true
    if counter==0:
        return
def bubblePop(x,y,c,pop): #checks if the bubble that it collides with should pop or not
    global bubblesList
    global score
    beingPopped=[] # list of all balls that will be removed
    for bub in range (len(pop)): #appends all the bubbles from pop into being popped
        beingPopped.append(pop[bub])
    
    counter=0
    if (x,y) not in beingPopped: # checks if the location of the bubble you're useing is in already in being popped
        
        beingPopped.append((x,y))
    else:pass
    if x==0 and y==0: # special case for if the bubble is in the top left hand corner
        x1,y1=x,y+1 # change x and y input into all the possible options available 
        x2,y2=x+1,y
        c1=bubblesList[x1][y1] # add all colours that will be used
        c2=bubblesList[x2][y2]
        xVal=[x1,x2] #seperate x and y location into 2 lists 
        yVal=[y1,y2]
        cVal=[c1,c2] #colours list
    if (x%2) == 0 and y == 10: # special case for the bubbles on the far right in odd rows
        x1,y1=x-1,y-1
        x2,y2=x,y-1
        x3,y3=x+1,y-1
        c1=bubblesList[x1][y1]
        c2=bubblesList[x2][y2]
        c3=bubblesList[x3][y3]
        xVal=[x1,x2,x3]
        yVal=[y1,y2,y3]
        cVal=[c1,c2,c3]
    elif (x%2) == 1 and y == 9: # special case for bubbles on the far right in even rows
        x1,y1=x-1,y+1
        x2,y2=x-1,y
        x3,y3=x,y-1
        x4,y4=x+1,y+1
        x5,y5=x+1,y
        c1=bubblesList[x1][y1]
        c2=bubblesList[x2][y2]
        c3=bubblesList[x3][y3]
        c4=bubblesList[x4][y4]
        c5=bubblesList[x5][y5]
        xVal=[x1,x2,x3,x4,x5]
        yVal=[y1,y2,y3,y4,y5]
        cVal=[c1,c2,c3,c4,c5]
    elif (x%2) == 0 and y == 9: # special case for the bubbles 1 left from the last bubble in the odd rows 
        x1,y1=x-1,y
        x2,y2=x-1,y-1
        x3,y3=x,y-1
        x4,y4=x+1,y-1
        x5,y5=x+1,y
        x6,y6=x,y+1
        c1=bubblesList[x1][y1]
        c2=bubblesList[x2][y2]
        c3=bubblesList[x3][y3]
        c4=bubblesList[x4][y4]
        c5=bubblesList[x5][y5]
        c6=bubblesList[x6][y6]
        xVal=[x1,x2,x3,x4,x5,x6]
        yVal=[y1,y2,y3,y4,y5,y6]
        cVal=[c1,c2,c3,c4,c5,c6]
    elif (x%2) == 0 : #if bubbles are in an even row 
        x1,y1=x-1,y-1
        x2,y2=x-1,y
        x3,y3=x,y+1
        x4,y4=x+1,y
        x5,y5=x+1,y-1
        x6,y6=x,y-1
        c1=bubblesList[x1][y1]
        c2=bubblesList[x2][y2]
        c3=bubblesList[x3][y3]
        c4=bubblesList[x4][y4]
        c5=bubblesList[x5][y5]
        c6=bubblesList[x6][y6]
        xVal=[x1,x2,x3,x4,x5,x6]
        yVal=[y1,y2,y3,y4,y5,y6]
        cVal=[c1,c2,c3,c4,c5,c6]
    elif (x%2)== 1: # if bubbles are in odd row
        x1,y1=x-1,y
        x2,y2=x-1,y+1
        x3,y3=x,y+1
        x4,y4=x+1,y+1
        x5,y5=x+1,y
        x6,y6=x,y-1
        c1=bubblesList[x1][y1]
        c2=bubblesList[x2][y2]
        c3=bubblesList[x3][y3]
        c4=bubblesList[x4][y4]
        c5=bubblesList[x5][y5]
        c6=bubblesList[x6][y6]
        xVal=[x1,x2,x3,x4,x5,x6]
        yVal=[y1,y2,y3,y4,y5,y6]
        cVal=[c1,c2,c3,c4,c5,c6]
    
    
    
    #for bub in range(len(beingPopped)):
    for i in range(len(xVal)):
        if c==cVal[i] and (xVal[i],yVal[i]) not in beingPopped: #if possible positions is the correct and not in being popped append to being popped 
         # flag to check if something was added to being popped
            if yVal[i] <0: # refuses negative values for y
                pass
            else:
                counter+=1 # if something is found add to a counter
                beingPopped.append((xVal[i],yVal[i]))#if a value was found run through beingPopped again
    else:pass
    
    if counter>0: # If counter is not 0 then recursively recall bubblePop
        
        for bub in range(len(beingPopped)): #run through all bubbles
            xPos,yPos=beingPopped[bub]
            if yPos < 0 : #do not allow negative positions
                pass
            else:
                xPos,yPos=beingPopped[bub]
                bubblePop(xPos,yPos,c,beingPopped)
    if counter==0: # if counter is 0 end the function
       
        if len(beingPopped)>=3: # if there are more then 3 bubbles in being popped they will be removed
            popSound.play() # popping noise
            for i in range(len(beingPopped)): #change values in bubblesList to 0 
                beingPopped[i]=x,y
                bubblesList[x][y]=0 #if 3 or more match turn their values into 0 so they "pop"
        
    
    checkTop()
    bubbleFall()
    

        
    
def checkSnap (x,y,c): # check the location which the bubbles can attach too
    global bubblesList
    global shotf
    snap=[] # keep all location of possible spots
    distances=[] # keep distances of all from possible spots to the bubble shot
    position=[] # keep position in (x,y) coordinates for bubblesList
    
    if x == -1: # special case for if the bubble is touching the top row
        position.append((0,y))
        distances.append((0))
    # %2 used to check if row is odd or even   
    if (x%2) == 0 and y == 10: #special case for if the bubble is in an even row and the last ball
        x1,y1=centersList[x-1][y-1] # get coordinates of possible position the bubble can snap too
        x2,y2=centersList[x][y-1]
        x3,y3=centersList[x+1][y-1]
        snap.append(bubblesList[x-1] [y-1]) # get (x,y) of possible position in bubblesList
        snap.append(bubblesList[x][y-1])
        snap.append(bubblesList[x+1][y-1])
        for check in range (0,3): #adjusted according to how many possible positions there are
            if snap[check]==0:
                if check==0:
                    position.append((x-1,y-1))
                    distances.append((hypot(shotf[X]-x1,shotf[Y]-y1))) # check the distance and append to distances
                if check==1:
                    position.append((x,y-1))
                    distances.append((hypot(shotf[X]-x2,shotf[Y]-y2)))
                if check==2:
                    position.append((x+1,y-1))
                    distances.append((hypot(shotf[X]-x3,shotf[Y]-y3)))      
    elif (x%2) == 1 and y == 9: # special case for even row final bubble
        x1,y1=centersList[x-1][y-1]
        x2,y2=centersList[x-1][y]
        x3,y3=centersList[x][y-1]
        x4,y4=centersList[x+1][y+1]
        x5,y5=centersList[x+1][y]
        snap.append(bubblesList[x-1][y-1])
        snap.append(bubblesList[x-1][y]) 
        snap.append(bubblesList[x][y-1])
        snap.append(bubblesList[x+1][y+1])
        snap.append(bubblesList[x+1][y])
        for check in range (0,5): # For all possible locations add their position and distances to a list
            if snap[check]==0:
                if check==0:
                    position.append((x-1,y-1))
                    distances.append((hypot(shotf[X]-x1,shotf[Y]-y1)))
                if check==1:
                    position.append((x-1,y))
                    distances.append((hypot(shotf[X]-x2,shotf[Y]-y2)))
                if check==2:
                    position.append((x,y-1))
                    distances.append((hypot(shotf[X]-x3,shotf[Y]-y3)))
                if check==4:
                    position.append((x+1,y+1))
                    distances.append((hypot(shotf[X]-x4,shotf[Y]-y4)))
                if check==5:
                    position.append((x+1,y))
                    distances.append((hypot(shotf[X]-x5,shotf[Y]-y5)))
    elif (x%2) ==0 and y == 9:# special case for even row second last bubble
        x1,y1=centersList[x-1][y]
        x2,y2=centersList[x-1][y-1]
        x3,y3=centersList[x][y-1]
        x4,y4=centersList[x+1][y-1]
        x5,y5=centersList[x+1][y]
        x6,y6=centersList[x][y+1]
        snap.append(bubblesList[x-1][y])
        snap.append(bubblesList[x-1][y-1]) 
        snap.append(bubblesList[x][y-1]) 
        snap.append(bubblesList[x+1][y-1])
        snap.append(bubblesList[x+1][y])
        snap.append(bubblesList[x][y+1]) 
        for check in range (0,6):
            if snap[check]==0:
                if check==0:
                    position.append((x-1,y))
                    distances.append((hypot(shotf[X]-x1,shotf[Y]-y1)))
                if check==1:
                    position.append((x-1,y-1))
                    distances.append((hypot(shotf[X]-x2,shotf[Y]-y2)))
                if check==2:
                    position.append((x,y-1))
                    distances.append((hypot(shotf[X]-x3,shotf[Y]-y3)))
                if check==3:
                    position.append((x+1,y-1))
                    distances.append((hypot(shotf[X]-x4,shotf[Y]-y4)))
                if check==4:
                    position.append((x+1,y))
                    distances.append((hypot(shotf[X]-x5,shotf[Y]-y5)))
                if check==4:
                    position.append((x,y+1))
                    distances.append((hypot(shotf[X]-x6,shotf[Y]-y6)))
    elif (x%2)== 0 : # bubbles in the even rows that are not the last or second last bubble
        x1,y1=centersList[x-1][y-1]
        x2,y2=centersList[x-1][y]
        x3,y3=centersList[x][y+1]
        x4,y4=centersList[x+1][y]
        x5,y5=centersList[x+1][y-1]
        x6,y6=centersList[x][y-1]
        snap.append(bubblesList[x-1][y-1])
        snap.append(bubblesList[x-1][y]) 
        snap.append(bubblesList[x][y+1]) 
        snap.append(bubblesList[x+1][y])
        snap.append(bubblesList[x+1][y-1])
        snap.append(bubblesList[x][y-1])
        for check in range (0,6):
            if snap[check]==0:
                if check==0:
                    position.append((x-1,y-1))
                    distances.append((hypot(shotf[X]-x1,shotf[Y]-y1)))
                if check==1:
                    position.append((x-1,y))
                    distances.append((hypot(shotf[X]-x2,shotf[Y]-y2)))
                if check==2:
                    position.append((x,y+1))
                    distances.append((hypot(shotf[X]-x3,shotf[Y]-y3)))
                if check==3:
                    position.append((x+1,y))
                    distances.append((hypot(shotf[X]-x4,shotf[Y]-y4)))
                if check==4:
                    position.append((x+1,y-1))
                    distances.append((hypot(shotf[X]-x5,shotf[Y]-y5)))
                if check==5:
                    position.append((x,y-1))
                    distances.append((hypot(shotf[X]-x6,shotf[Y]-y6)))
    elif (x%2)== 1 and x!=-1 : # bubbles in the odd rows that are not the last bubble
        x1,y1=centersList[x-1][y]
        x2,y2=centersList[x-1][y+1]
        x3,y3=centersList[x][y+1]
        x4,y4=centersList[x+1][y+1]
        x5,y5=centersList[x+1][y]
        x6,y6=centersList[x][y-1]
        snap.append(bubblesList[x-1][y])
        snap.append(bubblesList[x-1][y+1]) 
        snap.append(bubblesList[x][y+1]) 
        snap.append(bubblesList[x+1][y+1])
        snap.append(bubblesList[x+1][y])
        snap.append(bubblesList[x][y-1])
        for check in range (0,6):
            if snap[check]==0:
                if check==0:
                    position.append((x-1,y))
                    distances.append((hypot(shotf[X]-x1,shotf[Y]-y1)))
                if check==1:
                    position.append((x-1,y+1))
                    distances.append((hypot(shotf[X]-x2,shotf[Y]-y2)))
                if check==2:
                    position.append((x,y+1))
                    distances.append((hypot(shotf[X]-x3,shotf[Y]-y3)))
                if check==3:
                    position.append((x+1,y+1))
                    distances.append((hypot(shotf[X]-x4,shotf[Y]-y4)))
                if check==4:
                    position.append((x+1,y))
                    distances.append((hypot(shotf[X]-x5,shotf[Y]-y5)))
                if check==5:
                    position.append((x,y-1))
                    distances.append((hypot(shotf[X]-x6,shotf[Y]-y6)))
    
    posx,posy=position[distances.index(min(distances))] # check position for the bubblelocation with the lowest distance 
    bubblesList[posx][posy]= c #the position is then changed to the value of the shot fired
    shotf = [150,600,0,0,1]
    pop=[]#reset pop value back to nothing
    if checkLose()==False:#as long as you did not lose the game check for bubbles that can pop
        bubblePop(posx,posy,c,pop)
    checkWin()#after bubblepop check if board has been cleared for bubblePop
    pickCol()#choose next cannon shot
    
def moveShots(): #Moves the ball according to angle given and checks what location the ball can snap too
    global shotf
    global shotLive
    global bubblesList
    topBubs=1 #flag for if the ball is touching the top
    if shotf[X] >= screenWidth-45 or shotf[X] <= 45: #reverses the direction of VX when bubble hits either wall
        shotf[VX]= -shotf[VX]
    if shotf[Y] <= 45:
        shotf[VY]=0
        topBubs=0 #if the VY = 0 that means the ball is touching the top of the screen so set topbub= 0
        
    shotf[X] += shotf[VX] #move shot by adding the value of it's velocity to it's location each time
    shotf[Y] += shotf[VY]  
    colourC = shotf[C]
    if colourC==[255,128,0]: #return what the colour of the fired shot is
        colourC=1
    if colourC==[255,255,0]:
        colourC=2
    if colourC==[0,0,255]:
        colourC=3
    if colourC==[0,0,0]:
        colourC=4
    if colourC==[255,0,0]:
        colourC=5
    if colourC==[0,255,0]:
        colourC=6
    if topBubs == 0 : #If the shot is colliding with the top of the screen then allow it to stick to the top
        xpos=shotf[X]//30 #divide the xpos by 30 to figure out where the ball position is relative to the top
        shotLive=False
        if xpos<0:
            checkSnap (-1,(int(xpos)+1),colourC) #since values are always rounded up add 1 to xpos for correct position for values below 0
        else:
            checkSnap (-1,(int(xpos)-1),colourC)#since values are always rounded up subtract 1 from xpos for correct position
        
    else:
        for y in range (0,9):
            for x in range (0,11):
                ypos=y*2 #needs to skip rows
                x1,y1 = centersList[ypos][x] #find the x,y coordinates of all bubbles 
                if bubblesList[ypos][x] > 0 : #only check the distance of the bubbles that are live
                    d=max(hypot(shotf[X]-x1,shotf[Y]-y1),1) #checks the distance between the shot and all bubbles on the screen
                    sx=hypot(shotf[X]-x1,shotf[Y]-y1)*(shotf[X]-x1)/d #x length away from bubbles
                    sy=hypot(shotf[X]-x1,shotf[Y]-y1)*(shotf[Y]-y1)/d #y length away from bubbles
                    if hypot(shotf[X]-x1,shotf[Y]-y1) < 30: #if bubble distance is less the 30 then move on to checkSnap
                        shotf = [shotf[X],shotf[Y],0,0,shotf[C]]
                        shotLive=False
                        checkSnap(ypos,x,colourC)
                
                
        for y in range (1,9): #recheck for odd rows
            for x in range (0,10):
                ypos=y*2-1
                x1,y1 = centersList[ypos][x] 
                if bubblesList[ypos][x] > 0 :
                    d=max(hypot(shotf[X]-x1,shotf[Y]-y1),1)
                    sx=hypot(shotf[X]-x1,shotf[Y]-y1)*(shotf[X]-x1)/d
                    sy=hypot(shotf[X]-x1,shotf[Y]-y1)*(shotf[Y]-y1)/d
                    if hypot(shotf[X]-x1,shotf[Y]-y1) < 30:
                        shotf = [shotf[X],shotf[Y],0,0,shotf[C]]   
                        shotLive=False
                        checkSnap(ypos,x,colourC)


                    
def drawScene():
    global shotf
    global cannonAngle
    global cannongearAngle
    global gameOver
    global bubblesList
    screen.blit(background,(0,0)) 
    if shotLive==False: #draw the next ball you will be shooting next to the cannon
        shotf[X]=halfWidth-40
        shotf[Y]=cannonY+32
    #Timers#
    levelStopwatch = ImpactFontSmall.render("Level: "+str(round(levelTime,2))+"s" , 1, (255,255,255)) #prints the time in the bottom left hand corner
    screen.blit(levelStopwatch,(32,472))
    totalStopwatch = ImpactFontSmall.render("Total: "+str(round(totalTime,2))+"s" , 1, (255,255,255))
    screen.blit(totalStopwatch,(30,492))
    #Canon #blits the cannon based on angle given to it
    rotCannon = transform.rotate(cannonPointer , cannonAngle-90)
    rotCannongear = transform.rotate(cannonGear , cannongearAngle)
    screen.blit(rotCannongear,(halfWidth-rotCannongear.get_width()//2 , canvasHeight-rotCannongear.get_height()//2-10))
    #screen.blit(cannonBase,(halfWidth-cannonBase.get_width()//2 , canvasHeight-cannonBase.get_height()//2-10))
    screen.blit(rotCannon,(halfWidth-rotCannon.get_width()//2 , canvasHeight-rotCannon.get_height()//2-10))
    #Moving Bubble #bubbles that are moving must be shifted down and to the left by 15 because of picture distortion
    if shotf[C]==0:pass
    if shotf[C]==1:
        screen.blit(orangeBub,(shotf[X]-15,shotf[Y]-15))
    if shotf[C]==2:
        screen.blit(yellowBub,(shotf[X]-15,shotf[Y]-15))
    if shotf[C]==3:
        screen.blit(blueBub,(shotf[X]-15,shotf[Y]-15))
    if shotf[C]==4:
        screen.blit(purpleBub,(shotf[X]-15,shotf[Y]-15))
    if shotf[C]==5:
        screen.blit(redBub,(shotf[X]-15,shotf[Y]-15))
    if shotf[C]==6:
        screen.blit(greenBub,(shotf[X]-15,shotf[Y]-15))
        
    #Background Bubbles
    for y in range (0,9):
        for x in range (0,11):
            ypos=y*2
            center=centersList[ypos][x]
            realCenter=tuple(map(operator.sub,center,(15,15))) #centers are based on centers and since we're blitting they must be adjusted using tuple subtraction
            
            if bubblesList [ypos][x]==0:
                pass
            if bubblesList [ypos][x]==1:
                screen.blit(orangeBub,(realCenter))
            if bubblesList [ypos][x]==2:
                screen.blit(yellowBub,(realCenter))
            if bubblesList [ypos][x]==3:
                screen.blit(blueBub,(realCenter))
            if bubblesList [ypos][x]==4:
                screen.blit(purpleBub,(realCenter))
            if bubblesList [ypos][x]==5:
                screen.blit(redBub,(realCenter))
            if bubblesList [ypos][x]==6:
                screen.blit(greenBub,(realCenter))
            if bubblesList [ypos][x]==7:
                screen.blit(endBub,(realCenter))
    for y in range (1,9):
        for x in range (0,10):
            ypos=y*2-1
            center=centersList[ypos][x]
            realCenter=tuple(map(operator.sub,center,(15,15))) #centers are based on centers and since we're blitting they must be adjusted using tuple subtraction
            
            if bubblesList [ypos][x]==0:
                pass
            if bubblesList [ypos][x]==1:
                screen.blit(orangeBub,(realCenter))
            if bubblesList [ypos][x]==2:
                screen.blit(yellowBub,(realCenter))
            if bubblesList [ypos][x]==3:
                screen.blit(blueBub,(realCenter))
            if bubblesList [ypos][x]==4:
                screen.blit(purpleBub,(realCenter))
            if bubblesList [ypos][x]==5:
                screen.blit(redBub,(realCenter))
            if bubblesList [ypos][x]==6:
                screen.blit(greenBub,(realCenter))
            if bubblesList [ypos][x]==7:
                screen.blit(endBub,(realCenter))
            
            
    

#MAIN GAME#
keys = key.get_pressed()
display.set_caption("Bubble Blaster")

def main(): # main function that runs
    
    global totalTime
    global levelTime
    pickCol()#pick cannon shot colour
    myClock = time.Clock()  # constant frame rate
    totalTime=0 #start off the game with 0s time
    levelTime=0
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running = False       
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            gameMenu()
          #120 frames per second timing since it caused less lag
        levelTime+=1/120
        totalTime+=1/120
        fireShot()#moves the shot and checks popping and falling and victory
        drawScene()#draws what happens after fireshot
        display.flip()#you gotta flip those images :)
         
gameMenu()
    
quit ()
