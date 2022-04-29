from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im_RGB = Image.open('./images/image001.jpg')
im_RGB_array = np.array(im_RGB)

plt.figure()
plt.imshow(im_RGB)

im_gray_obj = im_RGB.convert("L")
im_gray = np.array(im_RGB.convert("L"))

plt.figure()
plt.imshow(im_gray,'gray')
plt.title('GRAYSCALE')