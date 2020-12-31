#!/usr/bin/python3

"""
    Program: PWM Lookup with a 100-Value Table (pwm100.py)
    Author:  M. Heidenreich, (c) 2020

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
            0, 0.000471285480509, 0.000964781961432, 0.001481536214969,
            0.002022644346174, 0.002589254117942, 0.003182567385564,
            0.003803842646029, 0.004454397707459, 0.005135612484362,
            0.005848931924611, 0.006595869074376, 0.007378008287494,
            0.0081970085861, 0.009054607179632, 0.009952623149689,
            0.01089296130854, 0.011877616239496, 0.012908676527678,
            0.013988329190195, 0.015118864315096, 0.016302679918954,
            0.017542287033382, 0.018840315031266, 0.02019951720402,
            0.021622776601684, 0.023113112148259, 0.024673685045253,
            0.02630780547701, 0.028018939632056, 0.02981071705535,
            0.031686938347034, 0.033651583224017, 0.035708818961488,
            0.037863009232264, 0.040118723362727, 0.042480746024977,
            0.044954087385763, 0.047543993733716, 0.050255958607436,
            0.053095734448019, 0.05606934480076, 0.059183097091894,
            0.062443596007499, 0.065857757502918, 0.069432823472428,
            0.073176377110267, 0.077096358995608, 0.081201083935591,
            0.085499258602144, 0.09, 0.09471285480509, 0.099647819614319,
            0.104815362149688, 0.110226443461741, 0.115892541179417,
            0.121825673855641, 0.128038426460288, 0.134543977074593,
            0.141356124843621, 0.148489319246111, 0.155958690743756,
            0.163780082874938, 0.171970085860998, 0.180546071796325,
            0.189526231496888, 0.198929613085404, 0.208776162394955,
            0.219086765276777, 0.229883291901949, 0.241188643150958,
            0.253026799189538, 0.265422870333817, 0.278403150312661,
            0.291995172040202, 0.306227766016838, 0.321131121482591,
            0.336736850452532, 0.353078054770101, 0.370189396320561,
            0.388107170553497, 0.406869383470335, 0.426515832240166,
            0.447088189614875, 0.468630092322638, 0.491187233627272,
            0.514807460249773, 0.539540873857625, 0.565439937337157,
            0.592559586074358, 0.620957344480193, 0.650693448007596,
            0.681830970918936, 0.71443596007499, 0.748577575029184,
            0.784328234724282, 0.821763771102671, 0.860963589956081,
            0.90201083935591, 0.944992586021436, 0.99
        )

left = PWMLED(13)
middle = PWMLED(19)
right = PWMLED(26)

try:
    for level in levels:
        left.value = level
        sleep(0.1)

    for level in reversed(levels):
        left.value = level
        sleep(0.1)

    pause()

except KeyboardInterrupt:
    pass

finally:
    left.close()
    middle.close()
    right.close()