
#connect to micropython board
#get_ipython().run_line_magic("serialconnect", " to --port=com4 --baud=115200")
get_ipython().run_line_magic("serialconnect", " to --port=/dev/ttyUSB1 --baud=115200")







#import necessary libraries on the esp32
from machine import Pin
from machine import PWM
import time
import math


#define pins and their functions

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
trigger = Pin(triggerPin, Pin.OUT)

#the refresh rate frequency of the PWM signals
pwmFreq = 1000
#resolution of the pwm in bits (will lead to a number of light intensity steps)
resolution = 10

#note: the lines below could be done in a loop, but would become more criptic
#check https://docs.micropython.org/en/latest/esp32/tutorial/pwm.html#esp32-pwm
# for details

pwmFreq = 50  # Hz
intensity = 0# 6.25%
allLeds = (led1Pin,led2Pin, led3Pin,led4Pin,led5Pin,led6Pin,
           led7Pin,led8Pin,led9Pin,led10Pin,led11Pin,led12Pin)
pwms = []
for pin in allLeds:
    pwms.append(PWM(Pin(pin), freq=pwmFreq, duty= intensity))


#all led pins are set to PWM so we can control the LED intensity
#ed1 = machine.PWM(machine.Pin(led1Pin), freq=pwmFreq,resolution = resolution, mode=0, channel=0, timer=0)
#led2 = machine.PWM(machine.Pin(led2Pin), freq=pwmFreq,resolution = resolution,timer=0)
#led3 = machine.PWM(machine.Pin(led3Pin), freq=pwmFreq,resolution = resolution,timer=0)
#led4 = machine.PWM(machine.Pin(led4Pin), freq=pwmFreq,resolution = resolution,timer=0)
#led5 = machine.PWM(machine.Pin(led5Pin), freq=pwmFreq,resolution = resolution,timer=0)
#led6 = machine.PWM(machine.Pin(led6Pin), freq=pwmFreq,resolution = resolution,timer=0)

#led7 = machine.PWM(machine.Pin(led7Pin), freq=pwmFreq,resolution = resolution,timer=1)
#led8 = machine.PWM(machine.Pin(led8Pin), freq=pwmFreq,resolution = resolution,timer=1)
#led9 = machine.PWM(machine.Pin(led9Pin), freq=pwmFreq,resolution = resolution,timer=1)
#led10 = machine.PWM(machine.Pin(led10Pin), freq=pwmFreq,resolution = resolution,timer=1)
#led11 = machine.PWM(machine.Pin(led11Pin), freq=pwmFreq,resolution = resolution,timer=1)
#led12 = machine.PWM(machine.Pin(led12Pin), freq=pwmFreq,resolution = resolution,timer=1)

#make a list with all leds so that it is easier to control all of them with loops
#allLeds = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10,led11,led12]

#turn all leds off for good measure
#for led in allLeds:
#    led.duty(0)

    




print(pwms)


from machine import Pin, PWM



try:
    f = 100  # Hz
    d = 1024 // 16  # 6.25%
    pins = (15, 2, 4, 16, 18, 19, 25,22, 23, 26, 27, 14 , 12, 13, 32, 33)
    pwms = []
    for i, pin in enumerate(pins):
        pwms.append(PWM(Pin(pin), freq=f * (i // 2 + 1), duty= 1023 if i==15 else d * (i + 1),))
        print(pwms[i])
finally:
    for pwm in pwms:
        try:
            pwm.deinit()
        except:
            pass



#support functions needed for protocol
#def count_time(counter=1000,trigger=0,triggerInterval = 500):
#    start = time.ticks_ms() # get millisecond counter
#    stop = start[:]
#    while stop-start<counter:
#        
#        if trigger==1:
#            if math.fmod(stop-start,triggerInterval)==0:
#                trigger.value(1)
#            
#        stop = time.ticks_ms()    


#stimulation protocol 

#turn all leds on and off in turns.

#interval to send triggers in ms
triggerInterval = 500
#baseline interval in ms
baseline = 5*1000
#duration of the on phase per led in ms
onPhase = 3*1000
#duration of the off phase per led in ms
offPhase = 3*1000
#number of repetitions of the entire stimulus (aka trials)
repetitions = 5






#actually start stimulation

#this makes the program wait for the baseline period.
#this is here so that users can start their recording system, than run this cell, 
#which will lead to a baseline recording at the beginning of their recorded traces

###NOTE PORT THE TRIGGER TIMERS TO MICROSECONDS SO THAT TRIGGERS ARE PRECISE ENOUGH

count_time(baseline)
for rep in repetitions:
    for led in allLeds:
        
        led.duty(1024)
        start = time.ticks_ms()   
        stop = time.tick_ms()
        triggerTimer1 = time.ticks()
        triggerTimer2 = time.ticks()
        
        while stop-start<onPhase:
            stop = time.tick_ms()
            if triggerTimer2-triggerTimer1>0 and triggerTimer2-triggerTimer1<=100:
                trigger.value(1)
            if triggerTimer2-triggerTimer1 >= 50:
                trigger.value(0)
            if triggerTimer2-triggerTimer1 >= 500:
                triggerTimer1 = time.ticks_ms()
                triggerTimer2 = time.ticks_ms()
            
            triggerTimer2 = time.tick_ms()
        
        led.duty(0)
        start = time.ticks_ms()   
        stop = time.tick_ms()
        triggerTimer1 = time.ticks()
        triggerTimer2 = time.ticks()
        
        while stop-start<onPhase:
            stop = time.tick_ms()
            if triggerTimer2-triggerTimer1>0 and triggerTimer2-triggerTimer1<=100:
                trigger.value(1)
            if triggerTimer2-triggerTimer1 >= 50:
                trigger.value(0)
            if triggerTimer2-triggerTimer1 >= 500:
                triggerTimer1 = time.ticks_ms()
                triggerTimer2 = time.ticks_ms()
            
            triggerTimer2 = time.tick_ms()
        
        
