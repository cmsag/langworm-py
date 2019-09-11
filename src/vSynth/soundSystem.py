from pyaudio import PyAudio, paFloat32
import random
import src.tools.filter as fl

block_length = 512
block_time = 1
started = False
sound_on = False

# Default sample rate just above 44 KHz
default_sr = 44100


class SoundSystem:

    def __init__(self, sample_rate):
        # Defined elsewhere, sample_rate should be passed to the class upon instantiation
        self.sample_rate = sample_rate

        self.block_time = block_length / self.sample_rate

        self.create_white_noise_node(2)

    def start_sound(self, *duration):
        # default = create 2 seconds of noise
        if duration is None:
            duration = 2

        white_noise = self.create_white_noise_node(duration * self.sample_rate)

        aspirate_filter = fl.BPBiquadFilter(centre_frequency=500,
                                            sample_rate=default_sr)

        fricative_filter = fl.BPBiquadFilter(centre_frequency=1000,
                                             sample_rate=default_sr)

        # ...
        # Function WiP
        # ...

    def create_white_noise_node(self, frame_count):
        # Using a PortAudio stream via pyaudio to replace the web audiocontext createBuffer function.
        # https://people.csail.mit.edu/hubert/pyaudio/docs/#class-stream
        # Not sure if it will work...
        # May be input or output. Putting output for now.
        input_node = PyAudio()
        my_stream = input_node.open(format=paFloat32,
                                    input=True,
                                    channels=1,
                                    frames_per_buffer=frame_count,
                                    rate=self.sample_rate)

        now_buffering = my_stream.read(1)
        i = 0
        while i < frame_count:
            i += 1
            now_buffering[i] = random.randint(0,44100)

        # AudioBufferSourceNode.buffer
        # An AudioBuffer that defines the audio asset to be played, or when set to the value null,
        # defines a single channel of silence (in which every sample is 0.0).

        # var source = this.audioContext.createBufferSource();
        # source.buffer = myArrayBuffer;
        # source.loop = true;

        source = PyAudio().open(output=True,
                                )
        source.input_host_api_specific_stream_info = my_stream

        return source
        # For this we need to get the equivalent of an audio buffer source node
        # https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode

        # ...
        # Function WiP
        # ...

test = SoundSystem(default_sr)