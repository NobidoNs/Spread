from colorsys import TWO_THIRD
from time import time
import pygame
import sys
import math
import tkinter
from tkinter import ttk


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
    
    
    

    class Rect:
        def __init__(self, color,pos=[10,10]):
            self.color=color
            self.x=pos[0]
            self.y=pos[1]
            self.z=(self.x % 3)+(self.y % 3)*3
            self.width=30
            self.heght=30

        def draw(self):
            #self.x=col*width+(col+1)*margin
            #self.y=row*height+(row+1)*margin
            pygame.draw.rect(display,self.color,(self.x*(self.width+10)+10,self.y*(self.heght+10)+10,self.width,self.heght))
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
            self.first=True
            need = False
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
        def check(self, x_medium_sq, y_medium_sq, medium_sq):
            x_centr = x_medium_sq * 3 + 1
            y_centr = y_medium_sq * 3 + 1
            y_pos = y_centr
            enables = []
            rec  = 0
            x_on = [1, 0, 2, 1]
            done = False
            part = False
            # print("x_form", x_medium_sq * 3 + 1)
            # print("y_form", y_medium_sq * 3 + 1)
            
            for i in x_on:
                if self.sq[(x_centr - 1)  + i][(y_pos - 1)].color != color_WHITE:
                    rec += 1
                    if self.sq[(x_centr - 1)  + i][(y_pos - 1)].color != color_RED:
                        part = True
                    if rec == 1 or rec == 3:
                        y_pos += 1
                    if rec == 4:
                        done = True
            rec = 0
            y_pos = y_centr
            enables = []
            x_to_activated = [2, -2, 0, 0]
            y_to_activated = [0, 0, 2, -2]
            loops = -1
            rec_2 = -1
            pos = 0

            if done == True:
                for i in x_on:
                    if self.sq[(x_centr - 1)  + i][(y_pos - 1)].color != color_WHITE:
                        self.sq[(x_centr - 1) + i][(y_pos - 1)].changeColor(color_WHITE)
                        rec += 1
                        if rec == 1 or rec == 3:
                            y_pos += 1
                    loops += 1
                    # print(loops)

                    two_x_medium_sq = x_centr - x_to_activated[loops] // 3
                    two_y_medium_sq = y_centr - y_to_activated[loops] // 3
                    


                    if self.sq[x_centr - x_to_activated[loops]][y_centr - y_to_activated[loops]].color != color_RED:
                        if x_centr - x_to_activated[loops] != 18 and y_centr - y_to_activated[loops] != 18:
                            # print("x_need", x_centr - x_to_activated[loops], "y_need", y_centr - y_to_activated[loops])
                            self.sq[x_centr - x_to_activated[loops]][y_centr - y_to_activated[loops]].changeColor(color_RED)
                    else:
                        two_x_sq = two_x_medium_sq * 3
                        two_y_sq = two_y_medium_sq * 3
                        for ch in x_on:
                            rec_2 += 1
                            print(self.sq[(two_x_sq - 1) + ch][two_y_sq - 1])
                            if self.sq[two_x_sq-ch][two_y_sq].color == color_WHITE:
                                self.sq[two_x_sq-ch][two_y_sq].changeColor(color_RED)
                            if rec == 1 or rec == 3:
                                two_y_sq -= 1



            if loops >= 0:
                for row in range(self.x):
                    for col in range(self.y):
                        if row == 0 or row == 17:
                            self.sq[row][col].changeColor(color_BLACK)
                        if col == 0 or col == 17:
                            self.sq[row][col].changeColor(color_BLACK)
            return done

        def check_2(self):
            output = False
            for i in range(18):
                for a in range(18):
                    if self.sq[a] [i].color == color_RED:
                        x_medium_sq = a // 3 
                        y_medium_sq = i // 3 
                        # print(x_medium_sq)
                        output = self.check(x_medium_sq, y_medium_sq, None)
                        if output == True:
                            self.check_2()
                            # print("done")
                            output = False
                        

        def click(self,x_mouse,y_mouse):
            column = (x_mouse-10) // (10+self.width)
            row_row = (y_mouse-10) // (10+self.heght)
            rec = 0
            one_row = row_row
            one_column = column
            done = False
            # print("x", x_mouse, "y", y_mouse)
            x_medium_sq = int((x_mouse) // (125) )
            y_medium_sq = int((y_mouse) // (125) )
            medium_sq = int(x_medium_sq + y_medium_sq*6)
            # print("x",x_medium_sq)
            # print("y",y_medium_sq)
            # print(medium_sq)
            color=self.sq[column][row_row].color
            if color == color_WHITE:
                self.sq[column][row_row].changeColor(color_RED)
                # done = self.check(x_medium_sq, y_medium_sq, medium_sq)
                done = self.check_2()
                # print("row", row_row, "column", column)
            if done == True:
                done = self.check(x_medium_sq, y_medium_sq, medium_sq)
            # if self.sq[row_row][column].color == color_RED and self.sq[row_row + 1][column - 1].color == color_RED and (
            # self.sq[row_row - 1][column - 1].color == color_RED and self.sq[row_row][column - 2].color == color_RED ):
            #     print("s1")


                    
            # if self.sq[row][col].z==7 and color==color_RED:
            #     pass
            # if self.sq[row][col].z==1 and color==color_RED:
            #     pass
            # if self.sq[row][col].z==3 and color==color_RED:
            #     pass
            # if self.sq[row][col].z==5 and color==color_RED:
            #     pass
        def draw(self):
            for i in range(self.x):
                for j in range(self.y):
                    self.sq[i][j].draw()
                    

    color=color_WHITE
    rects=Rects()

    while True:
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
    pygame.time.wait(1000)
    pygame.quit()

# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pygame.font23333 