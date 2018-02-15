import pyaudio
import wave

CHUNCK = 1024
Audio_path = 'file300.wav'
wf = wave.open(Audio_path, 'rb')

p = pyaudio.PyAudio()
stream= p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNCK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNCK)

stream.stop_stream()
stream.close()
p.terminate()
