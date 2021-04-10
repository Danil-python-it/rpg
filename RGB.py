#region библиотеки 
from pygame import *
from random import randint
#endregion 

#region основные настройки
L = 800
W = 800
I = 0

window = display.set_mode((L,W))
window.fill((255,255,255))
display.set_caption("RPG_warning")
FPS = 60
init()
damag = 0.92
x,y = None,None
clock = time.Clock()
#region color
GREEN = 0,255,0
BLACK = 0,0,0
WHITE = 255,255,255
color_angry3 = 165,10,0
color_angry2 = 62,0,77
color_angry1 = 0,121,120
color_red = 255,0,0
DEAD = 77,77,77
color_attack = 255,253,0

#endregion

color_angrys = [color_angry3,color_angry2,color_angry1]

angrys = list()

#endregion

#region классы

class player():
    
    def __init__(self,health,attack,lenght,width,x_coor,y_coor):
        self.XP = health
        self.XP1 = health
        self.damag = attack
        self.color = GREEN
        self.lenght = lenght 
        self.width = width
        self.x = x_coor
        self.y = y_coor
        self.rect1 = Rect(self.x,self.y,self.lenght,self.width)
        self.rect2 = Rect(self.x-100,self.y-100,self.lenght*3,self.width*3)
        global colo
        colo = self.damag
        

    def DRAW(self):
        draw.rect(window,WHITE,self.rect2)
        draw.rect(window,self.color,self.rect1)

    def health(self):
        damag = 92/self.XP1
        if self.XP*damag >= 0:
            wid = self.XP*damag
        elif self.XP*damag < 0:
            wid = 0
            self.color = DEAD
            game = False
            global colo
            colo = 0
            quit()
            

        rect_red = Rect(self.x+4,self.y+self.lenght+14,wid,12)
        rect_white = Rect(self.x+2,self.y+self.lenght+12,self.width-4,16)
        rect_black = Rect(self.x,self.y+self.lenght+10,self.width,20)
        draw.rect(window,BLACK,rect_black)
        draw.rect(window,WHITE,rect_white)
        draw.rect(window,color_red,rect_red)

    def attack(self,att):
        self.XP -= att

    def collidepoint(self,x,y):
        return self.rect1.collidepoint(x,y)

    def colliderect(self,i):
        return self.rect2.colliderect(i)

def animals():
    for i in range(randint(1,4)):
        angry_one = angry_player(randint(1,700),randint(1,670),100,100,100)
        angrys.append(angry_one)



class angry_player():
    def __init__(self,x_coor,y_coor,health,length,width):
        self.length = length
        self.width = width
        self.x = x_coor
        self.y = y_coor
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.color_red = color_red
        self.life = "да"

        coi = randint(1,100)
        if coi > 0 and coi < 60 :
            self.chance = 2
        elif coi >= 60 and coi < 90:
            self.chance = 1
        else:
            self.chance = 0

        self.color = color_angrys[self.chance]
        color = self.color
        self.rect = Rect(self.x,self.y,self.length,self.width)
    
        if self.color == color_angry1 :
            self.health = 50
            self.health_2 = 50
            self.att = 2
        elif self.color == color_angry2 :
            self.health = 100
            self.health_2 = 100
            self.att = 6
        elif self.color == color_angry3 :
            self.health = 150
            self.health_2 = 150
            self.att = 10

    def died1(self):
        global died 
        if self.health <= 0:
            self.BLACK = WHITE
            self.WHITE = WHITE
            self.color_red = WHITE

    
    def DRAW(self):
        draw.rect(window,self.color,self.rect)
    
    def check(self):
        global attar
        
        if self.color == WHITE:
            attar = False 
        else:
            attar =  True
    
    def check2(self):
        global life
        life = self.life
    
    def aliternol(self):
        self.life = "да"
        

    
    def dammag(self):
        damag = 92/self.health_2
        if self.health*damag >= 0:
            wid = self.health*damag
        elif self.health*damag < 0:
            wid = 0
            self.color = WHITE
            self.att = 0
            self.life = "нет"


        rect_red = Rect(self.x+4,self.y+self.length+14,wid,12)
        rect_white = Rect(self.x+2,self.y+self.length+12,self.width-4,16)
        rect_black = Rect(self.x,self.y+self.length+10,self.width,20)
        draw.rect(window,self.BLACK,rect_black)
        draw.rect(window,self.WHITE,rect_white)
        draw.rect(window,self.color_red,rect_red)

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def mani(self):
        self.x = randint(1,700)
        self.y = randint(1,680)
        self.rect = Rect(self.x,self.y,self.length,self.width)
        draw.rect(window,self.color,self.rect)
    def attack(self,colo):
        self.health -= colo
    def attacking(self):
        att = self.att
        player_one.attack(att)
    def run(self):
        self.x = randint(1,700)
        self.y = randint(1,680)
        self.rect = Rect(self.x,self.y,self.length,self.width)


#endregion

#region элементы игры
player_one = player(200,15,100,100,350,350)
ijn = 0
for i in range(randint(1,4)):
    angry_one = angry_player(randint(1,700),randint(1,670),100,100,100)
    angrys.append(angry_one)
LEN = len(angrys) 
#endregion

def up():
    window.fill((255,255,255))
    player_one.DRAW()
    player_one.health()
    for i in angrys:
        i.DRAW()
        i.dammag()

#region игровой цикл
game = True
gaming = True
point = 0
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

        if i.type == MOUSEBUTTONDOWN:
            x,y = i.pos
            if gaming == True:
                for v in angrys:
                    res = v.collidepoint(x,y)
                    I += res
                    if res == 1:
                        global colo
                        v.attack(colo)
                        up()
                        v.run()
                        display.update()
                        up()
                        gaming = False
                    elif res == 0:
                        gaming = False
        
        elif gaming == False:
            for i in angrys:
                i.check()
                global attar
                if attar == True:
                    if randint(1,3) == 1:
                        i.attacking()
                    else:
                        pass 
            gaming = True
        
    for i in angrys:
        i.check2()
        
        
        if life == "нет":
            point += 1
            print(life)
            display.update()
            life = "да"
            print(life)
        elif life == "да":
            point += 0
            i.aliternol()
    if point == LEN:
        angrys = list()
        point = 0
        animals()
        up()        
    
    
    player_one.DRAW()
    player_one.health()

    for i in angrys:
        i.died1()


    
    for i in angrys:
        i.DRAW()
        ros = player_one.colliderect(i)
        if ros == 1:
            up()
            i.mani()
        else:
            up()
            i.DRAW()

        i.dammag()

    clock.tick(FPS)
    display.update()
#endregion