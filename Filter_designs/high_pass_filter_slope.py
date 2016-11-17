__author__ = 'ranga'

import numpy as np
import matplotlib.pyplot as plt
#import cmath as cm
#import pylab as pl


R = 2200
L = 22E-3  # MH
fc = R/(2*np.pi*L)
f = np.arange(1, 10*fc, 1)
w = 2.0*np.pi*f

hp_mr = w/np.sqrt((w*w) + (R*R)/(L*L))

plt.plot(f, 20*np.log10(hp_mr), '-b')
plt.xscale('log')
plt.xlabel('Frequency (log)')
plt.ylabel('Magnitude (dB)')
plt.title('High Pass Filter')
plt.grid(which='both', axis='both')
plt.savefig('high_pass_filter.png')
plt.show()
