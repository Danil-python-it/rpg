from pygame import *

#настройки экрана
W = 700
L = 700

window = display.set_mode((L,W))
display.set_caption("animation_test")
WHITE = (255,255,255)
window.fill(WHITE)
clock = time.Clock()
FPS = 60
ti = 0
stutus = False


animate_list = ["png/Minotaur_02_Attacking_001.png","png/Minotaur_02_Attacking_002.png","png/Minotaur_02_Attacking_003.png","png/Minotaur_02_Attacking_004.png","png/Minotaur_02_Attacking_005.png","png/Minotaur_02_Attacking_006.png","png/Minotaur_02_Attacking_007.png","png/Minotaur_02_Attacking_008.png","png/Minotaur_02_Attacking_008.png","png/Minotaur_02_Attacking_009.png","png/Minotaur_02_Attacking_010.png","png/Minotaur_02_Attacking_011.png","png/Minotaur_02_Attacking_000.png",]
num = len(animate_list)





class Sprite():
    def __init__(self,tols,animate_list,x_coor,y_coor):
        self.l = 275
        self.w = 200
        self.anime = animate_list
        self.tols = tols
        self.x = x_coor
        self.y = y_coor
        self.rect = Rect(self.x,self.y,self.l,self.w)
        global personal
        personal = transform.scale(image.load(self.tols),(self.l,self.w))   
        NUM = 0 
    
    def DRAW(self):
        draw.rect(window,(255,255,255),self.rect)
        window.blit(personal,(self.x,self.y))
    
    def animation(self,png):
        png -= 1
        personal = transform.scale(image.load(self.anime[png]),(self.l,self.w))
        display.update()
    
    def collidpoint(self,x,y):
        return self.rect.collidepoint(x,y)



knight = Sprite("png/Minotaur_02_Attacking_000.png",animate_list,200,212)



game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        
        if i.type == MOUSEBUTTONDOWN:
            x,y = i.pos
            print(x,y)
            res = knight.collidpoint(x,y)
            if res == 1:
                stutus = True

    
    knight.DRAW()

    if stutus == True:
        ti += 1
        to = ti//15
        for i in range(num):
            if to == i and to < num:
                knight.animation(i)
            else:
                stutus = False
            


    
    
    
    
    
    
    
    

    clock.tick(FPS)
    display.update()