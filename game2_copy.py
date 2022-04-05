from time import time
import pygame
import sys
import math
import tkinter
from tkinter import ttk
import time


def main(winstyle=0):
    pygame.init()
    clock = pygame.time.Clock()
    size = (730,730)
    display = pygame.display.set_mode(size)
    pygame.display.set_caption("Test game2")

    color_BLACK = (0,0,0)
    color_WHITE = (255,255,255)
    color_BLUE =  (0,0,255)
    color_GREEN = (0,255,0)
    color_YELLOW = (255,255,0)
    color_RED = (255,0,0)
    width = 30
    height = 30
    margin = 10
    indent = 5
    
    
    

    class Rect:
        def __init__(self, color,pos=[margin,margin]):
            self.color=color
            self.x=pos[0]
            self.y=pos[1]
            self.z=(self.x % 3)+(self.y % 3)*3
            self.width=30
            self.heght=30

        def draw(self):
            #self.x=col*width+(col+1)*margin
            #self.y=row*height+(row+1)*margin
            pygame.draw.rect(display,self.color,(self.x*(self.width+margin)+margin,self.y*(self.heght+margin)+margin,self.width,self.heght))
        def changeColor(self,color):
            #self.column = x_mouse // (margin+width)
            #self.row = y_mouse // (margin+height)
            self.color=color
    class Rects:
        def __init__(self):
            self.x = 18
            self.y = 18
            self.width=30
            self.heght=30
            self.n=[]
            self.rest = False
            self.whitePole = True
            self.first=True
            self.player = 1
            self.plColor = color_RED
            self.plColors = [color_RED, color_BLUE]
            self.sq = [[i * j for j in range(self.x)] for i in range(self.y)]
            for row in range(self.x):
                for col in range(self.y):
                    self.sq[row][col] = Rect(color_WHITE,[row,col])
                    if row == 0 or row == 17:
                        self.sq[row][col].changeColor(color_BLACK)
                    if col == 0 or col == 17:
                        self.sq[row][col].changeColor(color_BLACK)
                    if self.sq[row][col].z==0 or self.sq[row][col].z==2:
                        self.sq[row][col].changeColor(color_BLACK)
                    if self.sq[row][col].z==4:
                        self.sq[row][col].changeColor(color_YELLOW)
                    if self.sq[row][col].z==6:
                        self.sq[row][col].changeColor(color_BLACK)
                    if self.sq[row][col].z==8:
                        self.sq[row][col].changeColor(color_BLACK)
        
        def recoloring(self, x_medium_sq, y_medium_sq):
            for y in range(3):
                for x in range(3):
                    x1 = (x_medium_sq*3) + x
                    y1 = (y_medium_sq*3) + y
                    a = self.WhatIsColor(x1, y1)
                    if a == color_BLUE or a == color_RED:
                        self.ChColor(x1, y1, self.plColor)

        def colorJamp(self, x_medium_sq, y_medium_sq, plColor):
            self.recoloring(x_medium_sq, y_medium_sq)
            br = False
            for y in range(3):
                for x in range(3):
                    if self.sq[(x_medium_sq*3) + x][(y_medium_sq*3) + y].color == color_WHITE:
                        self.sq[(x_medium_sq*3) + x][(y_medium_sq*3) + y].changeColor(plColor)
                        br = True
                        break
                if br == True:
                    break
        def getSq(self, x, y):
            if type(x) != int:
                print("ERR")
                return None
            return self.sq[x][y]

        def clear_medium_sq(self, x_medium_sq, y_medium_sq):
            for y in range(3):
                for x in range(3):
                    x1 = (x_medium_sq * 3) + x
                    y1 = (y_medium_sq * 3) + y
                    z = self.WhatIsColor(x1, y1)
                    if z == self.plColors[0] or z == self.plColors[1]:
                        self.ChColor(x1, y1, color_WHITE)

        def haveColor(self, x_medium_sq, y_medium_sq):
            x_centr = x_medium_sq * 3 + 1
            y_centr = y_medium_sq * 3 + 1
            x_on = [1, 0, 2, 1]
            y_pos = y_centr
            rec = 0
            for i in x_on:
                z = self.getSq((x_centr - 1)  + i,(y_pos - 1)).color
                rec += 1
                if z == self.plColors[0] or z == self.plColors[1]:
                    a = self.WhatIsColor((x_centr - 1)  + i, (y_pos - 1))
                    return [True, a]
                if rec == 1 or rec == 3:
                    y_pos += 1
            return [False, None]

        def onlyColorfull(self, x_medium_sq, y_medium_sq):
            x_centr = x_medium_sq * 3 + 1
            y_centr = y_medium_sq * 3 + 1
            x_on = [1, 0, 2, 1]
            y_pos = y_centr
            rec = 0
            for i in x_on:
                if self.getSq((x_centr - 1)  + i,(y_pos - 1)).color != color_WHITE:
                    rec += 1
                    if rec == 1 or rec == 3:
                        y_pos += 1
                    if rec == 4:
                        return True
            return False

        def renderOnce(self):
            for x in range(10):
                render()

        def chPlayer(self, nowPlayer):
            if nowPlayer == color_BLUE:
                self.plColor = color_RED
                return color_RED
            elif nowPlayer == color_RED:
                self.plColor = color_BLUE
            else:
                return color_GREEN

        def BOOM(self,x_medium_sq, y_medium_sq):
            x_centr = x_medium_sq * 3 + 1
            y_centr = y_medium_sq * 3 + 1
            x_to_activated = [2, -2, 0, 0]
            y_to_activated = [0, 0, 2, -2]
            self.clear_medium_sq(x_medium_sq, y_medium_sq)
            loops = -1

            for i in range(4):
                loops += 1
                x1 = x_centr - x_to_activated[loops]
                y1 = y_centr - y_to_activated[loops]

                two_x_medium_sq = (x1) // 3
                two_y_medium_sq = (y1) // 3
                z = self.WhatIsColor(x1, y1)
                
                if self.WhatIsColor(x1, y1) != True:
                    if self.WhatIsColor(x1, y1) == color_WHITE:
                        self.ChColor(x1, y1, self.plColor)
                        self.recoloring(two_x_medium_sq, two_y_medium_sq)
                    elif z == self.plColors[0] or z == self.plColors[1]:
                        self.colorJamp(two_x_medium_sq, two_y_medium_sq, self.plColor)
            self.renderOnce()

        def contur(self):
            for row in range(self.x):
                for col in range(self.y):
                    if row == 0 or row == 17:
                        self.sq[row][col].changeColor(color_BLACK)
                    if col == 0 or col == 17:
                        self.sq[row][col].changeColor(color_BLACK)

        def check(self, x_medium_sq, y_medium_sq):

            done = False

            if self.onlyColorfull(x_medium_sq, y_medium_sq) == True:
                done = True

            if done == True:
                self.BOOM(x_medium_sq, y_medium_sq)
                self.contur()
            return done

        def ChColor(self,x,y,color):
            if x >= 0 and x < 18:
                self.sq[x][y].changeColor(color)
        
        def WhatIsColor(self, x, y):
            if x >= 18 or y >= 18 or x < 0 or y < 0:
                a = True
                return a
            else:
                return self.sq[x][y].color

        def check_2(self):
            output = False
            for i in range(18):
                for a in range(18):
                    if self.sq[a] [i].color == self.plColors[0] or self.sq[a] [i].color == self.plColors[1]:
                        x_medium_sq = a // 3 
                        y_medium_sq = i // 3 
                        # print(x_medium_sq)
                        output = self.check(x_medium_sq, y_medium_sq)
                        if output == True:
                            self.check_2()
                            # print("done")
                            output = False
                        

        def click(self,x_mouse,y_mouse):
            column = (x_mouse-margin) // (margin+self.width)
            row_row = (y_mouse-margin) // (margin+self.heght)
            y_medium_sq = int((y_mouse) // ((height*3) + (margin*3) + indent))
            x_medium_sq = int((x_mouse) // ((height*3) + (margin*3) + indent))
            color=self.WhatIsColor(column, row_row)

            if color == color_BLACK or color == color_YELLOW or (
            color == self.plColors[0] or color == self.plColors[1]):
                return None
            [fl, c] = self.haveColor(x_medium_sq, y_medium_sq)
            if fl == True:
                if c != self.plColor:
                    return None

            if color == color_WHITE:
                self.sq[column][row_row].changeColor(self.plColor)
                self.check_2()

            self.whitePole = self.whiteList()
            if self.whitePole == False:
                self.loose()

            self.chPlayer(self.plColor)

        def whiteList(self):
            for y in range(self.y):
                for x in range(self.x):
                    a = self.WhatIsColor(x, y)
                    if (a == self.plColors[0] or a == self.plColors[1]) and self.first == False:
                        print("b")
                        return False
            print("a")
            self.first = False
            return True
                    

        def loose(self):
            BLoose = True
            RLoose = True
            for y in range(18):
                for x in range(18):
                    a = self.WhatIsColor(x, y)
                    if a == color_BLUE:
                        BLoose = False
                    if a == color_RED:
                        RLoose = False
            if BLoose == True:
                print("R WIN")
                print("Click To Restart")
                self.rest = True
            if RLoose == True:
                print("B WIN")
                print("Click To Restart")
                self.rest = True
            if self.rest == True:
                self.rest = False
                otv = self.restartClick()
                if otv == True:
                    self.fulRsetart()
        
        def fulRsetart(self):
            for row in range(self.x):
                for col in range(self.y):
                    a = self.WhatIsColor(row, col)
                    if a == self.plColors[0] or a == self.plColors[1]:
                        self.ChColor(row, col, color_WHITE)
            self.first = True

        def restartClick(self):
            while True:
                for ivent in pygame.event.get():
                    if ivent.type ==  pygame.MOUSEBUTTONDOWN:
                        return True


        def draw(self):
            for i in range(self.x):
                for j in range(self.y):
                    self.sq[i][j].draw()
                    

    color=color_WHITE
    rects=Rects()



    def render():
        display.fill(color_BLACK)
        x_mouse, y_mouse = pygame.mouse.get_pos()
        for ivent in pygame.event.get():
            if ivent.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif ivent.type ==  pygame.MOUSEBUTTONDOWN:
                rects.click(x_mouse,y_mouse)
                
        rects.draw()
        

        #линии
        for row in range(7):
            for col in range(7):
                x=col*width+(col)*margin
                y=row*120+4
                pygame.draw.rect(display,color_GREEN,(x,y,700,2))
        for row in range(7):
            for col in range(7):
                y=col*width+(col)*margin
                x=row*120+4
                pygame.draw.rect(display,color_GREEN,(x,y,2,700))
        pygame.display.flip()
        pygame.display.update()

        clock.tick(20)

    while True:
        render()
    pygame.time.wait(1000)
    pygame.quit()
# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pygame.font23333 