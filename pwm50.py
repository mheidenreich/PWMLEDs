#!/usr/bin/python3

"""
    Program:    PWM Lookup with a 50-Value Table (pwm50.py)
    Platform:   Raspberry Pi
    Author:     M. Heidenreich, (c) 2020

    Description:

    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/1fKH5PU9eck

    This example demonstrates how to dim LEDs using Raspberry Pi software PWM
    with a lookup table.

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

levels = (
            0, 0.001627653, 0.003387769, 0.005291128, 0.007349387, 0.009575153,
            0.011982057, 0.014584842, 0.017399448, 0.020443115, 0.023734483,
            0.027293711, 0.031142599, 0.03530472, 0.039805565, 0.044672701,
            0.049935937, 0.055627509, 0.061782277, 0.068437936, 0.07563525,
            0.083418301, 0.091834757, 0.100936166, 0.110778273, 0.121421356,
            0.132930602, 0.145376501, 0.15883528, 0.17338937, 0.189127911,
            0.206147295, 0.224551763, 0.244454035, 0.265976007, 0.289249495,
            0.31441704, 0.341632787, 0.371063424, 0.402889205, 0.437305052,
            0.474521752, 0.514767246, 0.558288025, 0.605350641, 0.656243338,
            0.711277817, 0.770791149, 0.835147834, 0.904742036, 0.98
        )

left = PWMLED(13)
middle = PWMLED(19)
right = PWMLED(26)

try:
    left.value = levels[40]    # 80% brigtness
    middle.value = levels[25]  # 50% brightness
    right.value = levels[15]   # 30% brightness

    pause()

except KeyboardInterrupt:
    pass

finally:
    left.close()
    middle.close()
    right.close()
