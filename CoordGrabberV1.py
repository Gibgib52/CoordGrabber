# Version 1

# gets mouse coords after delay seconds

import pyautogui
from time import sleep

# gives mouse coords once or twice after default 5 seconds.
def alert_coords(type="single", delay=5):

    screen_width, screen_height = pyautogui.size()
    screen_area = screen_width*screen_height
    # gets area of rect from 2 corner points
    def print_area(x1, y1, x2, y2):
        if x1 < x2: 
            width = x1 - x2
        else:
            width = x2 - x1
        
        if y1 > y2:
            height = y2 - y1
        else:
            height = y1 - y2

        # (x2 - x1) * (y2 - y1)
        calcArea = width * height
        calcPercent = round((calcArea / screen_area) * 100, 2) # round percentage to 2 decimal places

        print(f"Area: {calcArea}px")
        print(f"{calcPercent}% total screen area")

    def single(delay):
        print(f"getting single coord in {delay} seconds")
        sleep(delay)
        mx, my = pyautogui.position()
        coords = (mx, my)
        pyautogui.alert(f"Mouse Position ({mx}, {my})")

        print(f"formatted: {coords}")
        print(f"raw: {mx},{my}")

    def double(delay):
        coords = []

        # first
        print(f"getting first coord in {delay} seconds")
        sleep(delay)
        mx, my = pyautogui.position()
        coords.append((mx,my))
        alertString = f"First Mouse Position ({mx}, {my})\nClick ok to continue..."
        pyautogui.alert(alertString)
        print(alertString)

        # second
        print(f"getting second coord in {delay} seconds")
        sleep(delay)
        mx, my = pyautogui.position()
        coords.append((mx,my))
        alertString = f"Second Mouse Position ({mx}, {my})\nClick ok to continue..."
        pyautogui.alert(alertString)
        print(alertString)

        # extra formats
        print(f"{'-'*8} Other Formats {'-'*8}") # {'-'*8} is shorthand --------. i just think it looks cooler idk
        print(f"formatted: {coords[0]} {coords[1]}")

        x1 = coords[0][0]
        y1 = coords[0][1]
        x2 = coords[1][0]
        y2 = coords[1][1]
        print(f"raw: {x1},{y1} {x2},{y2}")
        print_area(x1, y1, x2, y2)
        
    match type:
        case "single":
            single(delay)
        case "double":
            double(delay)

alert_coords(type="double", delay=2)