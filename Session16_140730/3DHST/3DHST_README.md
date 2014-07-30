3DHST
=====

(initial stuff by Erik Tollerud)

Loading the data
----------------

To dowload the data, do this from python (inside this directory):

	>>> import getdata
	>>> getdata.download_data()  
	# will display a message to indicate the download is commencin

Then to load into an ipython notebook, do this:

	>>> import getdata
	>>> tdhst, readme = getdata.load_data()
	>>> print readme  # this will print the readme for your viewing pleasure

Now `tdhst` is an astropy `Table` with the catalogs, and `readme` is a string 
with a description of the columns.

Analysis
--------

At this point, just start playing around with clustering approaches.  A 
great place to look for some of these algorithms is 
[scikit-learn's clustering module](http://scikit-learn.org/stable/modules/clustering.html) 
An example use situation might be:

    >>> from sklearn import cluster
	>>> km = cluster.KMeans(n_clusters=10)
	>>> data = np.array([tdhst['ra'], tdhst['dec']]).T
	>>> km.fit(data)
	>>> labels = km.labels_

Now `labels` indicate which clusters K-means decided apply to each 3D-HST catalog entry
