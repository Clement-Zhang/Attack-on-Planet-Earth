import pygame
import random
import os
import math


WIDTH=1280
HEIGHT=720
FPS=30
BACKGROUND=(0,0,0)

gameFolder=os.path.dirname(__file__)
playerFolder=os.path.join(gameFolder,"CustomArt\Player")
enemyFolder=os.path.join(gameFolder,"CustomArt\Enemy")

class Player(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=playerImg
                self.rect=self.image.get_rect()
                self.rect.center=(100,HEIGHT/2)
        def update(self):
                moveSpeed=[0,0]
                diag=10*(1/2**.5)
                if control=="1":
                        mouseSpot=pygame.mouse.get_pos()
                        moveSpeed=playerMove(move(self.rect.center,mouseSpot))
                if control=="2":
                        key=pygame.key.get_pressed()
                        a=key[pygame.K_a]
                        d=key[pygame.K_d]
                        w=key[pygame.K_w]
                        s=key[pygame.K_s]
                        if w:
                                moveSpeed=[0,-10]
                        if s:
                                moveSpeed=[0,10]
                self.rect.centery+=moveSpeed[1]
                bound(self.rect)
                
class Enemy(pygame.sprite.Sprite):
        def __init__(self,player):
                pygame.sprite.Sprite.__init__(self)
                self.player=player
                self.image=enemyBlockImg
                self.rect=self.image.get_rect()
                self.rect.center=[WIDTH-100,random.randrange(100,HEIGHT-100)]
                self.moveSpeed=[random.randrange(-10,-4),random.randrange(-4,3)]
        def update(self):
                if self.rect.right>=WIDTH or self.rect.bottom>=HEIGHT or self.rect.left<=0:
                        self.rect.center=[WIDTH-100,random.randrange(100,HEIGHT-100)]
                        self.moveSpeed=[random.randrange(-10,-4),random.randrange(-4,3)]
                self.rect.centerx+=self.moveSpeed[0]
                self.rect.centery+=self.moveSpeed[1]

def move(start,end):
        distX=end[0]-start[0]
        distY=start[1]-end[1]
        if distX==0:
                distX=10^-6
        angle=math.atan2(distY,distX)
        h=math.cos(angle)
        v=-math.sin(angle)
        return h,v,distX,distY
        
def playerMove(move):
        hypot=math.hypot(move[2],move[3])
        i=(hypot/2)**.5
        moveX=move[0]*i
        moveY=move[1]*i
        return moveX,moveY
def enemyMove(move):
        x=move[2]
        y=move[3]
        moveX=move[0]*5
        moveY=move[1]*5
        if x>-5 and x<5:
                moveX=0
        if y>-5 and y<5:
                moveY=0
        return moveX,moveY
def moveSpeedCap(move):
        x=move[0]
        y=move[1]
        h=move[2]
        a=move[3]
        pi=math.pi
        if abs(h*math.cos(a))<5:
                x=0#center
        if x>5 and a<(.5*pi) and a>(-.5*pi):
                x=5#right
        if x<-5 and a<(-.5*pi) or a>(.5*pi):
                x=-5#left
        if abs(h*math.sin(a))<5:
                y=0#center
        if y>5 and a<0:
                y=5#down
        if y<-5 and a>0:
                y=-5#up
        return x,y
def bound(entity):
        s=entity
        if s.right>WIDTH:
                s.right=WIDTH
        if s.left<0:
                s.left=0
        if s.bottom>HEIGHT:
                s.bottom=HEIGHT
        if s.top<0:
                s.top=0

control="0"
while control!="1" and control!="2":
        control=input(("Move using mouse or keyboard? Type \"1\" for mouse, \"2\" for keyboard"))
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
playerImg=pygame.image.load(os.path.join(playerFolder,"BasicPlane.png")).convert()
enemyBlockImg=pygame.image.load(os.path.join(enemyFolder,"BasicPlane.png")).convert()
pygame.display.set_caption("My First Game")
clock=pygame.time.Clock()
running=True
allSprites=pygame.sprite.Group()
enemies=pygame.sprite.Group()

player=Player()
for i in range(random.randrange(0,10)):
        e=Enemy(player)
        allSprites.add(e)
        enemies.add(e)
allSprites.add(player)

while running:
        clock.tick(FPS)
        #process inputs
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        running=False
        #update
        allSprites.update()
        hitPlayer=pygame.sprite.spritecollide(player,enemies,False)
        if hitPlayer:
                running=False
        
        #draw screen
        screen.fill(BACKGROUND)
        allSprites.draw(screen)
        pygame.display.flip()
pygame.quit
