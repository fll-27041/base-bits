def run(bb: BaseBits):
    print("Running mission 1")
    for i in range(2):
        bb.ev3.speaker.beep(frequency=2000, duration=500)
    for i in range(2):
        bb.ev3.speaker.beep(frequency=1000, duration=500)
