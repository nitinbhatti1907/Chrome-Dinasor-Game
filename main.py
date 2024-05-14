# Title :- Automated Chrome Dino Game
# Discription :- The Chrome Dino game is a popular browser-based game that can be found by Google Chrome. It's a simple game where the player controls a dinosaur that runs automatically and has to jump over obstacles by pressing the spacebar. Using Python, it's possible to automate the Chrome Dino game by using a library like PyAutoGUI to control the mouse and keyboard. The basic idea is to use PyAutoGUI to locate the game on the screen, start the game, and then use image recognition to detect when an obstacle is approaching and make the dinosaur jump.

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

def iscollied(data):
    '''
    This function is create one block that indicate the cactus and bird in road when the cactus or bird come at block side the space key will be press automatic and dino jump itself. The block is not visible its a unvisible block.
    '''

    # draw rectangle for birds
    for i in range(275, 325):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit('down')
                return

    # draw rectangle for cactus
    for i in range(275, 325):
        for j in range(563, 700):
            if data[i, j] < 100:
                hit('up')
                return
    return

if __name__ == '__main__':
    '''
    This is the main function the program will start the execution from this function
    '''

    print("Dino Start Running in 3 sec...")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollied(data)

    '''For show the unvisible block run the main-2.py and swift tab on chrome dino game and wait 3 sec then one picture is blink on the screen and block will be visible on that picture.'''
