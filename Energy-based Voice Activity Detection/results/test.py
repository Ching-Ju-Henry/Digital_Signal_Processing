import wave
import matplotlib.pyplot as plt
import numpy as np
import sys

new = []
for i in range(10):
    name = 'file%d.wav'%i

    #read signal
    filename = wave.open(name, 'r')
    signal = filename.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    new.extend(signal)

    #plot figure
    plt.figure(i)
    plt.title(name)
    plt.plot(signal)

plt.figure(10)
plt.title('all')
plt.plot(new)
plt.show()


