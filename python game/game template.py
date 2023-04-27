import pygame
import random
import os
import math


WIDTH=1280
HEIGHT=720
FPS=30
BACKGROUND=(0,0,0)

gameFolder=os.path.dirname(__file__)
playerFolder=os.path.join(gameFolder,"PlatformerArtCompletePack\Basepack\Player")
enemyFolder=os.path.join(gameFolder,"PlatformerArtCompletePack\Basepack\Enemies")

class Player(pygame.sprite.Sprite):
        def __init__(self,move,moveSpeedCap):
                pygame.sprite.Sprite.__init__(self)
                self.image=playerImg
                self.rect=self.image.get_rect()
                self.rect.center=(WIDTH/2,HEIGHT/2)
                self.move=move
                self.moveSpeedCap=moveSpeedCap
        def update(self):
                mouseSpot=pygame.mouse.get_pos()
                move=self.move(self.rect.center,mouseSpot)
                moveSpeed=self.moveSpeedCap(move)
                self.rect.centerx+=moveSpeed[0]
                self.rect.centery+=moveSpeed[1]
class Enemy(pygame.sprite.Sprite):
        def __init__(self,player,move):
                pygame.sprite.Sprite.__init__(self)
                self.player=player
                self.image=enemyBlockImg
                self.rect=self.image.get_rect()
                self.rect.centerx=random.randrange(25,WIDTH-25)
                self.rect.centery=random.randrange(25,HEIGHT-25)
                self.move=move
        def update(self):
                move=self.move(self.rect.center,self.player.rect.center)
                self.rect.centerx+=move[0]
                self.rect.centery+=move[1]

def move(start,end):
        distX=end[0]-start[0]
        distY=-(end[1]-start[1])
        pi=math.pi
        if distX==0:
                distX=10^-6
        hypot=math.hypot(distX,distY)
        angle=math.atan2(distY,distX)
        moveX=math.cos(angle)*(hypot/2)**.5
        moveY=-math.sin(angle)*(hypot/2)**.5
        return moveX,moveY,hypot,angle,pi
def moveSpeedCap(move):
        x=move[0]
        y=move[1]
        h=move[2]
        a=move[3]
        pi=move[4]
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

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
playerImg=pygame.image.load(os.path.join(playerFolder,"p1_stand.png")).convert()
enemyBlockImg=pygame.image.load(os.path.join(enemyFolder,"blockerBody.png")).convert()
enemyBlockImg=pygame.transform.scale(enemyBlockImg,(25,25))
pygame.display.set_caption("My First Game")
clock=pygame.time.Clock()
running=True
allSprites=pygame.sprite.Group()
player=Player(move,moveSpeedCap)
for i in range(random.randrange(1,10)):
        e = Enemy(player,move)
        allSprites.add(e)
allSprites.add(player)
while running:
        clock.tick(FPS)
        #process inputs
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        running=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                        running=False
        #update
        allSprites.update()
        #draw screen
        screen.fill(BACKGROUND)
        allSprites.draw(screen)
        pygame.display.flip()
pygame.quit
