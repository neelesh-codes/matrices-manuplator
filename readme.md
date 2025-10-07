# Matrices Manipulator

A user-friendly GUI application for performing various operations on NumPy arrays and .npy files.

## Features

- **Array Operations**: Add, subtract, multiply, divide, and transpose arrays
- **File Operations**: Load, save, and copy .npy files
- **Quick Create**: Generate special arrays (zeros, ones, identity, random, linspace)
- **Array Information**: View detailed statistics about arrays
- **Text-to-Speech**: Optional voice feedback for operations

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/neelesh-codes/matrices-manipulator.git
cd matrices-manipulator
```

2. **Install required packages:**
```bash
pip install numpy pyttsx3
```

3. **Run the application:**
```bash
python main.py
```

## Usage Guide

### 1. Array Operations Tab

This tab allows you to perform mathematical operations on arrays.

**Input Format:**
- Arrays should be entered in Python list format
- Example: `[[1, 2, 3], [4, 5, 6]]`

**Available Operations:**
- **Add Arrays**: Element-wise addition of two arrays
- **Subtract Arrays**: Element-wise subtraction
- **Multiply Arrays**: Matrix multiplication (Array1 @ Array2)
- **Divide Arrays**: Element-wise division
- **Transpose Array 1**: Transpose the first array
- **Array 1 Info**: Display detailed information about the array

**Example Usage:**
1. Enter Array 1: `[[1, 2], [3, 4]]`
2. Enter Array 2: `[[5, 6], [7, 8]]`
3. Click "Add Arrays" to see the result

### 2. File Operations Tab

Manage .npy files with ease.

**Load .npy File:**
1. Click "Browse" to select a file
2. Click "Load & Display" to view the data
3. Click "Show Info" to see detailed statistics

**Save Array to .npy File:**
1. Enter array data in the format: `[[1, 2, 3], [4, 5, 6]]`
2. Click "Browse Location" to choose where to save
3. Click "Save" to create the file

**Copy .npy File:**
1. Select source file using the first "Browse" button
2. Select destination using the second "Browse" button
3. Click "Copy File" to duplicate the file

### 3. Quick Create Tab

Generate common array types quickly.

**Available Array Types:**

- **Zeros Array**: Create an array filled with zeros
  - Format: `3, 3` (rows, columns)

- **Ones Array**: Create an array filled with ones
  - Format: `3, 3` (rows, columns)

- **Identity Matrix**: Create an identity matrix
  - Format: `3` (size)

- **Random Array**: Create an array with random values
  - Format: `3, 3` (rows, columns)

- **Linspace Array**: Create evenly spaced values
  - Start: Starting value (e.g., `0`)
  - Stop: Ending value (e.g., `10`)
  - Num: Number of values (e.g., `11`)

**Note**: Created arrays are automatically loaded into Array 1 for further operations.

## Code Structure

```
matrices-manipulator/
├── main.py                 # GUI application
├── __init__.py            # Package initialization
├── README.md              # Documentation
└── utils/
    ├── __init__.py        # Utils package init
    ├── util1.py           # Array manipulation class
    └── util2.py           # File operations class
```

## Classes and Methods

### `Numpy_array_manipulator` (util1.py)

**Methods:**
- `basic_info(arr, speak_also=False)`: Display array information
- `multiply_two_arrays(array_1, array_2, speak_also=False)`: Matrix multiplication
- `add_two_arrays(array_1, array_2, speak_also=False)`: Array addition
- `subtract_two_arrays(array_1, array_2, speak_also=False)`: Array subtraction
- `divide_two_arrays(array_1, array_2, speak_also=False)`: Array division
- `transpose_the_array(array_to_transpose, speak_also=False)`: Array transpose

### `NPY_file_changer` (util2.py)

**Methods:**
- `load_npy_file(npy_file_path)`: Load a .npy file
- `copy_npy_file(src, dest)`: Copy a .npy file
- `basic_info_of_file(npy_file_path, speak_also=False)`: Display file information
- `move_to_npy(data, file_path)`: Save array to .npy file

## Text-to-Speech Feature

The `speak_also` parameter in various methods enables voice feedback. This feature uses the `pyttsx3` library and is available when using the classes programmatically.

**Example:**
```python
from utils.util1 import Numpy_array_manipulator
import numpy as np

manipulator = Numpy_array_manipulator()
arr = np.array([[1, 2], [3, 4]])
manipulator.basic_info(arr, speak_also=True)
```

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'pyttsx3'"**
- Solution: `pip install pyttsx3`

**"ModuleNotFoundError: No module named 'numpy'"**
- Solution: `pip install numpy`

**Text-to-speech not working**
- Ensure your system has speech synthesis capabilities
- On Windows, SAPI5 should be available by default
- On Linux, install `espeak`: `sudo apt-get install espeak`
- On macOS, speech synthesis is built-in

**Invalid array format error**
- Ensure arrays are in proper Python list format
- Use nested lists for 2D arrays: `[[1, 2], [3, 4]]`
- Use single lists for 1D arrays: `[1, 2, 3, 4]`

## Examples

### Example 1: Matrix Multiplication
```python
Array 1: [[1, 2, 3], [4, 5, 6]]
Array 2: [[7, 8], [9, 10], [11, 12]]
Result: [[58, 64], [139, 154]]
```

### Example 2: Array Transpose
```python
Array 1: [[1, 2, 3], [4, 5, 6]]
Result: [[1, 4], [2, 5], [3, 6]]
```

### Example 3: Create Identity Matrix
```python
Size: 3
Result:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**Neelesh**
- GitHub: [@neelesh-codes](https://github.com/neelesh-codes)

## Changelog

### Version 2.0
- Added comprehensive GUI using Tkinter
- Fixed typos in class and method names
- Improved error handling
- Added Quick Create tab for generating arrays
- Enhanced file operations interface
- Added detailed output logging

### Version 1.0
- Initial release
- Basic array operations
- File handling capabilities
- Text-to-speech integration

## Roadmap

Future features planned:
- [ ] Advanced matrix operations (determinant, inverse, eigenvalues)
- [ ] Data visualization with matplotlib
- [ ] Export to different formats (CSV, Excel)
- [ ] Batch processing of multiple files
- [ ] Custom themes for GUI
- [ ] Operation history and undo functionality

## Support

If you encounter any issues or have questions, please:
1. Check the Troubleshooting section
2. Open an issue on GitHub
3. Contact the developer

---

**Enjoy using Matrices Manipulator!** 🎉