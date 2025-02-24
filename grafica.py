from vpython import *
import asyncio

scene = canvas(title="Combinación de Conceptos en VPython", width=800, height=600)

def crear_esferas(posicion, radio, n):
    if n == 0:
        return
    esfera = sphere(pos=posicion, radius=radio, color=color.blue)
    crear_esferas(posicion + vector(1.5 * radio, 0, 0), radio * 0.8, n - 1)

crear_esferas(vector(-5, 0, 0), 1, 5)

async def mover_objeto(objeto, eje):
    while True:
        objeto.pos += eje * 0.1
        if objeto.pos.x > 2 or objeto.pos.y > 2 or objeto.pos.z > 2:
            objeto.pos = vector(-2, -2, -2)
        await asyncio.sleep(0.1)

cubo = box(pos=vector(-2, 0, 0), size=vector(1, 1, 1), color=color.red)
esfera = sphere(pos=vector(0, 0, 0), radius=1, color=color.green)

async def main():

    task1 = asyncio.create_task(mover_objeto(cubo, vector(1, 0, 0)))
    task2 = asyncio.create_task(mover_objeto(esfera, vector(0, 1, 0)))
    await asyncio.gather(task1, task2)

asyncio.run(main())