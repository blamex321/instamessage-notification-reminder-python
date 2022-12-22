import os
#for deleting the "config" folder
from plyer import notification
# Python library for accessing features of your hardware / platforms.
from threading import Timer
# Timer class is used to perform an operation or have a function run after a specified period has passed. The threading class has a subclass called the class timer
import time 
# time module to handle time-related tasks.
from instabot import Bot
#Function to set time to remind the event 
def set_reminder(total_time,message,handle):
    timer = Timer(total_time, reminder)
    timer.start()
    time.sleep(total_time)
    inMessage(message, handle)

#Function to set notification to show the event 
def reminder():
    notification.notify(title=Title, message=message, timeout=10)
#function to send a message Instagram Handle given
def inMessage(message,handle):
    if os.path.isfile("config\file.json"): #Update the json file here
        os.remove("config\file.json")
    bot = Bot()
    bot.login(username = "username",password = "password") # enter your username and password.
    bot.follow(handle) 
    bot.send_message(message,handle)

while True:
    print("                             EVENT REMINDER                               ")
    print("               A simple reminder to remind about the events               \n ")
    Title=input(" Enter the name of the event \n ")
    message = input("Enter your message: ")
    handle = input("Enter Instagram Handle: ")
    days = int(input("\nEnter the number of days: "))
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    total_time = (days * 86400) + (hours * 3600) + minutes * 60 + seconds
    set_reminder(total_time,message,handle)
    if input("\nDo you want to add more reminders? If so please enter 'yes': ").casefold() == "yes":
        continue

    break