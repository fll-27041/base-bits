def run(bb: BaseBits):
    print("Running mission 1")
    bb.robot.straight(1000)
    bb.ev3.speaker.beep()