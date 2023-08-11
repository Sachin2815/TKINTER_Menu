import speech_recognition as sr
import os
import time 
import pywhatkit
import pyautogui
import numpy as np
import matplotlib.pyplot as plt
from twilio.rest import Client
import cv2
from pynput.keyboard import Key, Controller
from geopy.geocoders import Nominatim
keyboard = Controller()
from PIL import Image, ImageDraw
from googlesearch import search
import boto3
import tkinter as tk
def open_software(software_name):
    software_path = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome":"chrome.exe",
        "command prompt":"cmd.exe",
        "explorer":"explorer.exe",
        "vlc":"vlc.exe",
         "taskmgr":"taskmgr",
        # Add more software names and paths here
    }

    if software_name in software_path:
        try:
            os.startfile(software_path[software_name])
        except Exception as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Software not found.")
    pass

def whatsapp():
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+9760736251", 
            message="Hello Linux World",
            tab_close=True
        )
        time.sleep(20)
        pyautogui.click()
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))
        
        
def message():

        client = Client("AC39df9b5371d70d011422b50c00ad1408", "b30460e4fd84223ba4c20e1982644faa")
        client.messages.create(to="+917764950400", 
                               from_="+14177364758", 
                               body="Hello Linux World!")


def click_photo():

   cap=cv2.VideoCapture(0)
   cap
   status ,photo =cap.read()
   cv2.imwrite("pic.jpg",photo)
   cv2.imshow("My photo",photo)
   cv2.waitKey(5000)
   cv2.destroyAllWindows()
   cap.release()

def crop_pic():
   cap=cv2.VideoCapture(0)
   cap
   status ,photo =cap.read()
   cv2.imwrite("pic.jpg",photo)
   cv2.imshow("My photo",photo[200:540,200:430])
   cv2.waitKey(5000)
   cv2.destroyAllWindows()
   cap.release()
    

def capture_video():
    cap=cv2.VideoCapture(0)
    while True:
        status ,photo=cap.read()
        cv2.imshow("My photo",photo)
        if cv2.waitKey(5)==13:
            break
    cv2.destroyAllWindows()

def capture_crop_video():
    cap=cv2.VideoCapture(0)
    while True:
        status ,photo=cap.read()
        photo[0:200,0:200]=photo[200:400,200:400]
        cv2.imshow("My photo",photo)
        if cv2.waitKey(5)==13:
            break
    cv2.destroyAllWindows()

    
def image_100_100():
    # Create a blank canvas for the image
    width = 400
    height = 300
    channels = 3
    image = np.zeros((height, width, channels), dtype=np.uint8)

    #Background (lemon)
    image[:300, 0:400, 0] = 255
    image[:300, 0:400, 1] = 255
    image[:300, 0:400, 2] = 102

    # Table (Brown)
    #1st leg

    image[200:300, 50:100 , 0] = 55
    image[200:300, 50:100, 1] = 0
    image[200:300, 50:100, 2] = 9

    #2nd leg

    image[200:300, 300:350 , 0] = 55
    image[200:300, 300:350, 1] = 0
    image[200:300,300:350, 2] = 9

    # Surface
    image[175:200,25:375, 0] = 55
    image[175:200,25:375, 1] = 0
    image[175:200,25:375, 2] = 9


    # TV (Black)
    # base (black)

    image[160:175,160:240, 0] = 0
    image[160:175,160:240, 1] = 0
    image[160:175,160:240, 2] = 0

    # Screen back
    image[50:160, 100:300,0] = 0
    image[50:160, 100:300,1] = 0
    image[50:160, 100:300,2] = 0

    # Screen(view) (sky blue)

    image[60:150, 110:290, 0] = 108
    image[60:150, 110:290, 1] = 255
    image[60:150, 110:290, 2] = 255
    # Display the image
    plt.imshow(image)
    plt.axis('on')
    plt.show()



    
def get_coordinates():
    location_name = input("enter the city name:")
    geolocator = Nominatim(user_agent="location_finder")
    location = geolocator.geocode(location_name)
    if location is None:
        print(f"Coordinates not found for '{location_name}'.")
        return None
    else:
        latitude = location.latitude
        longitude = location.longitude
        print(f"Coordinates for '{location_name}': Latitude = {latitude}, Longitude = {longitude}.")
        return latitude, longitude

    # Replace 'New York City' with your desired location.
    location_name = input("enter the city name:")
    

def top_10_google_searches():
    query=input("search here")
    try:
        search_results = list(search(query, num_results=10))
        print("Top 10 Google Searches for '{}':".format(query))
        for index, result in enumerate(search_results, start=1):
            print(f"{index}. {result}")
    except Exception as e:
        print("Error: ", str(e))
        
        
def launch_instance():
    launch = boto3.client('ec2',region_name='ap-south-1')
    launch.run_instances(
        ImageId='ami-0ded8326293d3201b',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1
        )
    describe_instance = boto3.client('ec2')
    describe_instance.describe_instances()
    
