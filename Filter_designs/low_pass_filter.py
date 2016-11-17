__author__ = 'ranga'



import numpy as np
import matplotlib.pyplot as plt
#import cmath as cm
#import pylab as pl


R = 2200
C = 47E-9  # nF
fc = 1.0/(2*np.pi*R*C)
f = np.arange(1, 10*fc, 1)
w = 2.0*np.pi*f

# To find slope
f_lower = 1000
f_upper = 10000

lp_mr = 1/np.sqrt((w*R*C)*(w*R*C) + 1)

plt.plot(f, 20*np.log10(lp_mr), '-r')
plt.xscale('log')
plt.xlabel('Frequency (log)')
plt.ylabel('Magnitude (dB)')
plt.title('Low Pass Filter')
plt.grid(which='both', axis='both')
plt.savefig('low_pass_filter.png')
plt.show()

