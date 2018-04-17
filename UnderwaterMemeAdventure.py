from gamelib import *
game=Game(1000,800,"AquaticMemez")

#graphics
#Title screen images


      # level background
bk = Image("download.jpg",game)
game.setBackground(bk)
bk.resizeTo(1000,800)
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
    y = randint(100,800)
    Blooper[index].moveTo(x,y)
    Blooper[index].resizeTo(100,100)
    s = randint(6,8)
    Blooper[index].setSpeed(s,90)
Bullet= []
for index in range(100):
    Bullet.append(Image("BULLETBILL.png",game))
for index in range(100):
    x = randint(1500,17500)
    y = randint(100,800)
    Bullet[index].moveTo(x,y)
    Bullet[index].resizeTo(100,100)
    s = randint(6,8)
    Bullet[index].setSpeed(s,90)


BIGGBOSS= Image("BOSS.png",game)
BIGGBOSS.resizeBy(-50)
BIGGBOSS.moveTo(850,400)
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

    
    
    game.drawText("AquATiC MeMeZ AdvEnTurE!!!!!! " , 200,200,F)
    game.update(100)
game.over=False


while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    play.moveTo(900,700)
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True


    


    game.drawText("De StOREy:",250,100,F)
    game.drawText("Some time into the future, about 1000 years from today. It is a time when memes become really popular",100,220)
    game.drawText("Even the dead memes make a comeback. But one day, Euganda Knuckles became very powerful, relocated the",100,235)
    game.drawText("and converted to communism. His new land is known as MemeLantis. Meanwhile, a young man known as Hero,",100,250)
    game.drawText("finds out that there is valuable treasure in MemeLantis, so he travels all the way to MemeLantis to find the treasure!!",100,265)
    game.drawText("On Hero's journey there will be Euganda Knuckle's henchmen to get rid of intruders",100,280)
    game.drawText("Hero must kill all the evil memes, kill communist Euganda Knuckles and get the treasure",100,305)
    
    
    

    game.update(100)
game.over=False

while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    play.moveTo(900,700)
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.drawText(" hao too plaey!!!!",250,100,F)
    game.drawText("This game is very simple, just like any other side-scrolling shooter, arrow keys are", 100, 250)
    game.drawText("to move the hero. The space bar is to fire your bullets, and don't worry, you have unliimited ammo",100,270)
    game.drawText("Now thst you understand how to play, move your mouse and click play to start your adventure",100,300)

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
            game.quit()
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
        game.over = True
        move.play()
        Hero.visible=False
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


    game.drawText("WHOOOOOO, you just beat Euganda Knuckles and stopped communism",100,200,)
    game.drawText("Here's your treasure!!",100,300,F)





    game.update(100)
    
game.over=False 
    



    
    




