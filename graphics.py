import pygal
import numpy as np

class LineGraph:

    lineGraph = pygal.Line()

    def __init__(self, title, allruns, lengthOfPath):
        self.lineGraph.title = "Performance Over Time"

        for runData in allruns:
            # Should loop through
            pass
        pass

    def draw(self):
        pass