import wave
import matplotlib.pyplot as plt
import numpy as np

#read signal
filename = wave.open('sample_audio.wav', 'r')
signal = filename.readframes(-1)
signal = np.fromstring(signal, 'Int16')

#parameter
n = 1500
tmp = 0
vol = []
signal_abs = []

#abs signal and shift signal to mean = 0
for num in range(len(signal)):
    signal_abs.append(abs(signal[num]-np.mean(signal)))

#calculate energy
for ind in range(len(signal_abs)):
    tmp = 0
    if (ind + n < 159744):
        tmp = sum(signal_abs[ind:ind+n])
    vol.append(tmp)

#find mask to find start and end
ind_tmp = np.zeros(len(vol))
for z in range(len(vol)):
    if vol[z]>=500000 and z >1000: #601500
        ind_tmp[z]=1

#find start and end
b = []
a = []
for n in range(len(ind_tmp)):
    if ind_tmp[n]==1 and ind_tmp[n-1] ==0:
        b.append(n)
    if ind_tmp[n]==1 and ind_tmp[n+1] ==0:
        a.append(n)        

#plot figure
axis1 = np.arange(len(signal))/16000.0
axis2 = np.arange(len(vol))/16000.0

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(axis1,signal)

plt.figure(2)
plt.title('energy')
plt.axhline(y=500000, c ='r')  #601500
plt.plot(axis2,vol)

plt.figure(3)
plt.title('mask')
plt.plot(axis2,ind_tmp)

plt.figure(4)
plt.title('Signal Wave with line')
plt.plot(axis1,signal)
for n_a in range(len(a)):
    plt.axvline(x = a[n_a]/16000.0, c = 'b', linewidth = 0.5)
for n_b in range(len(b)):
    plt.axvline(x = b[n_b]/16000.0, c = 'r', linewidth = 0.5)
plt.show()



