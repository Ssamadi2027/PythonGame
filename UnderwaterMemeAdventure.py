from gamelib import *
game=Game(800,700,"AquaticMemez")

#graphics
#Title screen images


      # level background
bk = Image("download.jpg",game)
game.setBackground(bk)
bk.resizeTo(800,700)
    # Title BK

    #play button

play = Image("play.png",game)
play.resizeBy(-40)

            



      #hero image
Hero = Image("submarine.png",game)
Hero.resizeBy(-55)
Hero.draw()
      #Images
explosion = Animation("explosion.png",22,game,1254/22,64)
explosion.visible = False
#bullet
bullet = Animation("bullet.jpg",1,game,225/1,225)
bullet.visible = False
bullet.resizeBy(-85)


Weegee= Image("Weegee.png",game)
Weegee.resizeBy(-100)
Weegee.setSpeed(5,90)
Weegee.moveTo(2500,500)

#final REtArDEd BoSs

F=Font(yellow,50,blue, "Comic Sans MS")



#Blooper wave 2
Blooper = []
for index in range(100):
    Blooper.append(Image("Blooper.png",game))
    
for index in range(100):
    x = randint(5050,17500)
    y = randint(100,700)
    Blooper[index].moveTo(x,y)
    Blooper[index].resizeTo(100,100)
    s = randint(6,8)
    Blooper[index].setSpeed(s,90)
Bullet= []
for index in range(100):
    Bullet.append(Image("BULLETBILL.png",game))
for index in range(100):
    x = randint(1500,17500)
    y = randint(100,700)
    Bullet[index].moveTo(x,y)
    Bullet[index].resizeTo(100,100)
    s = randint(6,8)
    Bullet[index].setSpeed(s,90)


BIGGBOSS= Image("BOSS.png",game)
BIGGBOSS.resizeBy(-50)
BIGGBOSS.moveTo(600,300)
BIGGBOSS.setSpeed(3,0)


'''
#blooper wave 1
blooper = []
for index in range(50):
    blooper.append(Image("Blooper.png",game))
    
    
for index in range(50):
    x =randint(800,5000)
    y =randint(100,800)
    blooper[index].setSpeed(2,90)# angle of zero moves it up
    blooper[index].resizeTo(100,100)
    blooper[index].moveTo(x,y)


'''



#Sound files
move = Sound("damn_you.wav",1)
OUT= Sound("outta_my_way.wav",2)
LAUGH = Sound("krlaugh.wav",3)


#ammo setup
"""
ammo = []
for index in range(1):
    ammo.append(Animation("bullet.jpg",1,game,225/1,225))

for index in range(1):
    x = randint(100,700)
    y = randint(100,4000)
    ammo[index].moveTo(x,-y)
    ammo[index].setSpeed(6,90)
"""
#TITLE SCREEn
while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    
    
    game.drawText("AquATiC MeMeZ AdvEnTurE!!!!!! " , 50,200,F)
    game.update(100)
game.over=False


while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    play.moveTo(700,600)
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True


    


    game.drawText("De StOREy:",250,50,F)
    game.drawText("About 1000 years into the future,a time when memes have become very popular",10,200)
    game.drawText("Suddenly, Communist Euganda Knuckles took over, deported all of the memes to",10,330)
    game.drawText("labor camps, and renamed the nation to MemeLantis",10,360)
    game.drawText("Meanwhile, a guy by the name of Hero, decides to go down to MemeLantis and eliminate",10,390)
    game.drawText("Euganda Knuckles",10,420)
    
    
    

    game.update(100)
game.over=False

while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    play.moveTo(700,600)
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.drawText(" hao too plaey!!!!",250,50,F)
    game.drawText("This game is very simple, just like any other side-scrolling shooter, arrow keys are", 50, 250)
    game.drawText("to move the hero. The space bar is to fire your bullets, and don't worry, you have unliimited ammo",50,270)
    game.drawText("Now thst you understand how to play, move your mouse and click play to start your adventure",50,300)
    
    game.update(100)
game.over=False
    


    
    


    


#Level 1 screen
BlooperKill = 0

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    game.drawText("Level 1",100,50)
    bk.draw()
    Hero.draw()
    Weegee.draw()
    

    bullet.move()

    

    
    Blooper[index].move()

    

    if Hero.collidedWith(mouse) and mouse.LeftClick:
        game.quit()
    


    




    #moving de Gyro
    if keys.Pressed[K_UP]:
        Hero.y -= 4
    if keys.Pressed[K_DOWN]:     
        Hero.y += 4
    if keys.Pressed[K_LEFT]:     
        Hero.x -= 4
    if keys.Pressed[K_RIGHT]:     
        Hero.x += 4
   # if keys.Pressed[K]:
    #    game.quit()
