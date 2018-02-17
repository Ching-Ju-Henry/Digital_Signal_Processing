# -*- coding: utf-8 -*-

import librosa as lib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
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
    D0 = np.zeros((r+1, c+1))
    D0[0, 1:] = np.inf
    D0[1:, 0] = np.inf
    D1 = D0[1:, 1:]

    for i in range(r):
        for j in range(c):
            D1[i, j] = np.sqrt(sum(abs(np.subtract(st1[:,i],st2[:,j]))**2))#np.abs(st1[:,i] - st2[:,j])
    
    for i in range(r):
        for j in range(c):
            D1[i, j] += min(D0[i, j], D0[i, j+1], D0[i+1, j])

    path = traceback(D0)
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

#e1 = np.sqrt(sum(abs(stft1)**2))
#e2 = np.sqrt(sum(abs(stft2)**2))
#e1 = e1.reshape(-1, 1)
#e2 = e2.reshape(1, -1)
#smM = np.dot(abs(stft1).T, abs(stft2))/np.dot(e1, e2)

outcome = []
for test_num in range(40):
    out = []
    m = []
    n = []
    o = []
    s = []
    for train_num in range(40):
        train = '/home/henry/DSP/train_feature/train_%d.npy'%train_num
        test = '/home/henry/DSP/test_feature/test_%d.npy'%test_num
        stft1 = np.load(train)
        stft2 = np.load(test)
        #print stft1.shape
        #print stft2.shape
        p, q, c = dtw(stft1.T, stft2.T)
        if train_num < 10:
            m.append(c*1)
        elif train_num < 20 and train_num >= 10:
            n.append(c*0.1)
        elif train_num < 30 and train_num >= 20:
            o.append(c*0.1)
        elif train_num < 40 and train_num >= 30:
            s.append(c*0.1)
        if train_num == 39:
            c = [(a+b+c+d)/4 for a,b,c,d in zip(m,n,o,s)]#m + n + o + s
            out.extend(c)
            #print out.index(min(out))
    outcome.append(out.index(min(out)))
        
print len(outcome)
print (outcome)

#Accuracy
score = 0
for num in range(len(outcome)):
    if outcome[num] == num/4: 
        score = score + 1
    
print ((score)/40.)
