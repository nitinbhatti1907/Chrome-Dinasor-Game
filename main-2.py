
"""For Play and Run Code Go To :- chrome://dino/"""

import time
import pyautogui as pg
from PIL import Image,ImageGrab

def hit(key):
    '''
    This function is hit the space key before collision is occured
    '''

    pg.keyDown(key)
    return

if __name__ == '__main__':
    '''
    This is the main function the program will start the execution from this function
    '''

    print("dino Start Running in 2 sec...")
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()

        # draw rectangle for birds
        for i in range(275, 325):
            for j in range(410, 563):
                data[i, j]=91

        # draw rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 700):
                data[i, j]=0

        image.show()
        break

    '''
    For show the unvisible block run the main-2.py and swift tab on chrome dino game 
    and wait 2 sec then one picture is blink on the screen and block will be visible on 
    that picture.
    '''
