from CameraClass import Camera
from Vectors import Vector2D
from ObjectClass import Object

class World:
    def __init__(self, camera=None, gravity=-9.81, Objects=[],DeltaTime=0.01):
        self.camera = Camera(self) if camera is None else camera
        self.gravity = gravity
        self.Objects = Objects
        self.DeltaTime = DeltaTime

    def get_objects(self):
        return self.Objects

    def get_camera_pos(self):
        return self.camera.get_Pos()
    
    def add_object(self,type,info):
        self.Objects.append(Object(self,type,info))

    def update_objects(self):
        for object in self.get_objects():
            object.update()