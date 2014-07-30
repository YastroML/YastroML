from __future__ import print_function

"""
Gets the 3DHST data for the YastroML hack day

Requires astropy to parse the data files
"""

# I'm not sure if this requires authentication or not...
LATEST_RELEASE_URL = 'http://monoceros.astro.yale.edu/RELEASE_V4.0/Photometry/3dhst_master.phot.v4.1.tar'

def download_data(localfilename=None, url=LATEST_RELEASE_URL):
    import urllib

    if not localfilename:
        localfilename = url.split('/')[-1]

    print('Downloading "{0}" to "{1}"'.format(url, localfilename))
    urllib.urlretrieve(url, localfilename)

    return localfilename

def load_data(fn=LATEST_RELEASE_URL.split('/')[-1]):
    """
    Gets the 3D-HST data and README.

    Parameters
    ----------
    fn : str
        The file to load the 3D-HST data from

    returns
    -------
    data : astropy.table.table
        The 3D-HST data release catalog
    readme : str
        The text of the 3D-HST release's README.  Contains descriptions of the
        table columns

    """
    import tarfile
    from astropy.io import fits
    from astropy.table import Table

    readme = cattab = None
    with tarfile.open(fn) as t:
        for m in t:
            if m.name.endswith('.cat.FITS'):
                #main catalog file
                f = t.extractfile(m)
                try:
                    cs = fits.conf.extension_name_case_sensitive
                    try:
                        fits.conf.extension_name_case_sensitive = False
                        f = fits.HDUList.fromstring(f.read())
                        cattab = Table(f[1].data)
                    finally:
                        fits.conf.extension_name_case_sensitive = cs
                        f.close()
                finally:
                    #not clear of closing is needed, but may as well just in case
                    f.close()
            elif 'readme' in m.name.lower():
                #readme file
                f = t.extractfile(m)
                try:
                    readme = f.read()
                finally:
                    #not clear of closing is needed, but may as well just in case
                    f.close()

    if readme is None:
        raise ValueError('Could not find readme - perhaps not a 3D-HST release tarball?')
    if cattab is None:
        raise ValueError('Could not find catalog FITS file - perhaps not a 3D-HST release tarball?')

    return cattab, readme