#shooting mechanics and blooper
    #normal blooper
        '''
    for index in range(50):
        blooper[index].move()
        

        if blooper[index].collidedWith(Hero):
            Hero.health-= 1
            explosion.moveTo(Hero.x,Hero.y)
            explosion.visible= True
            OUT.play()
        if keys.Pressed[K_SPACE]:
            bullet.moveTo(Hero.x,Hero.y)
            bullet.setSpeed(25,270)
            bullet.visible = True
        if blooper[index].collidedWith(bullet):
            blooper[index].visible=False
        if Hero.health <1:
            game.over = True
            move.play()
            Hero.visible=False
'''

    Weegee.move(True)
    if Weegee.collidedWith(Hero):
        Hero.health-= 3
    if Weegee.collidedWith(bullet):
        Weegee.visible=False
   
        
        
        
    

    #stronger blooper
    for index in range(100):
        Blooper[index].move()

        
        if Blooper[index].collidedWith(Hero):
            Hero.health-= 1
            explosion.moveTo(Hero.x,Hero.y)
            explosion.visible= True
            OUT.play()
        if keys.Pressed[K_SPACE]:
            bullet.moveTo(Hero.x,Hero.y)
            bullet.setSpeed(25,270)
            bullet.visible = True
        if Blooper[index].collidedWith(bullet):
            Blooper[index].visible=False
            BlooperKill += 1
            bullet.visible=False
        if Hero.health <1:
            move.play()
            Hero.visible=False
            game.quit()

        if BlooperKill >= 25:
            game.over= True
        
        
        

        

    game.drawText("health: " + str(Hero.health), Hero.x-20, Hero.y+50)
    game.drawText("Blooper Kill:" + str(BlooperKill),50,75)

    


   
        



    game.update(100)
game.over=False



#BIGGBOSS LEVEL


while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    game.drawText("Level 2",100,50)
    
    bk.draw()
    Hero.draw()
    BIGGBOSS.draw()
    BIGGBOSS.move(True)
    Bullet[index].move()

    bullet.move()
    if keys.Pressed[K_UP]:
        Hero.y -= 4
    if keys.Pressed[K_DOWN]:     
        Hero.y += 4
    if keys.Pressed[K_LEFT]:     
        Hero.x -= 4
    if keys.Pressed[K_RIGHT]:     
        Hero.x += 4

    if keys.Pressed[K_SPACE]:
        bullet.moveTo(Hero.x,Hero.y)
        bullet.setSpeed(25,270)
        bullet.visible = True
    if Hero.health <1:
        move.play()
        Hero.visible=False
        game.quit()
    for index in range(100):
        Bullet[index].move()
        if Bullet[index].collidedWith(Hero):
            Hero.health-= 1
            explosion.moveTo(Hero.x,Hero.y)
            explosion.visible= True
            OUT.play()

    #BIGGBOSS HEALTH

    if BIGGBOSS.health <1:
        game.over = True
        BIGGBOSS.visible= False
        
        

    if bullet.collidedWith(BIGGBOSS):
        BIGGBOSS.health -= 1
        explosion.visible=True
        explosion.moveTo(BIGGBOSS.x,BIGGBOSS.y)
        LAUGH.play()
    if BIGGBOSS.isOffScreen("top"):
        BIGGBOSS.setSpeed(3,180)
        if BIGGBOSS.isOffScreen("bottom"):
            BIGGBOSS.setSpeed(3,0)
        if BIGGBOSS.isOffScreen("top"):
            BIGGBOSS.setSpeed(3,180)               
        
    game.drawText("health: " + str(Hero.health), Hero.x-20, Hero.y+50)
    game.drawText("BOSS HEALTH:" + str(BIGGBOSS.health),BIGGBOSS.x-20,BIGGBOSS.y+50)

    game.update(60)


game.over=False

while not game.over:
    game.processInput()

    bk.draw()

    if keys.Pressed[K_SPACE]:
        game.quit()
    game.drawText("WHOOOOOO, you just beat Euganda Knuckles and stopped communism",10,200,)
    game.drawText("press spacebar to exit the game if you reach this point of the game",10,400)





    game.update(100)
    
game.over=False 
    



    
    




