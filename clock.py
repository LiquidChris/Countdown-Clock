from datetime import datetime
from datetime import timedelta

def runTimer():
    input("Press enter to start TIMER.")
    start = datetime.now()
    input("Press enter to stop TIMER.")
    end = datetime.now()
    
    print("hours:minutes:seconds:milliseconds")
    print(end-start)
    return 0

def runCountdown():
    hr = input("How many hours will the COUNTDOWN run: ")
    min = input("How many minutes will the COUNTDOWN run: ")
    sec = input("How many seconds will the COUNTDOWN run: ")
    input("Press enter to start COUNTDOWN.")
    start = datetime.now()
    while (datetime.now() <= start+timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))):
        continue

    print("The COUNTDOWN has ended.")
    return 0

while(True):
    select = input("Do you want to use COUNTDOWN or TIMER? (C/T/STOP): ")
    if select == "T":
        runTimer()
    elif select == "C":
        runCountdown()
    elif select == "STOP":
        break