def create_bucket():
    bucket = boto3.client('s3',region_name='ap-south-1')
    bucket.create_bucket(
    Bucket='sachinbucket28',
    ACL='private',
    CreateBucketConfiguration={
          'LocationConstraint': 'ap-south-1'}
    )
    
    
def use_sns_service():
    sns = boto3.client('sns',region_name='ap-south-1')
    sns.publish(
    Message='Dont take it serious.',
    Subject='this is automatd sns service.',
    TopicArn='arn:aws:sns:ap-south-1:299592517672:python_menu'
    )
    print("email sent")
    

def clear_status():
    status_label.config(text="cleared")

def create_button(parent, label, command):
    button = tk.Button(parent,font=("Arial",10,"bold"), text=label,width=20,height=2, command=command)
    return button


root = tk.Tk()
root.title("Main Window")
root.geometry("1200x900")
root.configure(bg="Orange")

title_label = tk.Label(root, text="Welcome to Menu",width=30,height=2, font="title_font", fg="#d44026")
title_label.pack(pady=15)

open_button = tk.Button(root, text="Open Software",fg="green",font=("Arial", 20, "bold"),width=25,command=lambda: open_software(software_entry.get().lower()))
open_button.pack()

software_entry = tk.Entry(root,width=64)
software_entry.pack(pady=20)


buttons_frame = tk.Frame(root, bg="lightblue")
buttons_frame.pack(padx=20, pady=20, fill="both", expand=True)


button_notepad = create_button(buttons_frame, "NOTEPAD",lambda: open_software("notepad"))
button_calculator = create_button(buttons_frame, "CALCULATOR", lambda: open_software("calculator"))
button_paint = create_button(buttons_frame, "PAINT", lambda: open_software("paint"))
button_chrome = create_button(buttons_frame, "CHROME", lambda: open_software("chrome"))
button_cmd = create_button(buttons_frame, "COMMAND PROMPT", lambda: open_software("command prompt"))
button_explorer = create_button(buttons_frame, "EXPLORER", lambda: open_software("explorer"))
button_vlc = create_button(buttons_frame, "VLC", lambda: open_software("vlc"))
button_taskmgr = create_button(buttons_frame, "TASK MANAGER",lambda: os.system("taskmgr"))
button_whatsapp = create_button(buttons_frame, "SEND WHATSAPP", whatsapp)
button_message = create_button(buttons_frame, "SEND MESSAGE", message)
button_photo = create_button(buttons_frame, "CLICK PHOTO",click_photo)
button_croppic = create_button(buttons_frame, "CROP PHOTO",crop_pic)
button_video = create_button(buttons_frame, "CAPTURE VIDEO",capture_video)
button_cropvideo = create_button(buttons_frame,"CROP VIDEO",capture_crop_video)
button_image= create_button(buttons_frame,"Image_creation",image_100_100)
button_coordinates = create_button(buttons_frame,"GEO COORDINATES" ,lambda:get_coordinates())
button_searchresults = create_button(buttons_frame,"TOP10GOOGLESEARCHES",lambda:top_10_google_searches())
button_launchinstance = create_button(buttons_frame,"LAUNCH INSTANCE",launch_instance)
button_createbucket = create_button(buttons_frame,"CREATE BUCKET",create_bucket)
button_usesnsservice = create_button(buttons_frame,"USE SNS SERVICE",use_sns_service)

button_notepad.grid(row=0, column=0, padx=10, pady=20)
button_calculator.grid(row=0, column=1, padx=20, pady=20)
button_paint.grid(row=0, column=2, padx=30, pady=20)
button_chrome.grid(row=0, column=3, padx=10, pady=20)
button_cmd.grid(row=1, column=0, padx=20, pady=20)
button_explorer.grid(row=1, column=1, padx=30, pady=20)
button_vlc.grid(row=1, column=2, padx=10, pady=20)
button_taskmgr.grid(row=1, column=3, padx=10, pady=20)
button_whatsapp.grid(row=2, column=0, padx=20, pady=20)
button_message.grid(row=2, column=1, padx=30, pady=20)
button_photo.grid(row=2, column=2, padx=20, pady=20)
button_croppic.grid(row=2, column=3, padx=30, pady=20)
button_video.grid(row=3, column=0, padx=40, pady=20)
button_cropvideo.grid(row=3, column=1, padx=50, pady=20)
button_image.grid(row=3, column=2,padx=40, pady=20)
button_coordinates.grid(row=3, column=3, padx=50, pady=20)
button_searchresults.grid(row=4, column=0, padx=40, pady=20) 
button_launchinstance.grid(row=4, column=1, padx=40, pady=20)
button_createbucket.grid(row=4, column=2, padx=40, pady=20)
button_usesnsservice.grid(row=4, column=3, padx=40, pady=20)

status_label = tk.Label(root, text="", fg="red")
status_label.pack(pady=10)

clear_button = tk.Button(root, text="Clear Status",fg="blue",font=("Arial", 20, "bold"),width=25 ,command=clear_status)
clear_button.pack()

root.mainloop()
