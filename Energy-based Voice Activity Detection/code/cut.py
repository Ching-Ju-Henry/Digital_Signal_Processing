import pyaudio
import wave
import numpy as np

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000
CHUNK = 1024
RECORD_SECONDS = 10


p = pyaudio.PyAudio()
num = np.load('SE.npy')
print (num[0])
print (len(num))


#read signal
filename = wave.open('file300.wav', 'r')
signal = filename.readframes(-1)
signal = np.fromstring(signal, 'Int16')

frames = []
for vo in range(len(num)):
   for bit in range(num[vo][0], num[vo][1]):
       frames.append(signal[bit])
   WAVE_OUTPUT_FILENAME = "file%d.wav"%vo
   waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
   waveFile.setnchannels(CHANNELS)
   waveFile.setsampwidth(p.get_sample_size(FORMAT))
   waveFile.setframerate(RATE)
   waveFile.writeframes(b''.join(frames))
   waveFile.close()
   frames = []

