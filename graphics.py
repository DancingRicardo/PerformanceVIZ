import pygal
import numpy as np

class LineGraph:

    lineGraph = pygal.Line()

    def __init__(self, title, allruns, lengthOfPath):
        self.lineGraph.title = title

        self.lineGraph.x_labels = map(str, range(0, lengthOfPath))

        distanceBuffer = np.array([])
        timeBuffer = np.array([])

        print("All Runs: ", allruns)

        for i in range(0, lengthOfPath):
            print(allruns[i])
            if i % 2:
                timeBuffer = np.append(timeBuffer, allruns[i])
            else:
                distanceBuffer = np.append(distanceBuffer, allruns[i])

        print(allruns.tolist())
        print(timeBuffer.tolist())
        self.lineGraph.add("Max Distance", distanceBuffer)
        self.lineGraph.add("Time To Finish", timeBuffer)

    def draw(self):
        self.lineGraph.render_in_browser()
