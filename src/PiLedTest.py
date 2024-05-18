import hal.hal_input_switch as SWITCH
import hal.hal_led as LED
import time
global i

def main():
    i=0
    LED.init()
    SWITCH.init()
    level = 1
    while(1):
        i=0
        switch_pos = SWITCH.read_slide_switch()
        if (switch_pos==1):
            while i<50:
                LED.set_output(24, level)
                level = not level
                time.sleep(0.1)
                i+=1
                print(i,i)
            if i>=50:
                LED.set_output(24,0)
        if i>=50:
            LED.set_output(24,0)
            break

        else:
            
            LED.set_output(24, level)
            level = not level
            time.sleep(0.05)


if __name__ == "_main_":
    main()
