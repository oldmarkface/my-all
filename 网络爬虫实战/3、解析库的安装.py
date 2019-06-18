import lxml

from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>Mark</p>','lxml')
print(soup.p.string)

import pyquery

import locale
locale.setlocale(locale.LC_ALL,'C')

import tesserocr
from PIL import Image
image = Image.open('image.png')
print(tesserocr.image_to_text(image))
