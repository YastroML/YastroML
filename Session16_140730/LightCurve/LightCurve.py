import numpy as np 
import matplotlib.pyplot as plt 

#index 0 holds time in Julian Date, index 1 holds R band magnitude
lightcurve=np.loadtxt("LightCurve.txt", use_cols(1,2), unpack=True)

#a quick way to visualize the data w matplotlib
plt.plot(lightcurve[0],lightcurve[1],'ro')
plt.gca().invert_yaxis #magnitudes are backwards
plt.show()