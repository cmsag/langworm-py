# SOURCE: https://stackoverflow.com/questions/12093594/how-to-implement-band-pass-butterworth-filter-with-scipy-signal-butter/12233959#12233959

from pyaudio import PyAudio, paFloat32
from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
from pyaudio import PyAudio


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

fs = 500.0
lowcut = 250.0
highcut = 1250.0

volume = 0.2
samples = (np.sin(2*np.pi*np.arange(44100*1)*440/44100)).astype(np.float32)


def get_sample(frequency):
    return (np.sin(2 * np.pi * np.arange(frequency * 1) * (frequency/10) / frequency)).astype(np.float32)


pa = PyAudio()
current_rate = 44100
my_stream = pa.open(format=paFloat32,
                    # the 3 arguments from createWhiteNoiseNode in pinktrombone
                    channels=1,
                    frames_per_buffer=8,
                    rate=current_rate,
                    # End of pinktrombone args
                    output=True)

filtered_samples = butter_bandpass_filter(samples,fs,lowcut,highcut)

while True:
    #samples = get_sample(random.randint(0, 44100))
    my_stream.write(volume*samples)

my_stream.stop_stream()
my_stream.close()

pa.terminate()