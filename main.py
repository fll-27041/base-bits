#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import math
import sys
import os

from missions import mission1
from missions import mission2
from missions import mission3
from missions import mission4
from missions import mission5

class BaseBits:
    """Encapsulates base code for First Lego League projects.  
    
    Includes main loop, a simple paginated menu system, device
    initialization, and top-level error handling""" 
    def __init__(self):
        """Initializes new instance of the class and sets up hardware"""
        self.ev3 = EV3Brick()
        self.motorA = Motor(Port.A)
        self.motorB = Motor(Port.B)
        self.motorC = Motor(Port.C)
        self.motorD = Motor(Port.D)

        self.robot = DriveBase(self.motorB, self.motorC, wheel_diameter=56,
                                axle_track=152)
        self.robot.settings(straight_speed=200, straight_acceleration=100,
                            turn_rate=100, turn_acceleration=100)

        self.sensor1 = ColorSensor(Port.S1)
        self.sensor4 = ColorSensor(Port.S4)

        # Represents what page of the menu we are on
        self.page = 0

        # Menu items, consisting of a numbered mission and a four-letter code
        # and the function within the module to run.  By default uses the 
        # greater than and less-than characters to advance / go back to different
        # pages of the menu, in case the number of items exceeds the buttons.
        self.passes = [
            ("1-Pump", mission1.run),
            ("2-Agua", mission2.run),
            ("3-Dyno", mission3.run),
            ("4-Push", mission4.run),
            (">", self.next_page),
            ("5-Wind", mission5.run),
            ("6-None", self.previous_page),
            ("7-None", self.previous_page),
            ("8-None", self.previous_page),
            ("<", self.previous_page)
        ]

    def next_page(self):
        """Advances to the next page of the menu"""
        self.page = self.page + 1
        print("Advanced to page " + str(self.page))

    def previous_page(self):
        """Goes back to the previous page of the menu"""
        self.page = self.page - 1
        print("Going back to page " + str(self.page))

    def setup_screen(self):
        """Draws the menu on the screen, based on the current page"""
        self.ev3.screen.clear()
        
        # Constants representing top, left, bottom, right, and center.
        # Optimized for 6-character display strings
        positions = [(50, 0), (105, 50), (50, 100), (0, 50), (80, 50)]
        items_per_page = 4

        # Find our offset into our list of passes (aka missions), and 
        # display the relevant menu items.
        offset = self.page * items_per_page + self.page
        for i in range(len(self.passes[offset:offset + 5])):
            self.ev3.screen.draw_text(positions[i - offset][0],
                                      positions[i - offset][1],
                                      self.passes[offset + i][0])

        # Draw a simple page indicator (for example, 1/3 if there are 3 pages)
        self.ev3.screen.draw_text(142, 100, str(self.page + 1) + "/" +
                                  str(math.ceil(len(self.passes) / 5)))

    def main_menu_loop(self):
        """Main loop for the program.

        Draws a menu, waits for key presses, and then launches the mission
        assoicated with that key press."""
        
        # Draw the main menu
        self.setup_screen()

        # Keep a list of buttons that can be pressed, which we'll use to 
        # cut down on some duplicate code.
        buttons = [Button.UP, Button.RIGHT, Button.DOWN, Button.LEFT,
                   Button.CENTER]

        # Main loop
        while True:
            pressed = []
            while pressed is None or len(pressed) != 1:
                # If we don't have anything pressed, perform a small
                # sleep to avoid burning CPU cycles (and precious battery)
                time.sleep(0.01)
                pressed = self.ev3.buttons.pressed()
            
            # Find which button was pressed, both the object and simple 0-4 number
            button = pressed[0]
            button_index = buttons.index(button)

            # Delay until button is raised - this avoids accidental multi-launch
            # of the function if the button is held down.
            while any(self.ev3.buttons.pressed()):
                pass

            # Play a nice triplet tone for user feedback, different sounds for 
            # different buttons (but not menu navigation)
            if not button == Button.CENTER:
                for i in range(3):
                    self.ev3.speaker.beep(200 + 50 * button_index + 20 * i)
            # Blank the screen in case the program wants to draw something
            self.ev3.screen.clear()

            # Clear the screen and run the mission.  If an error happens, we 
            # play a sound and print it, but don't halt the rest of the main
            # menu.
            try:
                # A note on the syntax: we are first getting the function to run
                # from the passes list, which is a list of 2-element tuples.
                # The individual missions are grouped into pages of 5, so we 
                # multiple by the current page number, then add the number of the 
                # button to find the program.  The [1] is funding the stored function
                # that runs the mision.  We are then calling it like a function with
                # the () and passing the BaseBits object in so that function can use it.
                self.passes[self.page * 5 + button_index][1](self)
            except Exception as e:
                print(str(e))
                # Play a very disappointed noise
                for i in range(5):
                    self.ev3.speaker.beep(100)
            self.setup_screen()


if __name__ == '__main__':
    print("Initializing base-bits!  Hello World!")
    base_bits = BaseBits()
    base_bits.main_menu_loop()
