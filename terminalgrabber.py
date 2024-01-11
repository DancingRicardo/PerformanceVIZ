
import tkinter as tk
from tkinter.filedialog import askopenfilename
import numpy as np

tk.Tk().withdraw() # Says that you won't be using many tkinter functions


def saveResults():
    # Open the file inside the project path, appending it
    try:
        fileToLoad = open(askopenfilename(), 'r')
        # Save the CODE variable to the User's C++ Project.
        print(fileToLoad)
        fileToSave = open(askopenfilename(), 'a')
        fileToSave.write(fileToLoad.read())
        print(fileToSave)
        fileToSave.close()
        print("Saved!")
    except:
        print("Not Saved. ):")

def readPerformance(performanceString):

    """buffer = np.array([]) # Code that I struggled to make but as it turns out I
        # only needed one line of code. ):

    useForDistance = False

    lastCheckWasFalse = False

    decimalContainerString = ""

    for i in range(0, len(performanceString)):
        if performanceString[i].isdigit() is True or performanceString[i] == ".":
            decimalContainerString = decimalContainerString + str(performanceString[i])
            lastCheckWasFalse = False
            print(str(performanceString[i]))
        else:
            if not lastCheckWasFalse:
                print("String: ", decimalContainerString)
                finalNumberToAdd = np.int32(decimalContainerString)
                buffer = np.append(buffer, [finalNumberToAdd, useForDistance])
                decimalContainerString = ""
                lastCheckWasFalse = True
                useForDistance = not useForDistance

    finalNumberToAdd = np.int32(decimalContainerString)
    buffer = np.append(buffer, [finalNumberToAdd, useForDistance])

    ogBufferSize = buffer.size

    print(ogBufferSize)
    for i in range(0, ogBufferSize - 1):
        if i % 2:
            buffer = np.delete(buffer, i)

    print(buffer)"""

    stringbuffer = np.array([])
    returnBuffer = np.array([])

    stringbuffer = np.append(stringbuffer, performanceString.split(","))

    if (stringbuffer.size != 0):
        for val in stringbuffer:
            returnBuffer = np.append(returnBuffer, float(val))
    print(returnBuffer)
    return returnBuffer

