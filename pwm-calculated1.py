#!/usr/bin/python3

"""
    Program:    LED Dimming Using Calculated PWM - Example 1 (pwm-calculated1.py)
    Platform:   Raspberry Pi
    Author:     M. Heidenreich, (c) 2020

    Description:

    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/1fKH5PU9eck

    This example demonstrates how dim LEDs using Raspberry Pi and software PWM.
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

steps = 10
fade_factor = steps * log10(2)/log10(steps)

def brightness(level):
    return (pow(2, (level/fade_factor))-1)/steps

right = PWMLED(26)
middle = PWMLED(19)
left = PWMLED(13)

try:
    print("\n            PWM DUTY CYCLE")
    print("LEFT LED        MIDDLE LED        RIGHT LED")
    print("-----------------------------------------------")

    for level in range(1, 11):
        left.value = level/10
        middle.value = pow(2, level)/1024
        right.value = brightness(level)

        print(f"{100*left.value}%\t\t{100*middle.value:3.6f}%\t  {100*right.value:3.6f}%")

        sleep(1)

    pause()

except KeyboardInterrupt:
    pass

finally:
    left.close()
    middle.close()
    right.close()
