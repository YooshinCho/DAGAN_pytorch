import numpy as np
from PIL import Image
import os

imagedir = 'carplate_v1'
Images = np.zeros([8,50,28,28,3], dtype = np.float32)
for subdir in os.listdir(imagedir):
    cnt = 0
    for filename in os.listdir(os.path.join(imagedir, subdir)):
        im = Image.open(os.path.join(imagedir, subdir, filename))
        im_ = np.array(im.resize((28,28)), dtype=np.float32)
        im_ = im_ / 255.
        Images[int(subdir),cnt] = im_
        cnt += 1
    print(cnt, int(subdir))


np.save('carplate_v1.npy', Images)

