
import sys
import numpy as np
from PIL import Image
from torchvision import transforms
sys.path.append("..")
from code.common.ContVar import *

'''
https://www.cnblogs.com/ghgxj/p/14219097.html
'''
file_path = PROJECT_PATH + '\\sample\\face\\face1.png'
print(file_path)
img = Image.open(file_path)
transform = transforms.Grayscale()
img = transform(img)
Image._show(img)