# -------------------------
# Name: Simple Graphics
# Date created: 9/16/2024
# Author: devpython88
# Version: v0.1
# -------------------------

import pygame as pg

pg.init()

class GFXRect(pg.Rect):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.vel = 0.0


win = pg.display.set_mode((800, 600))
pg.display.set_caption("SimpleGFX")

font = pg.font.SysFont("Consolas", 36)
header = font.render("SiMPLE GRAPHiCS", 0, "black")
header_rect = header.get_rect()
header_rect.x = (win.get_width() // 2) - header_rect.width

clock = pg.time.Clock()
rects: list = []

makeRectFall = False

runnin = True

while runnin:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runnin = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()

            rects.append(GFXRect(*mouse_pos, 30, 30))
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_5:
                makeRectFall = True
            
            elif event.key == pg.K_r:
                rects.clear()
                makeRectFall = False
    
    win.fill("white")
    clock.tick(60)

    # Draw Header before rects to make it look better
    win.blit(header, header_rect)

    for rect in rects:
        if makeRectFall:
            if rect.y < win.get_height() - 30:
                rect.vel += 0.1
                rect.y += rect.vel
            else:
                # Clamp the y position at the bottom
                rect.y = win.get_height() - 30
                rect.vel = 0  # Stop the velocity when it reaches the bottom

        pg.draw.rect(win, "red", rect)

    pg.display.update()
    pg.display.flip()

pg.quit()