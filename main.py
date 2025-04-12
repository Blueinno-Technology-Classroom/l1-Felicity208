import pyautogui as gui
from PIL import ImageGrab
import time 

gui.PAUSE = 0


#gui.displayMousePosition()

#screenshot = ImageGrab.grab()
#print(screenshot)

holes = [
    (172, 389),
    (240, 389),
    (306, 389),
    (172, 447),
    (240, 447),
    (306, 447),
    (172, 503),
    (240, 503),
    (306, 503)
]

start_time = time.time()
# time.sleep(2)
gui.click(289, 467)

while time.time() - start_time < 60 :
    print(65 - (time.time() - start_time))
    
    mouseX, mouseY = gui.position()
    # print(mouseX, mouseY)
    screenshot = ImageGrab.grab()
    screenshot_data = screenshot.load()
    # print(screenshot_data[mouseX*2, mouseY*2])


    for hole in holes:
        x = hole[0]*2
        y = hole[1]*2
        r, g, b, _ = screenshot_data[x,y]
        # print(r, g, b)
        if r < 150 and g< 150 and b < 150:
            # print('skip')
            continue
        else:
            # print('click')
            gui.click(hole)
