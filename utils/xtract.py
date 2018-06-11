import h5py

f = h5py.File('ourtest.hdf5', 'r')
print(f['/data'][0,0,0,0])
