import pygame as pg

class GameObject():

    def __init__(self, x: float, y: float, w: int, h:int, img: str):
        self.x = x
        self.y = y

        self.width = w
        self.height = h
        self.img = pg.image.load(img)

    def update(self):
        return
    
    def draw(self):
        return