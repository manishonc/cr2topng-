Here is a comprehensive GitHub README file for the script `cr2topng-compressed.py`. This README provides an overview, prerequisites, installation steps, usage instructions, and troubleshooting tips.

### GitHub README

---

# CR2 to Compressed PNG Converter

This Python script converts CR2 files to highly compressed PNG files using multithreading for faster processing. It resizes images before compression to ensure they are manageable for `pngquant`, and only saves the compressed PNG files in the output directory.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

This script is designed to convert Canon RAW (CR2) files to compressed PNG images. The conversion and compression processes are optimized for performance and quality:
- Uses `rawpy` and `Pillow` for image conversion.
- Leverages `pngquant` for high-quality compression.
- Implements multithreading to process multiple files simultaneously.
- Resizes images to a maximum width of 1920 pixels to reduce file size before compression.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3
- `Pillow` for image processing
- `rawpy` for handling CR2 files
- `pngquant` for PNG compression

## Installation

### Install Dependencies

1. **Install Python packages:**
    ```bash
    pip install pillow rawpy
    ```

2. **Install `pngquant`:**
    ```bash
    # Using Homebrew on macOS
    brew install pngquant
    ```

### Clone the Repository

```bash
git clone https://github.com/your-username/cr2-to-compressed-png.git
cd cr2-to-compressed-png
```

## Usage

1. **Set Your Source and Output Directories:**
    Modify the `source_directory` and `output_directory` variables in the script to point to your source and output folders.

2. **Run the Script:**
    ```bash
    python3 cr2topng-compressed.py
    ```

### Example

Modify the script with your directories:
```python
source_directory = '/path/to/your/100CANON'
output_directory = '/path/to/your/output'
```

Run the script:
```bash
python3 cr2topng-compressed.py
```

## Options

- **Multithreading:** The script uses up to 5 threads for concurrent processing. Adjust the `max_workers` parameter in the script to change the number of concurrent processes.
- **Image Resizing:** The script resizes images to a maximum width of 1920 pixels. Modify the `max_width` variable in the script to change this value.

## Troubleshooting

### Common Errors

- **`File is too large for pngquant processing`**:
  Resize the image or increase the allowable file size for `pngquant`.

- **`module 'PIL.Image' has no attribute 'ANTIALIAS'`**:
  Use `Image.LANCZOS` instead of `Image.ANTIALIAS` for high-quality downsampling.

- **`Error processing [filename]: pngquant failed`**:
  Check the stderr output for specific issues, such as unsupported file formats or corrupted data.

### Log and Debug

The script prints conversion and compression status messages to the console. Review these messages to diagnose issues with specific files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the instructions, paths, and any other specifics to better fit your project and repository. Replace `https://github.com/your-username/cr2-to-compressed-png.git` with your actual GitHub repository URL and update any other details as necessary.
