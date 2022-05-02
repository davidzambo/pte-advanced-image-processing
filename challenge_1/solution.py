from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open('./images/image001.jpg')

image_array = np.array(image)
image_width = len(image_array[0])
one_third_of_width = image_width // 3

middle_bottle_cap = image_array[:60, one_third_of_width:one_third_of_width * 2, :]

plt.figure()
plt.imshow(middle_bottle_cap)

u = np.arange(0,3,1)+np.arange(0,9,2)[:,np.newaxis]


# image_grayscale_obj = image.convert("L")
# image_grayscale = np.array(image_grayscale_obj)

# plt.figure()
# plt.imshow(image_grayscale,'gray')
# plt.title('GRAYSCALE')