import h5py
import numpy as np

def reader(filename):
    '''
        reader for the generator. returns image and dict of attributes
    '''
    f = h5py.File(filename)
    #grp = f.create_group('data')
    img = np.array(f['img'])
    md_h = dict(f['attributes'])
    md = dict()
    for key, val in md_h.items():
        md[key] = val.value
    return md, img
