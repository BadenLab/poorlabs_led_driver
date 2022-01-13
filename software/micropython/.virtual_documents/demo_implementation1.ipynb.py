#get_ipython().run_line_magic("esptool", "  --port=com4 erase")
get_ipython().run_line_magic("esptool", " --port=COM4 esp32 \".//esp32-20210902-v1.17.bin\"")


#reboot board
#get_ipython().run_line_magic("rebootdevice", "")

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
