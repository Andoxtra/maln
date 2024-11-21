from RunInThreads import *

tkinterGUI = "Tkinter"
physicalGUI = "Physical"

if __name__ == "__main__":
    while True:
        runner = RunInThreads(tkinterGUI)
        runner.run_game()
