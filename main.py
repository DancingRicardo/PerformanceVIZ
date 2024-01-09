# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import graphics

performanceContainer = np.array([[0,0], [3,0], [6,3], [9,1], [12,2], [15,0], [18,3], [21,1]])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(performanceContainer.itemsize)
graph = graphics.LineGraph('TestGraph', performanceContainer, 8)

graph.draw()

print('test')