#get_ipython().run_line_magic("esptool", "  --port=com4 erase")
#get_ipython().run_line_magic("esptool", " --port=COM4 esp32 \".//esp32-20210902-v1.17.bin\"")


#reboot board
get_ipython().run_line_magic("rebootdevice", "")
#connect to micropython board
get_ipython().run_line_magic("serialconnect", " to --port=com4 --baud=115200")







#send files to board
get_ipython().run_line_magic("sendtofile", " --source=\"ports.py\" \"ports.py\"")
get_ipython().run_line_magic("sendtofile", " --source=\"esp32_rmt_pwm.py\" \"esp32_rmt_pwm.py\"")
get_ipython().run_line_magic("sendtofile", " --source=\"full_field_flicker.py\" \"full_field_flicker.py\"")
get_ipython().run_line_magic("sendtofile", " --source=\"support.py\" \"support.py\"")

#reboot board
get_ipython().run_line_magic("rebootdevice", "")

#print board contents
get_ipython().run_line_magic("ls", "")


#import the FFF stimulus on the esp32
import full_field_flicker as fff



stimulus = fff.FFF()




stimulus.baseline = 1*1000 #baseline interval in ms
stimulus.onDuration  = 1*1000 #amount time each led is on in ms
stimulus.offDuration = 1*1000 #amount time each led is off in ms
stimulus.trials = 1 #number of trials


stimulus.start()


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
        
        


get_ipython().run_line_magic("sendtofile", " --source=\"esp32_rmt_pwm.py\" \"esp32_rmt_pwm.py\"")
get_ipython().run_line_magic("rebootdevice", "")
from esp32_rmt_pwm import PWM
from machine import Pin
p25 = PWM(Pin(25))

#p25.freq(261)
p25.duty(768)
#p25.run()
