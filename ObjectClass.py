from Vectors import Vector2D
import pygame as py

class Object_Info:
    def __init__(self):
        self.shape="rect"
        self.color=(30,200,30)
        self.width = 40
        self.height = 40
        self.pos = Vector2D(10,10)
        self.speed = Vector2D(90,90)

class Object:
    def __init__(self,world, type, info):
        self.world=world
        self.type = type
        self.info = info

    def draw(self, screen):
        if self.info.shape == "rect":
            py.draw.rect(screen, self.info.color, self.get_rect(screen))

    def get_rect(self,screen):
        return (self.get_x()-self.world.camera.get_pos().x,
                screen.get_height()-self.info.height-self.get_y()+self.world.camera.get_pos().y,
                self.info.width,
                self.info.height)
    
    def get_x(self):
        return self.info.pos.x
    
    def get_y(self):
        return self.info.pos.y
    
    def update(self):
        self.info.pos+=self.info.speed*self.world.DeltaTime()
        self.info.speed+=Vector2D(0,self.world.gravity)*self.world.DeltaTime()

