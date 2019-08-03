#!/usr/bin/env python3
'''text read'''

from PIL import Image
import pytesseract

path='a2.png'
text = pytesseract.image_to_string(Image.open(path),lang='chi_sim')
print(text)