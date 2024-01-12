import nh5
import h5py

# create a sample h5 file
h5_file = h5py.File("sample.h5", "w")
h5_file.create_dataset("dataset1", data=[1, 2, 3])
h5_file.create_dataset("dataset2", data=[4, 5, 6])
h5_file.create_dataset("dataset3", data=[7, 8, 9])

# convert the h5 file to nh5
nh5.h5_to_nh5("sample.h5", "sample.nh5")
