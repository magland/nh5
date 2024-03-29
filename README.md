# nh5

`nh5` is a Python package to support a new file format, .nh5, which stands for "not hdf5". This project aims to simplify and improve the loading of data in web applications, particularly for visualization purposes.

This package has an *very small* codebase. Feel free to explore!

See the [accompanying JavaScript library](https://github.com/magland/nh5/tree/main/js).

## Motivation behind nh5

The creation of this format was driven by specific challenges encountered with the hdf5 format, particularly in the context of web-based applications. While hdf5 is efficient for packaging large volumes of data, including data arrays, it falls short in terms of efficiency and ease when it comes to reading data from a web browser or from remote files. This inefficiency is primarily due to the scattered nature of metadata within the hdf5 file, necessitating multiple HTTP requests for access.

**Simplified Data Access:** Unlike hdf5, where metadata can be dispersed throughout the file, nh5 starts with a straightforward JSON text header. This header contains all the necessary attributes and metadata about the data arrays and can be loaded in one shot by the browser.

**Predefined Data Structure:** While hdf5 allows appending to an existing file, nh5 assumes that data is known in advance and needs to be packaged for visualization in web applications.

## Installation

You can install nh5 using pip

```bash
pip install nh5
```

## Usage

To convert an hdf5 file to an nh5 file, use the h5_to_nh5 function:

```python
from nh5 import h5_to_nh5

h5_to_nh5("path_to_your_hdf5_file.h5", "path_for_the_output_nh5_file.nh5")
```

To convert an nh5 file to an hdf5 file, use the nh5_to_h5 function:

```python
from nh5 import nh5_to_h5

nh5_to_h5("path_to_your_nh5_file.nh5", "path_for_the_output_hdf5_file.h5")
```

## Limitations

- Limited data types: Does not support all hdf5 data types.
- No compression support: Currently, the nh5 format does not support data compression.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing

The code in this project is licensed under Apache License 2.0.

## Author

The package and format were created by Jeremy Magland
