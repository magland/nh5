import os
import numpy as np
import nh5
import h5py


def main():
    if os.path.exists("sample.h5"):
        os.remove("sample.h5")
    if os.path.exists("sample.nh5"):
        os.remove("sample.nh5")
    if os.path.exists("sample2.h5"):
        os.remove("sample2.h5")

    # create a sample h5 file
    with h5py.File("sample.h5", "w") as h5_file:
        h5_file.create_dataset("dataset1", data=np.array([[1, 2, 3], [4, 5, 6]]).astype(np.int32))
        h5_file.create_dataset("dataset2", data=np.array([4, 5, 6]).astype(np.int32))
        h5_file.create_dataset("folder1/dataset3", data=np.array([7, 8, 9]).astype(np.int32))
        group = h5_file.create_group("folder2")
        group.attrs["attr1"] = "value1"
        group.attrs["attr2"] = 2

    # convert the h5 file to nh5
    nh5.h5_to_nh5("sample.h5", "sample.nh5")
    # convert back to h5
    nh5.nh5_to_h5("sample.nh5", "sample2.h5")

    # check to see if the files are the same
    h5_file = h5py.File("sample.h5", "r")
    h5_file2 = h5py.File("sample2.h5", "r")

    def visit_func(x):
        a = h5_file[x]
        b = h5_file2[x]
        for attr_name, attr_value in a.attrs.items():
            if b.attrs.get(attr_name) != attr_value:
                raise ValueError(f"Attribute mismatch: {attr_name}")
        for attr_name, attr_value in b.attrs.items():
            if a.attrs.get(attr_name) != attr_value:
                raise ValueError(f"Attribute mismatch: {attr_name}")
        if isinstance(a, h5py.Group):
            print(f"Group: {x}")
        else:
            print(f"Dataset: {x}")
            array1 = a[()]
            array2 = b[()]
            if not np.array_equal(array1, array2):
                raise ValueError(f"Array mismatch: {x}")
    h5_file.visit(visit_func)

    print("Success!")


if __name__ == "__main__":
    main()
