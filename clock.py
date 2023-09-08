from datetime import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import ttk 

## starts the timer (but it won't stop!!)
# def runTimer():
#     start = datetime.now()
#     toggleButtonText()

#     while (tButtonText.get() == "Stop timer"):
#         continue
#     # input("Press enter to stop TIMER.")
#     end = datetime.now()
#     toggleButtonText()
    
#     print("hours:minutes:seconds:milliseconds")
#     print(end-start)

## toggles the button text
# def toggleButtonText():
#     buttonText = tButtonText.get()
#     if buttonText == "Start timer":
#         tButtonText.set("Stop timer")
#     elif buttonText == "Stop timer":
#         tButtonText.set("Reset timer") 
#     else:
#         tButtonText.set("Start timer") 
#     selectionWindow.update()


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
    i = 0
    timeLeft = totalSec
    while (datetime.now() <= start+timedelta(seconds=totalSec)):
        if datetime.now() >= start+timedelta(seconds=i):
            displayCDStatus(timeLeft)
            timeLeft = totalSec-i
            i += 1
        continue
    
    cdStatusText.set("The countdown has ended!")
    selectionWindow.update()
    return 0

## collect timer data and start timer
# def startT():
#     runTimer()

## toggles the button test to end the timer
# def stopT():
#     toggleButtonText()

## toggles the button text and resets the display
# def restT():
#     return None

## decides what the button will do based on the name of the button
# def toggleCommand():
#     buttonText = tButtonText.get()
#     if buttonText == "Start timer":
#         startT()
#     elif buttonText == "Stop timer":
#         stopT()

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
# tFrame = tk.Frame(mainFrame)
cdFrame = tk.Frame(mainFrame)
# tFrame.pack(side = "left")
# cdFrame.pack(side = "right")
cdFrame.pack()

## labels for the frames
# tLabel = tk.Label(tFrame, text = "Timer")
cdLabel = tk.Label(cdFrame, text = "Countdown")
# tLabel.pack(side = "top")
cdLabel.pack(side = "top")

## collect timer data
# def collectTData():
#     return None

## diplay Entrys for the frames
cdStatusText = tk.StringVar(cdFrame)
cdEndText = tk.StringVar(cdFrame)
# tStatusEntry = ttk.Entry(tFrame)
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
    cdStatusEntry.configure(textvariable=cdStatusText)
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
# tButtonText = tk.StringVar(tFrame)
# tButtonText.set("Start timer")
# tStartButton = ttk.Button(tFrame, textvariable = tButtonText, command = toggleCommand)
cdStartButton = ttk.Button(cdFrame, text = "Start Countdown", command = startCD)
# tStartButton.pack()
cdStartButton.pack()

## pack display for the countdown and timer
# tStatusEntry.pack()
cdStatusEntry.pack()

selectionWindow.mainloop()