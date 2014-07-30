Star Formation
==============

Here are two simple data files with radial velocities and errors for young stars in two different clusters. The challenge is to determine the intrinsic velocity dispersion of the cluster in the presence of these errors and some number of outliers. I can think of at least 3 different ways to do this using stuff from astroML, so it would be great to be able to compare different methods.

To read in the data use the following commands:

```python
import pickle
cl1 = open('cluster1.pkl','rb')
vels1,errs1 = pickle.load(cl1)
```