#!/usr/bin/python3

"""
    Program: LED Dimming Using Calculated PWM - Example 2 (pwm-calculated2.py)
    Author:  M. Heidenreich, (c) 2020

    Description:

    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/1fKH5PU9eck

    This example demonstrates how dim LEDs using Raspberry Pi and software PWM,
    The formula used compensates for the non-linear LED-PWM interaction.

    THIS SOFTWARE AND LINKED VIDEO TOTORIAL ARE PROVIDED "AS IS" AND THE
    AUTHOR DISCLAIMS ALL WARRANTIES INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from signal import pause
from time import sleep
from gpiozero import PWMLED
from math import log10

steps = 100
fade_factor = steps * log10(2)/log10(steps)

def brightness(level):
    return (pow(2, (level/fade_factor))-1)/steps

right = PWMLED(26)
middle = PWMLED(19)
left = PWMLED(13)

try:
    left.value = brightness(75)     # 75% brightness
    middle.value = brightness(50)   # 50% brightness
    right.value = brightness(25)    # 25% brightness

    pause()

except KeyboardInterrupt:
    pass

finally:
    left.close()
    middle.close()
    right.close()
