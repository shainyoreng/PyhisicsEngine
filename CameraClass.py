from Vectors import Vector2D
from Enums import *
'''
camera_type:
Stationary, Constent speed, Attached, Moves with, Free falling
'''


class Camera:
    def __init__(self, world, pos=Vector2D(0, 0), camera_type=CT.Stationary, speed=Vector2D(0, 0), attached=None):
        self.pos = pos
        self.camera_type = camera_type
        self.speed = speed
        self.attached = attached
        self.world = world

    def update(self):
        if self.camera_type == CT.Stationary:
            pass

        elif self.camera_type == CT.ConstentSpeed:
            self.pos += self.speed*self.world.DeltaTime()

        elif self.camera_type == CT.FreeFalling:
            self.pos += self.speed*self.world.DeltaTime()
            self.speed += Vector2D(0, self.world.gravity)*self.world.DeltaTime()

        elif self.camera_type == CT.Attached:
            self.pos = self.attached.info.pos-Vector2D(350, 350)

        elif self.camera_type == CT.MovesWith:
            self.pos = self.pos+self.attached.info.speed*self.world.DeltaTime()

    def get_pos(self):
        return self.pos
