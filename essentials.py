import pygame as pg


class GFXRect(pg.Rect):
    def __init__(self, x, y, w, h, c: str):
        super().__init__(x, y, w, h)
        self.vel = 0.0
        self.color = c

class RectangleFallType:
    NONE: int = 0
    DOWNWARDS: int = 1
    UPWARDS: int = 2