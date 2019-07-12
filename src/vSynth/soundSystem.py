
block_length = 512
block_time = 1
started = False
sound_on = False


class SoundSystem:

    def __init__(self, sample_rate):
        # Defined elsewhere, sample_rate should be passed to the class upon instantiation
        self.sample_rate = sample_rate

        self.block_time = block_length / self.sample_rate

    def start_sound(self, duration):
        # default = create 2 seconds of noise
        duration = 2
        white_noise = self.create_white_noise_node(duration * self.sample_rate)

        # Now we need to create a biquad filter node
        # The equivalent in Java returns a node with the following properties https://www.javascripture.com/BiquadFilterNode
        # detune : AudioParam  readonly
        # frequency : AudioParam  readonly
        # gain : AudioParam  readonly
        # Q : AudioParam  readonly
        # type : String
        # It has the following method, too:
        # getFrequencyResponse(frequencyHz : Float32Array, magResponse : Float32Array, phaseResponse : Float32Array)

        # https://webaudio.github.io/web-audio-api/#biquadfilternode

        # https://webaudio.github.io/web-audio-api/#audionode

        # https://arachnoid.com/BiQuadDesigner/

    # ...
    # Function WiP
    # ...

    def create_white_noise_node(self):
        pass

    # ...
    # Function WiP
    # ...
