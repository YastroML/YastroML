import numpy as np 
import matplotlib.pyplot as plt 
from astropy.io import ascii

#index 0 holds time in Julian Date, index 1 holds R band magnitude

lightcurve = ascii.read("LightCurve.txt")

#a quick way to visualize the data w matplotlib
plt.plot(lightcurve['jd'],lightcurve['mag'],'ro')
plt.gca().invert_yaxis #magnitudes are backwards
plt.show()
