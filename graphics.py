import pygal
import numpy as np

class LineGraph:

    lineGraph = pygal.Line()

    def __init__(self, title, allruns, lengthOfPath):
        self.lineGraph.title = title

        self.lineGraph.x_labels = map(str, range(0, lengthOfPath))

        buffer = np.array([])

        for i in range(lengthOfPath):
            buffer = np.append(buffer, allruns[i, 0])
            pass

        print(allruns.flatten().tolist())
        print(buffer.tolist())
        self.lineGraph.add(self.lineGraph.title, buffer)

    def draw(self):
        self.lineGraph.render_in_browser()