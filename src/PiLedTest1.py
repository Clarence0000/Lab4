import hal.hal_input_switch as input_switch
import hal.hal_led as led
import time

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay/2)

    led.set_output(0, 0)
    time.sleep(delay/2)


def main():
    input_switch.init()
    led.init()

    while(True):
        switch = input_switch.read_slide_switch()
        if switch == 1:
            blink_led(0.2)

if __name__ =='__main__':
    main()