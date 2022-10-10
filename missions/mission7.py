from pybricks.tools import wait, StopWatch, DataLog

def run(bb: BaseBits):

    print("Running mission 7 - Calibrate")
   
    bb.ev3.speaker.beep()  # Intro beep

    print("Place both on black")
    bb.ev3.screen.draw_text(0,20,"Sensors on Black")
    
    for i in range(3):  
        bb.ev3.speaker.beep(800 - 100 * i)
        wait(1000)

    left_sum_reflectivity = 0
    right_sum_reflectivity = 0

    for n in range(100): # Find minimum reflectivity

        left_sum_reflectivity += bb.left_color_sensor.reflection()
        right_sum_reflectivity += bb.right_color_sensor.reflection()

    left_min_reflectivity = left_sum_reflectivity/100
    right_min_reflectivity = right_sum_reflectivity/100

    print("minimums", left_min_reflectivity, right_min_reflectivity)

    bb.ev3.screen.clear()
    bb.ev3.screen.draw_text(0,20,"Sensors on White")

    bb.ev3.speaker.beep()  # Done with minimums, move robot
    bb.robot.straight(-50)  # Back robot off of black line
    
    for i in range(3):  
        bb.ev3.speaker.beep(800 - 100 * i)
        wait(1000)

    for n in range(100):  # Find maximum reflectivty

        left_sum_reflectivity += bb.left_color_sensor.reflection()
        right_sum_reflectivity += bb.right_color_sensor.reflection()

    left_max_reflectivity = left_sum_reflectivity/100
    right_max_reflectivity = right_sum_reflectivity/100

    print("maximums", left_max_reflectivity, right_max_reflectivity)

    left_average_reflectivity = (left_max_reflectivity + left_min_reflectivity)/2  # Calculate average value between white and black for line following
    right_average_reflectivity = (right_max_reflectivity + right_min_reflectivity)/2  # Calculate average value between white and black for line following
    
    print("Average values ", left_average_reflectivity, right_average_reflectivity)

    bb.ev3.screen.clear()  # Clear screen before drawing results

    bb.ev3.screen.draw_text(0,0,"Average Values")

    bb.ev3.screen.draw_text(0,30,"PRT1")  # Draw top line of headers
    bb.ev3.screen.draw_text(100,30, int(left_average_reflectivity))
    bb.ev3.screen.draw_text(0,60,"PRT4")
    bb.ev3.screen.draw_text(100,60, int(right_average_reflectivity))
    bb.ev3.screen.draw_text(0,90,"Cntr Bttn to Stop")

    pressed = []  # Check if a button has been pressed

    while len(pressed) != 1:  # Loop until a button is pressed
        pressed = bb.ev3.buttons.pressed()

    button = pressed[0]  # Remember which button was pressed
    bb.ev3.screen.clear()  # Clear the screen so it is cleabn for selected program
    bb.ev3.speaker.beep(1500, 100)  # Let user know a button was pressed

    # Now wait for the button to be released before starting selected code
    while any(ev3.buttons.pressed()):  # Don't start new program until button released
        pass
    
    bb.ev3.speaker.beep()  # Done, return to menu


    data = DataLog('left_average_reflectivity, right_average_reflectivity')

    data.log(left_average_reflectivity, right_average_reflectivity)

