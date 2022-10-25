from pybricks.tools import wait, StopWatch, DataLog

def run(bb: BaseBits):

    print("Running mission 7 - Calibrate")
   
    bb.ev3.speaker.beep()  # Intro beep

    # Get sensor values for black
    print("Place both on black, then press button")
    bb.ev3.screen.draw_text(0,10,"Place both Sensors")
    bb.ev3.screen.draw_text(0,40, "   On black then")
    bb.ev3.screen.draw_text(0,70, "Press center button")
    
    pressed = []  # Check if a button has been pressed
    while len(pressed) != 1:  # Loop until a button is pressed - Waiting for Black
        pressed = bb.ev3.buttons.pressed()

    bb.ev3.screen.clear()  # Clear the screen so it is clean for next step
    bb.ev3.speaker.beep(1500, 100)  # Let user know a button was pressed

    left_min_reflectivity = bb.left_color_sensor.reflection()
    right_min_reflectivity = bb.right_color_sensor.reflection()

    print("minimums", left_min_reflectivity, right_min_reflectivity)

    # Now wait for the button to be released before starting next code
    while any(bb.ev3.buttons.pressed()):  # Don't start new program until button released
        pass

    # Get sensor values for white
    print("Place both on white, then press button")
    bb.ev3.screen.draw_text(0,10,"Place both Sensors")
    bb.ev3.screen.draw_text(0,40, "   On white then")
    bb.ev3.screen.draw_text(0,70, "Press center button")
    
    pressed = []  # Check if a button has been pressed
    while len(pressed) != 1:  # Loop until a button is pressed - Waiting for White
        pressed = bb.ev3.buttons.pressed()

    bb.ev3.screen.clear()  # Clear the screen so it is clean for next step
    bb.ev3.speaker.beep(1500, 100)  # Let user know a button was pressed

    left_max_reflectivity = bb.left_color_sensor.reflection()
    right_max_reflectivity = bb.right_color_sensor.reflection()

    print("maximums", left_max_reflectivity, right_max_reflectivity)

    # Now wait for the button to be released before starting next code
    while any(bb.ev3.buttons.pressed()):  # Don't start new program until button released
        pass


    left_average_reflectivity = int((left_max_reflectivity + left_min_reflectivity)/2)  # Calculate average value between white and black for line following
    right_average_reflectivity = int((right_max_reflectivity + right_min_reflectivity)/2)  # Calculate average value between white and black for line following
    
    print("Average values ", left_average_reflectivity, right_average_reflectivity)

    bb.ev3.screen.clear()  # Clear screen before drawing results

    bb.ev3.screen.draw_text(0,0,"Values   Left  Right")
    bb.ev3.screen.draw_text(0,30,"Black")
    bb.ev3.screen.draw_text(90, 30, left_min_reflectivity)
    bb.ev3.screen.draw_text(140, 30, right_min_reflectivity)

    bb.ev3.screen.draw_text(0,60,"White")
    bb.ev3.screen.draw_text(90, 60, left_max_reflectivity)
    bb.ev3.screen.draw_text(140, 60, right_max_reflectivity)

    bb.ev3.screen.draw_text(0,90,"Average")
    bb.ev3.screen.draw_text(90, 90, left_average_reflectivity)
    bb.ev3.screen.draw_text(140, 90, right_average_reflectivity)

    pressed = []  # Check if a button has been pressed
    while len(pressed) != 1:  # Loop until a button is pressed - Waiting for Black
        pressed = bb.ev3.buttons.pressed()

    bb.ev3.speaker.beep(1500, 100)  # Let user know a button was pressed

    # Now wait for the button to be released before starting next code
    while any(bb.ev3.buttons.pressed()):  # Don't start new program until button released
        pass    



