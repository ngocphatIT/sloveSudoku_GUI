import pygame
from solveSudoku import *
pygame.init()
class Button:
    def __init__(self,**kwargs):
        self.bg1=kwargs['bg1']
        self.fg1=kwargs['fg1']
        self.font=kwargs['font']
        self.text=kwargs['text']
        self.sizex=kwargs['sizex']
        self.sizey=kwargs['sizey']
        self.bg2=kwargs['bg2']
        self.fg2=kwargs['fg2']
    def show(self,surface,x,y):
        pygame.draw.rect(surface,self.bg1,(x,y,self.sizex,self.sizey))
        text=pygame.font.SysFont(self.font[0],self.font[1]).render(self.text,True,self.fg1)
        rectT=text.get_rect()
        rectT.center=(x+self.sizex//2,y+self.sizey//2)
        surface.blit(text,rectT)
        if pygame.mouse.get_pos()[0]>=x and pygame.mouse.get_pos()[1]<=y+self.sizey and pygame.mouse.get_pos()[0]<=x+self.sizex and pygame.mouse.get_pos()[1]>=y:
            pygame.draw.rect(surface,self.bg2,(x,y,self.sizex,self.sizey))
            text=pygame.font.SysFont(self.font[0],self.font[1]).render(self.text,True,self.fg2)
            rectT=text.get_rect()
            rectT.center=(x+self.sizex//2,y+self.sizey//2)
            surface.blit(text,rectT)
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
        return False
class Block:
    def __init__(self,sizex,sizey,width,data,group):
        self.sizex = sizex
        self.sizey = sizey
        self.data=data
        self.group= group
        self.width=width
        self.fontsize=30
        self.color=(0,0,0)
    def show(self,surface,x,y):
        groupColor=[(255,0,0),(0,255,0),(0,0,255),(0,255,0),(0,0,255),(255,0,0),(0,0,255),(255,0,0),(0,255,0)]
        pygame.draw.rect(surface,groupColor[self.group],[x,y,self.sizex-self.width//2,self.sizey-self.width//2],self.width)
        self.text=pygame.font.SysFont('Arial',self.fontsize).render(str(self.data),True,self.color)
        rect=self.text.get_rect()
        rect.center=(x+self.sizex//2,y+self.sizey//2)
        if self.data!=0:
            surface.blit(self.text,rect)
class SudokuGame:
    def __init__(self,width=600,height=700):
        self.surface=pygame.display.set_mode((width,height))
        self.distance_x=100
        self.distance_y=50
        self.sizex=50
        self.sizey=50
        self.data=[ 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] ]
        self.btnSolve=Button(bg1=(128,128,128),fg1=(255,255,255),font=('Times',20),text='Giải',sizex=100,sizey=50,bg2=(0,128,128),fg2=(0,255,255))
        pygame.display.set_caption("Sudoku")
    def run(self):
        clock=pygame.time.Clock()
        FPS=30
        self.isChoice=True
        self.xChoice=0
        self.yChoice=0
        while True:
            self.display()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos=pygame.mouse.get_pos()
                        self.xChoice=(pos[0]-self.distance_x)//self.sizex
                        self.yChoice=(pos[1]-self.distance_y)//self.sizey
                        self.isChoice=True
                if self.xChoice<=8 and self.yChoice<=8:
                    if self.isChoice:
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_0:
                                self.data[self.yChoice][self.xChoice]=0
                            if event.key==pygame.K_1:
                                self.data[self.yChoice][self.xChoice]=1
                            if event.key==pygame.K_2:
                                self.data[self.yChoice][self.xChoice]=2
                            if event.key==pygame.K_3:
                                self.data[self.yChoice][self.xChoice]=3
                            if event.key==pygame.K_4:
                                self.data[self.yChoice][self.xChoice]=4
                            if event.key==pygame.K_5:
                                self.data[self.yChoice][self.xChoice]=5
                            if event.key==pygame.K_6:
                                self.data[self.yChoice][self.xChoice]=6
                            if event.key==pygame.K_7:
                                self.data[self.yChoice][self.xChoice]=7
                            if event.key==pygame.K_8:
                                self.data[self.yChoice][self.xChoice]=8
                            if event.key==pygame.K_9:
                                self.data[self.yChoice][self.xChoice]=9
                            if event.key==pygame.K_RETURN:
                                self.isChoice=False
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            self.xChoice+=1
                            if self.xChoice>8:
                                self.xChoice=0
                        if event.key==pygame.K_LEFT:
                            self.xChoice-=1
                            if self.xChoice<0:
                                self.xChoice=8
                        if event.key==pygame.K_DOWN:
                            self.yChoice+=1
                            if self.yChoice>8:
                                self.yChoice=0
                        if event.key==pygame.K_UP:
                            self.yChoice-=1
                            if self.yChoice<0:
                                self.yChoice=8
            pygame.display.update()
    def display(self):
        self.surface.fill((255,255,255))
        self.drawData()
        if self.isChoice:
            if self.xChoice<=8 and self.yChoice<=8:
                pygame.draw.rect(self.surface,(255,255,255),(self.distance_x+self.xChoice*self.sizex,self.distance_y+self.yChoice*self.sizey,self.sizex,self.sizey),2)
            else:
                self.isChoice=False
        if self.btnSolve.show(self.surface,self.distance_x+int(self.sizex*3.5),self.distance_y+self.sizey*9+20):
            data=Sudoku(self.data)
            data.solve()
            self.data=data.data
    def drawData(self):
        width=2
        group=0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])): 
                group=int(i/3)*3+int(j/3)
                if self.data[i][j]!=0:
                    block=Block(sizex=self.sizex,sizey=self.sizey,width=width,data=self.data[i][j],group=group)
                    block.show(surface=self.surface,x=self.distance_x+j*self.sizex+width,y=self.distance_y+self.sizey*i+width)
                else:
                    block=Block(sizex=self.sizex,sizey=self.sizey,width=width,data=0,group=group)
                    block.show(surface=self.surface,x=self.distance_x+j*self.sizex+width,y=self.distance_y+i*self.sizey+width)
if __name__ == '__main__':
    game=SudokuGame()
    game.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    