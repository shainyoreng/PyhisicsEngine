from ObjectClass import Object, Object_Info
from WorldClass import World
from Enums import *
from pygame.time import Clock
from Vectors import Vector2D
import pygame as py
from tokenize import Double
from logging import raiseExceptions
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""


"""
types:
body, spring, planet, rope, wall

precision:
low, med, high, super high
"""


def update_screen(screen, world):
    world.camera.update()
    screen.blit(bg, (screen.get_size()[0]//2 - bg.get_size()[0]//2 - world.camera.get_pos().x,
                     screen.get_size()[1]//2 - bg.get_size()[1]//2 + world.camera.get_pos().y))

    for object in world.get_objects():
        object.draw(screen)

    screen = py.transform.flip(screen, False, True)

    py.display.update()


if __name__ == '__main__':
    bg = py.image.load("Background.png")
    
    py.init()

    FPS=60

    width = 700
    height = 700
    win = py.display.set_mode((width, height))

    Precision = Pr.Med

    MyWorld = World()
    MyWorld.add_object(OT.Body, Object_Info())
    MyWorld.add_object(OT.Body, Object_Info())

    MyWorld.Objects[1].info.pos = Vector2D(400, 400)
    MyWorld.Objects[1].info.speed = Vector2D(0, 0)
    MyWorld.Objects[1].info.color = (220, 10, 50)
    # MyWorld.Objects[0].info.width = 0
    MyWorld.camera.camera_type = CT.Attached
    MyWorld.camera.attached = MyWorld.Objects[0]
    #print(str(Vector2D(Pi,0) * Vector2D(0,4)))
    # print(abs(Vector2D(3,4)))

    Flag = True
    while Flag:

        update_screen(win, MyWorld)

        MyWorld.update_objects(FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                Flag = False

                py.quit()

            # if event.type==py.MOUSEBUTTONDOWN:
            #     mouse_down(py.mouse.get_pos)
            # if event.type==py.KEYDOWN:
            #     key_down(py.mouse.get_pos,event)
