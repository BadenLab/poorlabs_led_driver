import time 
import math

#support functions needed for protocol
def count_time_ms(counter=1000,triggered=1,triggerPin=None):
    triggerDuration = 100  #trigger duration in ms
    triggerInterval = 1000 
    start = time.ticks_ms() # get millisecond counter
    stop = time.ticks_ms() # get millisecond counter
    if triggered==1:
        triggerTimer1 = time.ticks_ms()
        triggerTimer2 = time.ticks_ms()
        
    while stop-start<counter:          
        if triggered==1:
            
            if triggerTimer2-triggerTimer1>0 and triggerTimer2-triggerTimer1<=triggerDuration:
                triggerPin.value(1)
            if triggerTimer2-triggerTimer1 > triggerDuration:
                triggerPin.value(0)
            if triggerTimer2-triggerTimer1 >= triggerInterval:
                triggerTimer1 = time.ticks_ms()
                triggerTimer2 = time.ticks_ms()
            
            triggerTimer2 = time.ticks_ms()
        stop = time.ticks_ms()   
    



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