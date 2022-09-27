from pybricks.tools import wait, StopWatch, DataLog

def run(bb: BaseBits):

    print("Running mission 7 - Calibrate")
   
    bb.ev3.speaker.beep()  # Intro beep

    print("Place both on black")
    
    for i in range(3):  
        bb.ev3.speaker.beep(400 - 50 * i)
        wait(1000)

    left_sum_reflectivity = 0
    right_sum_reflectivity = 0

    for n in range(100): # Find minimum reflectivity

        left_sum_reflectivity += bb.left_color_sensor.reflection()
        right_sum_reflectivity += bb.right_color_sensor.reflection()

    left_min_reflectivity = left_sum_reflectivity/100
    right_min_reflectivity = right_sum_reflectivity/100

    print("minimums", left_min_reflectivity, right_min_reflectivity)

    bb.ev3.speaker.beep()  # Done with minimums, move robot
    bb.robot.straight(-50)  # Back robot off of black line
    
    for i in range(3):  
        bb.ev3.speaker.beep(400 - 50 * i)
        wait(1000)

    for n in range(100):  # Find maximum reflectivty

        left_sum_reflectivity += bb.left_color_sensor.reflection()
        right_sum_reflectivity += bb.right_color_sensor.reflection()

    left_max_reflectivity = left_sum_reflectivity/100
    right_max_reflectivity = right_sum_reflectivity/100

    print("maximums", left_max_reflectivity, right_max_reflectivity)

    bb.ev3.speaker.beep(1000, 3000)  # Done

    left_average_reflectivity = (left_max_reflectivity + left_min_reflectivity)/2  # Calculate average value between white and black for line following
    right_average_reflectivity = (right_max_reflectivity + right_min_reflectivity)/2  # Calculate average value between white and black for line following
    
    print("Average values ", left_average_reflectivity, right_average_reflectivity)


    # bb.robot.drive(30,0)  # Start robot driving straight at medium speed ---------------------------------------

    # left_max_refl = 50   # Variable for highest left reflectivity
    # right_max_refl = 50   # Variable for highest right reflectivity

    # while True:  # Drive until sensor at near edge of black and save highest reflectivity

    #     left_reflectivity = bb.left_color_sensor.reflection()
    #     if left_reflectivity > left_max_refl:     # Test if new highest reflectivity
    #         left_max_refl = left_reflectivity     # Save highest value
        
    #     right_reflectivity = bb.right_color_sensor.reflection()
    #     if right_reflectivity > right_max_refl:     # Test if new highest reflectivity
    #         right_max_refl = right_reflectivity     # Save highest value

    #     if left_reflectivity < 50:    # End loop when at near edge of black
    #         break

    # print("At edge of black, highest value ", left_max_refl, right_max_refl)

    # bb.ev3.speaker.beep()    # At edge of black 

    # left_min_refl = 50   # Variable for lowest left reflectivity
    # right_min_refl = 50   # Variable for lowest right reflectivity          

    # while True:  # Drive until sensor at far edge of black and save lowest reflectivity

    #         left_reflectivity = bb.left_color_sensor.reflection()
    #         if left_reflectivity < left_min_refl:     # Test if new lowest reflectivity
    #             left_min_refl = left_reflectivity     # Save lowest value
            
    #         right_reflectivity = bb.right_color_sensor.reflection()
    #         if right_reflectivity < right_min_refl:     # Test if new lowest reflectivity
    #             right_min_refl = right_reflectivity     # Save lowest value

    #         if left_reflectivity > 50:    # End loop when at near edge of black
    #             break

    # print("At edge of black, lowest value ", left_min_refl, right_min_refl)

    # left_average_refl = (left_max_refl + left_min_refl)/2  # Calculate average value between white and black for line following
    # right_average_refl = (right_max_refl + right_min_refl)/2  # Calculate average value between white and black for line following
    
    # print("Average values ", left_average_refl, right_average_refl)

    # bb.robot.straight(20) # Drive futher so when robot pivots the sensor will be on the edge and pointed along the line
    # bb.ev3.speaker.beep()


