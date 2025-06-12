import wave
import struct
import math

def create_ambient(filename, freq=110, duration_ms=3000, volume=0.3, sample_rate=44100):
    n_samples = int(sample_rate * duration_ms / 1000)
    wav_file = wave.open(filename, "w")
    wav_file.setparams((1, 2, sample_rate, n_samples, "NONE", "not compressed"))

    for i in range(n_samples):
        wave_value = volume * math.sin(2 * math.pi * freq * i / sample_rate)
        wav_file.writeframes(struct.pack("h", int(wave_value * 32767.0)))

    wav_file.close()

create_ambient("ambient_cave.wav")
print("✅ Created 'ambient_cave.wav'")