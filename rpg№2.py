from pygame import *
from random import randint

FPS = 60
L = 800
W = 800
point = 0

WHITE = (255,255,255)
GREEN = 0,255,0
RED = 255,0,0
BLACK = 0,0,0
GRAY = 77,77,77


init()
one = 67,154,255
two = 0,0,255
three = 0,0,49
f1 = font.Font(None,70)
text1 = f1.render("YOU LOSE",True,BLACK)
text2 = f1.render("YOU WIN",True,BLACK)
color_angry = [one,two,three]
angry = list()
stutus = False



clock = time.Clock()
window = display.set_mode((L,W))
window.fill(WHITE)
display.set_caption("rpg two")

#region Sprite
class Sprite():
    def __init__(self,x_coor,y_coor,color,health,attack,lenght=100,width=100):
        self.x = x_coor
        self.y = y_coor
        self.color = color
        self.health = health
        self.hp = (width-8)/self.health
        self.attack = attack
        self.lenght = lenght
        self.width = width
        self.rect = Rect(self.x,self.y,self.lenght,self.width)
        self.coli = True


    def DRAW(self):
        draw.rect(window,self.color,self.rect)

    def xp(self):
        
        wid = self.hp*self.health
        if self.health < 0:
            wid = 0
            self.color = GRAY
            self.coli = False

        if self.coli == True:
            rect_black =Rect(self.x,self.y+self.lenght+10,self.width,30)
            rect_white =Rect(self.x+2,self.y+self.lenght+12,self.width-4,26)
            rect_red =Rect(self.x+4,self.y+self.lenght+14,wid,22) 

            draw.rect(window,BLACK,rect_black)        
            draw.rect(window,WHITE,rect_white)
            draw.rect(window,RED,rect_red)
        else:
            pass
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
#endregion

class angry_Sprite():
    def __init__(self,x_coor,y_coor,lenght=100,width=100):
        self.x = x_coor
        self.y = y_coor
        self.color = color_angry[randint(0,2)]
        self.to = self.color
        self.lenght = lenght
        self.width = width
        self.rect = Rect(self.x,self.y,self.lenght,self.width)
        self.coli = True
        
        if self.color == one:
            self.health = 100
            self.attack = 10
        elif self.color == two:
            self.health = 150
            self.attack = 15
        elif self.color == three:
            self.health = 200
            self.attack = 20

        self.hp = (self.width-8)/self.health
    
    def prover(self):
        self.rect = Rect(self.x,self.y,self.lenght,self.width)
        draw.rect(window,WHITE,self.rect)

    def DRAW(self):
        self.rect = Rect(self.x,self.y,self.lenght,self.width)
        draw.rect(window,self.color,self.rect)
    
    def xp(self):
        wid = self.hp*self.health
        if self.health < 0:
            wid = 0
            self.color = GRAY
            self.coli = False
            draw.rect(window,self.color,self.rect)

        if self.coli == True:
            rect_black =Rect(self.x,self.y+self.lenght+10,self.width,30)
            rect_white =Rect(self.x+2,self.y+self.lenght+12,self.width-4,26)
            rect_red =Rect(self.x+4,self.y+self.lenght+14,wid,22) 

            draw.rect(window,BLACK,rect_black)        
            draw.rect(window,WHITE,rect_white)
            draw.rect(window,RED,rect_red)
        else:
            pass
    


    def colliderect(self,rect):
        return self.rect.colliderect(rect)
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

player = Sprite(325,321,GREEN,300,20)
for i in range(randint(1,3)):
    person = angry_Sprite(randint(0,700),randint(0,650))
    angry.append(person)
col = len(angry)
col_two = len(angry)
print(col)
col -= 1


game = True
while game:
    for i in event.get():
        
        if i.type == QUIT:
            game = False
        
        if i.type == MOUSEBUTTONDOWN:
            button_type = i.button
            x,y = i.pos
            
            for i in angry:
                res = i.collidepoint(x,y)
                if res == 1 and stutus == True and button_type == 1:
                    i.health -= player.attack
                    stutus = False
                elif button_type != 1 and res == 0:
                    player.health += 20

    for i in angry:
        i.prover()
        ras = i.colliderect(player.rect)
        if ras == 1:
            print(1)
            i.x = randint(0,700)
            i.y = randint(0,650)
            i.prover()
            display.update()
        else:
            i.DRAW()
            i.xp()

    if stutus == False:
        ro = randint(0,col)
        if angry[ro].coli != False:
            player.health -= angry[ro].attack
            angry[ro].color = RED
            angry[ro].DRAW()
            display.update()
            print("------------------------------------------------")
            print("вам был нанесён урон -", str(angry[ro].attack))
            print("ваш урвень здоровье -", str(player.health))
            print("------------------------------------------------")
            angry[ro].color = angry[ro].to
            display.update()
            stutus = True
        else:
            pass

    for v in range(1):
        for i in angry:
            if i.color == GRAY:
                point += 1
            else:
                pass
        if point == col_two:
            point = 0
            window.fill((GREEN))
            window.blit(text2,(325,330))
            player.coli = False
            angry = list()
        else:
            point = 0


    if player.color == GRAY:
        player.color = RED
        window.fill((RED))
        window.blit(text1,(325,330))
        display.update()


    player.DRAW()
    player.xp()
    
    clock.tick(FPS)
    display.update()