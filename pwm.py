#!/usr/bin/python3

"""
    Program:    PWM Test (pwm.py)
    Platform:   Raspberry Pi
    Author:     M. Heidenreich, (c) 2020

    Description:

    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/1fKH5PU9eck

    This example demonstrates a basic dimming LED technique using gpiozero
    and Raspberry Pi GPIO.

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

left = PWMLED(13)
middle = PWMLED(19)
right = PWMLED(26)

try:
    left.value = 1
    middle.value = 0.5
    right.value = 0.25

    pause()

except KeyboardInterrupt:
    pass

finally:
    left.close()
    middle.close()
    right.close()
