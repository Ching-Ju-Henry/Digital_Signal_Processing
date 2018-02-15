# -*- coding: utf-8 -*-

import librosa as lib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

#==============================================================================
# Calculate the STFT feature for both sounds 
#==============================================================================
#----------------------------load sound S1, S2--------------------------------#
filename1 = '/home/henry/DSP/lab3/sm1_cln.wav'
s1, sr1 = lib.load(filename1)
filename2 = '/home/henry/DSP/lab3/sm2_cln.wav'
s2, sr2 = lib.load(filename2)
print s2.shape
stft1 = lib.stft(s1, n_fft = 512, hop_length = 256)
stft2 = lib.stft(s2, n_fft = 512, hop_length = 256)
print stft1.shape
#==============================================================================
# Dynamic Time Wrapping  s1, s2
#==============================================================================
# Write a function of DTW that return p, q and accumulated cost matrix(D)
# def dtw(s1,s2):
#    
#     return p, q, D
def traceback(D):
    i, j = np.array(D.shape) - 2
    p, q = [i], [j]
    while ((i > 0) or (j > 0)):
        tb = np.argmin((D[i, j], D[i, j+1], D[i+1, j]))
        if (tb == 0):
            i -= 1
            j -= 1
        elif (tb == 1):
            i -= 1
        else: # (tb == 2):
            j -= 1
        p.insert(0, i)
        q.insert(0, j)
    return np.array(p), np.array(q)

def dtw(st1, st2):
    r, c = len(st1.T), len(st2.T)
    print r, c
    D0 = np.zeros((r+1, c+1))
    D0[0, 1:] = np.inf
    D0[1:, 0] = np.inf
    D1 = D0[1:, 1:]

    for i in range(r):
        for j in range(c):
            print st1[:,i].shape
            print st2[:,j].shape
            D1[i, j] = np.sqrt(sum(abs(np.subtract(st1[:,i],st2[:,j]))**2))#np.abs(st1[:,i] - st2[:,j])
    
    for i in range(r):
        for j in range(c):
            D1[i, j] += min(D0[i, j], D0[i, j+1], D0[i+1, j])

    path = traceback(D0)
    print D1.shape
    return path[0], path[1], D1[r-1,c-1]


#==============================================================================
# spectrogram : find the distance matrix to get the distribution of data
#==============================================================================

# e1 = energy matrix of sound 1
# e2 = energy matrix of sound 2
# smM = distance matrix
# p, q, c = dtw(s1,s2) call your function here
# plt.figure(figsize = (10,10))
# plot smM


e1 = np.sqrt(sum(abs(stft1)**2))
e2 = np.sqrt(sum(abs(stft2)**2))
e1 = e1.reshape(-1, 1)
e2 = e2.reshape(1, -1)
smM = np.dot(abs(stft1).T, abs(stft2))/np.dot(e1, e2)

p, q, c = dtw(stft1, stft2)
print (c)

plt.figure(figsize = (10,10))
plt.imshow(smM.T, cmap = cm.gray, origin = 'low', interpolation = 'nearest')
plt.xlim([-0.5, smM.shape[0]-0.5])
plt.ylim([-0.5, smM.shape[1]-0.5])
plt.plot(p, q, 'ro')


#==============================================================================
# Time signal
#==============================================================================
fig = plt.figure(figsize=(16, 8))

# Plot x_1 --> ax1
axis1 = np.arange(len(s1))/float(sr1)
a1 = plt.subplot(211)
plt.plot(axis1, s1)

# Plot x_2 --> ax2
axis2 = np.arange(len(s2))/float(sr2)
a2 = plt.subplot(212)
plt.plot(axis2, s2)

# Plot coord1 and coord2 on ax1 and ax2
transFigure = fig.transFigure.inverted()
for num in range(len(p)):
    if (num%10)==0:
        coord1 = transFigure.transform(a1.transData.transform([p[num]*256./sr1,0]))
        coord2 = transFigure.transform(a2.transData.transform([q[num]*256./sr2,0]))
        line = matplotlib.lines.Line2D((coord1[0],coord2[0]),
                                       (coord1[1],coord2[1]),
                                       transform=fig.transFigure,
                                       color = 'r')
        fig.lines.append(line)



plt.show()
