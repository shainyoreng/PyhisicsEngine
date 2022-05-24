import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]=""

from logging import raiseExceptions
from tokenize import Double
import pygame as py
from Vectors import Vector2D
from pygame.time import Clock
from Enums import *
from WorldClass import World
from ObjectClass import Object, Object_Info


"""
types:
body, spring, planet, rope, wall

precision:
low, med, high, super high
"""



def update_screen(screen, world):
    world.camera.update()

    screen.fill((179,202,219))
    for object in world.get_objects():
        object.draw(screen, world.get_camera_pos())

    screen = py.transform.flip(screen,False,True)

    py.display.update()


if __name__ == '__main__':

    py.init()

    width = 700
    height = 700
    win = py.display.set_mode((width, height))

    clock = Clock()
    

    Precision = Pr.Med

    MyWorld = World()
    MyWorld.add_object(OT.Body,Object_Info())
    MyWorld.add_object(OT.Body,Object_Info())
    MyWorld.DeltaTime = clock.tick(60)/3000

    MyWorld.Objects[1].info.pos=Vector2D(400,400)
    MyWorld.Objects[1].info.speed=Vector2D(0,0)
    MyWorld.Objects[1].info.color=(220,10,50)

    MyWorld.camera.camera_type=CT.Attached
    MyWorld.camera.attached = MyWorld.Objects[0]
    #print(str(Vector2D(Pi,0) * Vector2D(0,4)))
    # print(abs(Vector2D(3,4)))

    Flag = True
    while Flag:
        
        update_screen(win, MyWorld)

        MyWorld.update_objects()

        for event in py.event.get():
            if event.type == py.QUIT:
                Flag = False

                py.quit()
        
            # if event.type==py.MOUSEBUTTONDOWN:
            #     mouse_down(py.mouse.get_pos)
            # if event.type==py.KEYDOWN:
            #     key_down(py.mouse.get_pos,event)
