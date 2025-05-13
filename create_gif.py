import imageio.v3 as iio

filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

'''import imageio.v3 as iio
from PIL import Image
import numpy as np

# List of your image file paths
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']

# Open the first image to get target size
first_img = Image.open(filenames[0])
target_size = first_img.size  # (width, height)

images = []

for filename in filenames:
    img = Image.open(filename).convert("RGB")  # Ensure RGB format
    img = img.resize(target_size)  # Resize to match first image
    images.append(np.array(img))  # Convert to array for imageio

# Save as GIF
iio.imwrite("team.gif", images, duration=500, loop=0)'''
