import datetime
import time
import winsound

# Get the alarm time from the user
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))

# Set up the alarm time as a datetime object
alarm_time = datetime.time(hour=hour, minute=minute)

while True:
    # Get the current time
    now = datetime.datetime.now().time()
    
    # Check if it's time for the alarm
    if now >= alarm_time:
        print("ALARM!")
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
        break
    
    # Wait for one second
    time.sleep(1)
