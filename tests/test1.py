import numpy as np
import nh5
import h5py

# create a sample h5 file
h5_file = h5py.File("sample.h5", "w")
h5_file.create_dataset("dataset1", data=np.array([1, 2, 3]).astype(np.int32))
h5_file.create_dataset("dataset2", data=np.array([4, 5, 6]).astype(np.int32))
h5_file.create_dataset("dataset3", data=np.array([7, 8, 9]).astype(np.int32))

# convert the h5 file to nh5
nh5.h5_to_nh5("sample.h5", "sample.nh5")
