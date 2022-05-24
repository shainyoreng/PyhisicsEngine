from CameraClass import Camera
from Vectors import Vector2D
from ObjectClass import Object
from pygame.time import Clock


class World:
    def __init__(self, camera=None, gravity=-9.81, Objects=[],DeltaTime=0.01):
        self.camera = Camera(self) if camera is None else camera
        self.gravity = gravity
        self.world_clock = Clock()
        self.Objects = Objects

        #Delta time
        self.DT=0

    def get_objects(self):
        return self.Objects

    def get_camera_pos(self):
        return self.camera.get_pos()
    
    def add_object(self,type,info):
        self.Objects.append(Object(self,type,info))

    def update_objects(self,FPS):
        self.DT = self.world_clock.tick(FPS)
        for object in self.get_objects():
            object.update()

    def DeltaTime(self):
        return self.DT/300