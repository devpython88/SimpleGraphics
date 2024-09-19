# -------------------------
# Name: Simple Graphics
# Date created: 9/16/2024
# Author: devpython88
# Version: v0.1
# -------------------------

from ast import List
import random
import pygame as pg
from tkinter import simpledialog, Tk, messagebox
from essentials import GFXRect, RectangleFallType

pg.init()

root = Tk()
root.withdraw()

win = pg.display.set_mode((800, 600))
pg.display.set_caption("SimpleGFX")

font = pg.font.SysFont("Consolas", 36)
header = font.render("SiMPLE GRAPHiCS", 0, "black")
header_rect = header.get_rect()
header_rect.x = (win.get_width() // 2) - header_rect.width

clock = pg.time.Clock()
rects: list = []

rectFallType = RectangleFallType.NONE

runnin = True

# VALID COLORS
valid_colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'brown': (165, 42, 42),
    'black': (0, 0, 0)
}

while runnin:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runnin = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()

            color = simpledialog.askstring("Color?", "Enter the color (e.g red, green, etc...)")

            if color is None or color not in valid_colors.keys():
                messagebox.showerror(title="error", message="invalid color")
            else:
                rects.append(GFXRect(*mouse_pos, 30, 30, color))
        
        elif event.type == pg.KEYDOWN:
            # 5 = down
            if event.key == pg.K_5:
                rectFallType = RectangleFallType.DOWNWARDS

            # 4 = up
            elif event.key == pg.K_4:
                rectFallType = RectangleFallType.UPWARDS
            
            elif event.key == pg.K_r:
                rects.clear()
                makeRectFall = False
    
    win.fill("white")
    clock.tick(60)

    # Draw Header before rects to make it look better
    win.blit(header, header_rect)

    for rect in rects:
        if rectFallType != RectangleFallType.NONE:
            if rectFallType == RectangleFallType.DOWNWARDS:
                if rect.y <= win.get_height() - 30:
                    rect.vel += random.uniform(0.1, 0.3)
                    rect.y += rect.vel
                else:
                    rect.vel = 0
                    rect.y = win.get_height() - 30
            
            elif rectFallType == RectangleFallType.UPWARDS:
                if rect.y >= 0:
                    rect.vel += random.uniform(0.1, 0.3)
                    rect.y -= rect.vel
                else:
                    rect.vel = 0
                    rect.y = 0

        pg.draw.rect(win, rect.color, rect)

    pg.display.update()
    pg.display.flip()

pg.quit()