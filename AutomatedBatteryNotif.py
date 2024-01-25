# pip install plyer
# pip install psutil
# perform these commands in cmd or terminal
import psutil # retrieves info on running processes &system utilization
from plyer import notification # python library for accessing hw/platform features
import time
#user i/p variable
frequency = eval(input("how often would you like to be notified: "))
battery = psutil.sensors_battery()
percent = battery.percent

#while loop to calculate the change between the said frequency of battery for notification
while(True):
    battery = psutil.sensors_battery()
    curr_percent = battery.percent
    change = curr_percent - percent
    diff = abs(change)
    
    if(diff>=frequency):
        notification.notify(
            title="Current battery",
            message = str(curr_percent) + "%battery remaining",
            timeout = 5#allocating time for loop to run
            )
        percent=curr_percent
    continue
        