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
<<<<<<< HEAD
from missions import mission7
=======

# test change
>>>>>>> d9fba579a716853c393ca1febb0eba89812c635e

class BaseBits:
    """Encapsulates base code for First Lego League projects.  
    
    Includes main loop, a simple paginated menu system, device
    initialization, and top-level error handling""" 
    def __init__(self):
        """Initializes new instance of the class and sets up hardware"""

        # Sets up the hardware and performs initial diagnostics
        try:
            self.ev3 = EV3Brick()  
            self.ev3.light.on(Color.GREEN)
            self.ev3.speaker.beep(frequency=400, duration=200)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"BRICK ERROR")
            self.ev3.print("BRICK ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.left_attachment_motor = Motor(Port.A)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT A MOTOR")
            print("PORT A MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()
    
        try:
            self.left_drive_motor = Motor(Port.B,positive_direction=Direction.CLOCKWISE)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT B MOTOR")
            print("PORT B MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.right_drive_motor = Motor(Port.C,positive_direction=Direction.CLOCKWISE)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT C MOTOR")
            print("PORT C MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:    
            self.right_attachment_motor = Motor(Port.D)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT D MOTOR")
            print("PORT D MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=88, axle_track=111)
            self.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"DRIVEBASE ERROR")
            print("DRIVEBASE ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try: 
            self.left_color_sensor = ColorSensor(Port.S1)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT 1 SENSOR")
            print("PORT 1 SENSOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.right_color_sensor = ColorSensor(Port.S4)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT 4 SENSOR")
            print("PORT 4 SENSOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        self.ev3.screen.clear()
        self.ev3.light.off()
        self.ev3.light.on(Color.GREEN)
        self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
        wait(1000)
        self.ev3.screen.clear()   

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
            ("Calibrate", mission7.run),
            ("8-None", self.previous_page),
            ("<", self.previous_page)
        ]

    def next_page(self, dup_self):
        """Advances to the next page of the menu"""
        self.page = self.page + 1
        print("Advanced to page " + str(self.page))

    def previous_page(self, dup_self):
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
                # button to find the program.  The [1] is finding the stored function
                # that runs the mission.  We are then calling it like a function with
                # the () and passing the BaseBits object in so that function can use it.
                function = self.passes[self.page * 5 + button_index][1]
                function(self)
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
