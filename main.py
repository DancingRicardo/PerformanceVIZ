# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import graphics
import terminalgrabber as tg
import pygame as pg
import pygame_textinput as textinput

pg.init()

performanceContainer = np.array([])

# Create TextInput-object
textObj = textinput.TextInputVisualizer()

screen = pg.display.set_mode((1000, 700))
clock = pg.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pg.event.get()

    # Feed it with events every frame
    textObj.update(events)
    # Blit its surface onto the screen
    screen.blit(textObj.surface, (10, 10))

    for event in events:
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            exit()
    buffer = tg.readPerformance(textObj.value)
    performanceContainer = np.append(performanceContainer, buffer)

    pg.display.update()
    clock.tick(30)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(performanceContainer.itemsize)
graph = graphics.LineGraph('TestGraph', performanceContainer, 8)

tg.saveResults()

graph.draw()


