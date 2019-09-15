# https://people.csail.mit.edu/hubert/pyaudio/docs/#pyaudio.Stream.__init__

# https://stackoverflow.com/questions/24920346/filtering-a-wav-file-using-python

from pyaudio import PyAudio, paFloat32
import numpy as np
from scipy import signal
from scipy.signal import butter, lfilter
import random
import math

class BPBiquadFilter:

    def __init__(self, centre_frequency, sample_rate):

        dBgain = 20
        # Q = Quality factor
        Q = 0.5
        self.sample_rate = sample_rate
        self.centre_frequency = centre_frequency

        absolute_gain = 10**(dBgain / 40)

        omega = 2 * math.pi * self.centre_frequency/sample_rate

        omega_sn = math.sin(omega)
        omega_cs = math.cos(omega)

        alpha = omega_sn / (2*Q)

        beta = math.sqrt(2*absolute_gain)

        self.b0 = alpha
        self.b1 = 0
        self.b2 = -alpha
        self.a0 = 1 + alpha
        self.a1 = -2 * omega_cs
        self.a2 = 1 - alpha

bp = BPBiquadFilter(centre_frequency=300,sample_rate=44100)

# samples = np.array([bp.b0,bp.b1,bp.b2,bp.a0,bp.a1,bp.a2])

volume = 0.2
samples = (np.sin(2*np.pi*np.arange(44100*1)*440/44100)).astype(np.float32)
print(type(samples))

pa = PyAudio()
my_stream = pa.open(format=paFloat32,
                    # the 3 arguments from createWhiteNoiseNode in pinktrombone
                    channels=1,
                    frames_per_buffer=8,
                    rate=44100,
                    # End of pinktrombone args
                    output=True)

while True:
    my_stream.write(volume*samples)

my_stream.stop_stream()
my_stream.close()

pa.terminate()
