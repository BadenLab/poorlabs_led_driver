#import necessary libraries on the esp32
import machine

# The ESP model being used only has 8 native PWM ports.
# to circunvent this, we are using a library (below), that makes use
# of the built remote control module native to the ESP32. 
# this gives us another 8 PWM ports.

# library location https://github.com/codemee/esp32_rmt_pwm
from esp32_rmt_pwm import PWM


class Leds:
    def __init__(self):
        #port 1 on the controller box
        led1Pin = 19
        led2Pin = 21
        led3Pin = 14
        led4Pin = 27
        led5Pin = 26
        led6Pin = 25

        #port 2 on the controller box
        led7Pin = 15
        led8Pin = 2
        led9Pin = 16
        led10Pin = 17
        led11Pin = 22
        led12Pin = 23


        triggerPin = 18 
        self.trigger = machine.Pin(triggerPin, machine.Pin.OUT)

        #the refresh rate frequency of the PWM signals
        pwmFreq = 1000
        #resolution of the pwm in bits (will lead to a number of light intensity steps)
        #self.resolution = 10

        #note: the lines below could be done in a loop, but would become more criptic
        #check https://docs.micropython.org/en/latest/esp32/tutorial/pwm.html#esp32-pwm
        # for details

        #all led pins are set to PWM so we can control the LED intensity
        
        self.led1 = machine.PWM(machine.Pin(led1Pin))
        self.led2 = machine.PWM(machine.Pin(led2Pin))
        self.led3 = machine.PWM(machine.Pin(led3Pin))
        self.led4 = machine.PWM(machine.Pin(led4Pin))
        self.led5 = machine.PWM(machine.Pin(led5Pin))
        self.led6 = machine.PWM(machine.Pin(led6Pin))

    
        self.led7 = PWM(machine.Pin(led7Pin)) 
        self.led8 = PWM(machine.Pin(led8Pin))
        self.led9 = PWM(machine.Pin(led9Pin))
        self.led10 = PWM(machine.Pin(led10Pin))
        self.led11 = PWM(machine.Pin(led11Pin))
        self.led12 = PWM(machine.Pin(led12Pin))
        
        
        #make a list with all leds so that it is easier to control all of them with loops
        self.allLeds = [self.led1,self.led2,self.led3,self.led4,self.led5,self.led6,
                        self.led7,self.led8,self.led9,self.led10,self.led11,self.led12
                       ]

        #turn all leds off for good measure
        for led in self.allLeds:
            led.init(freq=pwmFreq, duty=0)