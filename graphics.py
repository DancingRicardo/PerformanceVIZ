import pygal
import numpy as np

class LineGraph:

    lineGraph = pygal.Line()

    def __init__(self, title, allruns, lengthOfPath):
        self.lineGraph.title = title

        self.lineGraph.x_labels = map(str, range(0, lengthOfPath))

        distanceBuffer = np.array([])
        timeBuffer = np.array([])

        for i in range(lengthOfPath):
            distanceBuffer = np.append(distanceBuffer, allruns[i, 0])
            pass
        for i in range(lengthOfPath):
            timeBuffer = np.append(timeBuffer, allruns[i, 1])
            pass

        print(allruns.flatten().tolist())
        print(timeBuffer.tolist())
        self.lineGraph.add("Max Distance", distanceBuffer)
        self.lineGraph.add("Time To Finish", timeBuffer)

    def draw(self):
        self.lineGraph.render_in_browser()