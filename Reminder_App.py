import time
import os

target_hour = int(input('Enter your Hour(24 hour system): '))
target_min = int(input('Enter your Min: '))
reminder = input('Enter your reminder: ')

while True:
    current_hour = time.localtime().tm_hour
    current_min = time.localtime().tm_min

    if current_hour == target_hour and current_min == target_min:
        desktop_path = r"C:\Users\Harris\OneDrive\Desktop\Reminder.txt"
        with open(desktop_path,'w') as file:
            file.write(reminder)
        os.startfile(desktop_path)
        break

time.sleep(30)