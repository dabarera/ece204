__author__ = 'ranga'



import numpy as np
import matplotlib.pyplot as plt
import itertools
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

lp_lower = 20*np.log10( 1/np.sqrt((2*np.pi*f_lower*R*C)**2 + 1 ))
lp_upper = 20*np.log10( 1/np.sqrt((2*np.pi*f_upper*R*C)**2 + 1 ))
slope = lp_upper - lp_lower

lp_mr = 1/np.sqrt((w*R*C)*(w*R*C) + 1)

plt.plot(f, 20*np.log10(lp_mr), '-r',linewidth=2.5)

# Plot slope lines
# horizonal
plt.plot([1,f_lower],[lp_lower, lp_lower],'b--',linewidth=1.5)
plt.plot([1,f_upper],[lp_upper, lp_upper],'g--',linewidth=1.5)
#vertical
plt.plot([f_lower,f_lower],[-20, lp_lower],'b-.',linewidth=1.5)
plt.plot([f_upper,f_upper],[-20, lp_upper],'g-.',linewidth=1.5)
plt.text(10, -10, 'Slope :' + str(np.round(slope,2)) + ' dB/decade')
plt.xscale('log')
plt.xlabel('Frequency (log)')
plt.ylabel('Magnitude (dB)')
plt.title('Low Pass Filter')
plt.grid(which='both', axis='both')
plt.savefig('low_pass_filter.png')
plt.show()

