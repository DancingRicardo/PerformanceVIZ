
import tkinter as tk
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw() # Says that you won't be using many tkinter functions


def saveResults():
    # Open the file inside the project path, appending it

        fileToLoad = open(askopenfilename(), 'r')
        # Save the CODE variable to the User's C++ Project.
        print(fileToLoad)
        fileToSave = open(askopenfilename(), 'a')
        fileToSave.write(fileToLoad.read())
        print(fileToSave)
        fileToSave.close()
        print("Saved!")
  
