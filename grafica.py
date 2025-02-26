from vpython import *
import asyncio
import random
import math

scene = canvas(title="Combinación de Conceptos en VPython", width=800, height=600, background=color.black)

def create_cylinders(posicion, n):
    if n == 0:
        return
    posicion.x = 2
    cylinder(pos=posicion, radius=0.5, color=color.blue)
    create_cylinders(posicion + vector(2, 2, 0), n - 1)

create_cylinders(vector(-5, 0, 0), 5)

conos = [
    cone(pos=vector(-4, 0, 0), radius=0.5, height=1.5, color=color.yellow),
    cone(pos=vector(-3, 0, 0), radius=0.5, height=1.5, color=color.yellow),
    cone(pos=vector(-2, 0, 0), radius=0.5, height=1.5, color=color.yellow),
    cone(pos=vector(-1, 0, 0), radius=0.5, height=1.5, color=color.yellow)
]

cilindro = cylinder(pos=vector(0, 0, 0), radius=0.3, length=1.5, color=color.green)

objects = [cilindro] + conos

move_active = True
angle_cono = 3
angle_cilindro = 0.4

async def move_cubo_recursively(obj, radius, angle_increment):
    global angle_cono
    while True:
        if move_active:
            angle_cono += angle_increment
            obj.pos.x = radius * math.cos(angle_cono)
            obj.pos.z = radius * math.sin(angle_cono)
        await asyncio.sleep(0.1)

async def move_cilindro_recursively(obj, radius, angle_increment):
    global angle_cilindro
    while True:
        if move_active:
            angle_cilindro -= angle_increment
        await asyncio.sleep(0.1)

async def move_conos_recursively():
    while True:
        if move_active:
            for i, cono in enumerate(conos):
                cono.pos.y = math.sin(angle_cono + (i * 0.2)) * 1.5
        await asyncio.sleep(0.1)


def change_colors():
    for objeto in objects:
        objeto.color = vector(random.random(), random.random(), random.random())

def restart_move():
    global move_active, angle_cono, angle_cilindro
    move_active = True
    angle_cono = 0
    angle_cilindro = 0
    cilindro.pos = vector(0, 0, 0)
    for i, cono in enumerate(conos):
        cono.pos = vector(4 + i, 0, 0)

def keydown(evt):
    if evt.key == 'r':
        restart_move()
    elif evt.key == 'c':
        change_colors()

scene.bind('keydown', keydown)

async def main():
    tasks = [
        move_cubo_recursively(cilindro, 2, 0.1),
        move_cilindro_recursively(cilindro, 1, 0.15),
        move_conos_recursively() 
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
