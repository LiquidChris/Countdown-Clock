from datetime import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import ttk 

## collect countdown data
def collectCDData():
    time = [0,0,0]
    if(hourEntry.get() != ""):
        time[0] = int(hourEntry.get())
    if(minEntry.get() != ""):
       time[1] = int(minEntry.get())
    if (secEntry.get() != ""):
        time[2] = int(secEntry.get())
    return time

## start and stop the countdown
def runCountdown(time): ## time = [hours, minutes, seconds]
    totalSec = (time[0] * 60 * 60) + (time[1] * 60) + time[2]    
    start = datetime.now()
    secsPassed = 0
    timeLeft = totalSec
    while (secsPassed <= totalSec):
        if datetime.now() >= start+timedelta(seconds=secsPassed):
            displayCDStatus(totalSec-secsPassed)
            timeLeft = totalSec-secsPassed
            secsPassed += 1
        continue
    
    cdStatusText.set("The countdown has ended!")
    selectionWindow.update()
    return 0

#################
#################
#### Tkinter ####
#################
#################

## set up countdown window
selectionWindow = tk.Tk()
selectionWindow.geometry("450x450")
selectionWindow.title("Stopwatch")

## frames for timer and stopwatch
mainFrame = tk.Frame(selectionWindow)
mainFrame.pack()
cdFrame = tk.Frame(mainFrame)
cdFrame.pack()

## labels for the frames
cdLabel = tk.Label(cdFrame, text = "Countdown")
cdLabel.pack(side = "top")

## diplay Entrys for the frames
cdStatusText = tk.StringVar(cdFrame)
cdEndText = tk.StringVar(cdFrame)
cdStatusEntry = ttk.Entry(cdFrame, width=30)

## displays the countdown status
def displayCDStatus(timeLeft):
    timeLeftString = ""
    hoursLeft = 0
    minsLeft = 0
    while(timeLeft > 1200):
        timeLeft -= 1200
        hoursLeft += 1
    if hoursLeft < 10:
        timeLeftString += "0"
    timeLeftString += str(hoursLeft)
    timeLeftString += ":"
    
    while(timeLeft > 60):
        timeLeft -= 60
        minsLeft += 1
    if minsLeft < 10:
        timeLeftString += "0"
    timeLeftString += str(minsLeft)
    timeLeftString += ":"
    
    if timeLeft < 10: 
        timeLeftString += "0"
    timeLeftString += str(timeLeft)
    
    cdStatusText.set(timeLeftString)
    cdStatusEntry.configure(textvariable=cdStatusText, foreground="green")
    selectionWindow.update()

## collect countdown data and start countdown
def startCD():
    time = collectCDData()
    runCountdown(time)

## entry boxes and labels for countdown
hourEntry = ttk.Entry(cdFrame)
minEntry = ttk.Entry(cdFrame)
secEntry = ttk.Entry(cdFrame)
hourLabel = ttk.Label(cdFrame, text = "hours:")
minLabel = ttk.Label(cdFrame, text = "minutes:")
secLabel = ttk.Label(cdFrame, text = "seconds:")
hourLabel.pack()
hourEntry.pack()
minLabel.pack()
minEntry.pack()
secLabel.pack()
secEntry.pack()

## buttons for the frames
cdStartButton = ttk.Button(cdFrame, text = "Start Countdown", command = startCD)
cdStartButton.pack()

## pack display for the countdown and timer
cdStatusEntry.pack()

## starts the program
if __name__ == "__main__":
    selectionWindow.mainloop()

import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )