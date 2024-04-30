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