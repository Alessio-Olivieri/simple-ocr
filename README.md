# README

## Overview

This Python script performs Optical Character Recognition (OCR) on images copied to the clipboard, extracting text from them using the Tesseract OCR engine. The script utilizes `pytesseract` to interface with Tesseract, and `Pillow`'s `ImageGrab` module to access images from the system clipboard.

## Features

- Captures an image from the clipboard.
- Uses Tesseract OCR to extract text from the image.
- Displays the extracted text in the terminal.
- Handles cases where no image is found in the clipboard.

## Prerequisites

1. **Python 3.x** installed on your machine.
2. **Tesseract-OCR** installed on your system.

   - For Windows, download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
   - For Linux, you can install it using your package manager (e.g., `sudo apt install tesseract-ocr`).
   - For macOS, install it via Homebrew: `brew install tesseract`.

3. **Python Libraries**: Install the required Python libraries by running:
   ```bash
   pip install pytesseract Pillow
   ```

## How to Use

1. Copy an image to your clipboard that contains text.
2. Run the Python script:
   ```bash
   python ocr_clipboard.py
   ```
3. The script will attempt to grab the image from your clipboard and extract text using Tesseract.
4. If successful, the extracted text will be printed in the terminal.

## Error Handling

- If the clipboard does not contain an image, the script will print the message: `No image found in the clipboard.`

## Code Explanation

```python
#!/usr/bin/env python
import pytesseract
from PIL import ImageGrab

# Grab the image from the clipboard
try:
    img = ImageGrab.grabclipboard()

    # Check if the clipboard contains an image
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(img)
    print(text)
except:
    print("No image found in the clipboard.")
```

- The script starts by importing necessary libraries: `pytesseract` for OCR and `ImageGrab` from the `Pillow` library to capture the clipboard image.
- The `ImageGrab.grabclipboard()` function tries to grab an image from the clipboard.
- If an image is found, it runs `pytesseract.image_to_string()` on the image to extract the text and prints the result.
- If no image is found in the clipboard, it will display an error message.

## Notes

- Ensure that Tesseract is correctly installed and accessible via the system’s PATH. You might need to specify the Tesseract path in some cases, like so:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract_executable'
  ```

## License

This script is free to use and distribute under the MIT License. Feel free to modify and adapt it for your needs.
