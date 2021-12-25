# Importing Image and ImageGrab module from PIL package
from PIL import Image, ImageGrab
import win32api, win32con
from pynput.keyboard import Key, Controller
import time

#Pokemon's RGB code to compare for shiny, this is for the NON Shiny version of the pokemon
RED = 221
GREEN = 217
BLUE = 221

#Creates the upper and lower bounds for the pokemon's color
RED_HIGH = RED +3
RED_LOW = RED -3
GREEN_HIGH = GREEN +3
GREEN_LOW = GREEN - 3
BLUE_HIGH = BLUE +3
BLUE_LOW = BLUE -3


#Keys that map to the NXBT button
HOME = '['
Y = 'j'
A = 'l'
DPAD_UP = 'w'

# XY coordinates for clicking on the Webapp page
webapp_x = 3654
webapp_y = 419


# XY coordinates for the status of the Controller
color_x = 4977
color_y = 135

# XY coordinates for checking the pokemon's color
poke_x = 2211
poke_y = 686


# XY coordinates for restarting the controller
restart_x = 4789
restart_y = 833


# XY coordinates for running the macro
run_x = 4789
run_y = 1190

# Function that can be used to find the XY coordinates for script
def get_cords():
    x,y = win32api.GetCursorPos()
    print(x,y)

# Function that clicks the mouse at specific XY coordinates
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#Im lazy and typing slp is a lot faster for me than typing time.sleep, it takes in pauses the function for sec seconds
def slp(sec):
    time.sleep(sec)

# Checks the color of a specific pixel with a given XY coordinate
def ShinyCheck(x,y):
    left_x = x
    top_y = y
    right_x = left_x + 100
    bottom_y = top_y + 100
    # using the grab method
    im2 = ImageGrab.grab(bbox = (left_x, top_y, right_x, bottom_y), all_screens=True)
    # Uncomment the below to see the pokemon to determine if you need to adjust XY coordinates or timing
    #im2.show()
    rgb_im = im2.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    print(r,g,b)
    return r, g, b

# Putting it all together
def main():
    #Create the Keyboard 
    keyboard = Controller()
    #Keep Track of how many loops we are through
    i = 0
    #Variable to determine whether or not to cancel the loop
    notShiny = True
    while notShiny:

        #click on the webapp
        click(webapp_x,webapp_y)
        slp(0.5)
        click(webapp_x,webapp_y)
        slp(1.4)
        #Start the macro for the hunt
        click(run_x,run_y)
        #the number of seconds in between loops
        slp(76.2)

        #Check the pixel of the Pokemon and store it as an RGB value
        r,g,b = ShinyCheck(poke_x, poke_y)
        i = i+1
        print(i)
        #Check if the pokemon is anything other than the non shiny version
        if r >= RED_LOW and r <= RED_HIGH and g >= GREEN_LOW and g <= GREEN_HIGH and b >= BLUE_LOW and b <= BLUE_HIGH :
            pass
        #If the pokemon is not it's NON Shiny version, code stops running
        else:
            notShiny = False
            break
        #checks if the controller needs to be restarted
        r2,g2,b2 = ShinyCheck(color_x,color_y)
        if r2 >= 93 and r2 <=98 and g2 >= 193 and g2 <=200 and b2 >=76 and b2 <= 82 :
            pass
        else:
            click(restart_x,restart_y)
        #waits to restart the loop
        slp(5)
        
input()
main()

        
        
