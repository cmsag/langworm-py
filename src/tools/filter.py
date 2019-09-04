# Now we need to create a biquad filter node
# The equivalent in Java returns a node with the following properties https://www.javascripture.com/BiquadFilterNode
# detune : AudioParam  readonly
# frequency : AudioParam  readonly
# gain : AudioParam  readonly
# Q : AudioParam  readonly
# type : String
# It has the following method, too:
# getFrequencyResponse(frequencyHz : Float32Array, magResponse : Float32Array, phaseResponse : Float32Array)


# With thanks to arachnoid.com for the explanation of biquadratic filters and how to make them
# https://arachnoid.com/BiQuadDesigner/
# Arachnoid's biquadratic filter in Java was also used heavily for reference:
# https://arachnoid.com/BiQuadDesigner/source_files/BiQuadraticFilter.java
# This is partially an implementation of the recipe here:
# https://web.archive.org/web/20160325025442/http://www.musicdsp.org/files/Audio-EQ-Cookbook.txt
# This implementation by rfabbri was a very useful reference:
# https://gist.github.com/ttm/3851044


import math


# Create a bandpass biquadratic filter - there's no need to use any other type for this program.
class BPBiquadFilter:

    def __init__(self, centre_frequency, sample_rate):

        dBgain = 20
        self.sample_rate = sample_rate
        Q = 0.5

        self.centre_frequency = centre_frequency

        absolute_gain = 10**(dBgain / 40)

        omega = 2 * math.pi * self.centre_frequency/sample_rate

        omega_sn = math.sin(omega)
        omega_cs = math.cos(omega)

        alpha = omega_sn / (2*Q)

        beta = math.sqrt(2*absolute_gain)

        b0 = alpha
        b1 = 0
        b2 = -alpha
        a0 = 1 + alpha
        a1 = -2 * omega_cs
        a2 = 1 - alpha
