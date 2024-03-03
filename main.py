import webbrowser
import time
import customtkinter
import pyautogui
from customtkinter import *
from PIL import Image


clicks = 0

# Create window, CTk class = basis of CustomTkinter program
window = CTk()
window.geometry("600x600")
window.title("Match Generator Deluxe 2024 (Version: 1.0)")

set_appearance_mode("dark")
set_default_color_theme("blue")

# adjust the path and upload your own cover image
logo = customtkinter.CTkImage(Image.open
                              (r'C:\Users\Frambuesa\PycharmProjects\Tinderbot4\Match Generator Deluxe 2024\cover-image.jpg'),
                              size=(600,400))

# master is always "window" as only one window has been created (see above)
label = customtkinter.CTkLabel(master=window,
                               image=logo,
                               text="")
label.pack()

def start_liking_100():

    # open the tinder website automatically
    webbrowser.open('https://tinder.com/app/recs')

    """ After the website has been loaded, the bot starts (15 seconds)
    if 15 seconds is not enough, simply increase the number of seconds or use the version with 125 clicks
    to perform at least 100 automatic likes."""

    time.sleep(15)

    # determine screen resolution
    wh = pyautogui.size()

    clicks = 0
    global liking
    liking = True

    while (liking):

        # automatically move the mouse cursor to the Like button
        if wh.width == 1920 and wh.height == 1080:
            pyautogui.click(1280, 860, button='left') # click left mouse button automatically
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 100:   # stop the bot after 100 likes
                liking = False

        elif wh.width == 1600 and wh.height == 900:
            pyautogui.click(1060, 710, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 100:
                liking = False

        elif wh.width == 1440 and wh.height == 900:
            pyautogui.click(968, 708, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 100:
                liking = False

        elif wh.width == 1366 and wh.height == 768:
            pyautogui.click(922, 605, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 100:
                liking = False

        elif wh.width == 1280 and wh.height == 720:
            pyautogui.click(870, 560, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 100:
                liking = False


def start_liking_125():
    webbrowser.open('https://tinder.com/app/recs')

    time.sleep(15)
    wh = pyautogui.size()
    clicks = 0
    global liking
    liking = True
    while (liking):

        if wh.width == 1920 and wh.height == 1080:
            pyautogui.click(1280, 860, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 125:
                liking = False

        elif wh.width == 1600 and wh.height == 900:
            pyautogui.click(1060, 710, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 125:
                liking = False

        elif wh.width == 1440 and wh.height == 900:
            pyautogui.click(968, 708, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 125:
                liking = False

        elif wh.width == 1366 and wh.height == 768:
            pyautogui.click(922, 605, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 125:
                liking = False

        elif wh.width == 1280 and wh.height == 720:
            pyautogui.click(870, 560, button='left')
            clicks = clicks + 1
            time.sleep(2)
            if clicks == 125:
                liking = False

button_start_100 = CTkButton(master = window,
                             text = "Start (100x)",
                             font = ("Calibiri", 18),
                             fg_color="#1EB082",
                             height = 80,
                             command = start_liking_100) # Call function start_liking_100

button_start_100.place(x=130, y=480)

button_start_125 = CTkButton(master = window,
                             text = "Start (125x)",
                             font = ("Calibiri", 18),
                             height=80,
                             fg_color ="#B84DF4",
                             command = start_liking_125)

button_start_125.place(x=330, y=480)


title = CTkLabel(master = window,
                 text ="Match Generator Deluxe 2024",
                 font=("Arial", 22),
                 text_color="white",)
title.place(x=153, y=425)

# start program
window.mainloop()