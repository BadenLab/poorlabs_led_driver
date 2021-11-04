# Poorlabs stimulus generator
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

Links/tutorials used:
- [getting started with ESP 32 and micropython](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [controlling an ESP with micropython via a Jupyter notebook](https://towardsdatascience.com/micropython-on-esp-using-jupyter-6f366ff5ed9) 
- datasheets:
  - [Chips performing logical AND on the signals to control each LED and the blanking signal](https://www.mouser.co.uk/datasheet/2/308/74LS08-1190273.pdf)
  - [Chip inverting the blanking signal (logical NOT)](https://www.mouser.co.uk/datasheet/2/308/1/MC74HC14A_D-2315678.pdf)

