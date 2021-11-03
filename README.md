# Poorlabs led driver
A custom driver for Chrolis LED system from ThorLabs


This repository contains all the documentation needed to build a custom driver for a [Chrolis LED system from Thorlabs](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=13597).

Features:
- Synchronisation with 2 photon microscope blanking signal (or any other synchronisation TTL pulse)
  - Synchronisation done via hardware, dispensing the need to include complicated logic on the microcontroller
- Based on ESP32 (uses [BeeHive](https://github.com/BeeHive-org/BeeHive) main breakout board)
- Set of stimuli provided. Based on [Led Zappelin's code](https://github.com/BadenLab/LED-Zappelin)

Skills required:
- Coding (Arduino IDE / Micropython)
- Soldering
- Using a drill, screwdriver
