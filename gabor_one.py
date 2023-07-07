import cv2
import numpy as np
import matplotlib.pyplot as plt
t = 'ksize=(100,100), theta=0, lambd=10, gamma=0.5, psi=0'
lstSigma = [4,8,12]
sigma=lstSigma[1]
gabor = cv2.getGaborKernel(ksize=(100,100), sigma=sigma, theta=0, lambd=10, gamma=0.5, psi=0)

fig=plt.figure()
plt.axis('off')
plt.imshow(gabor,cmap="gray")
print(gabor.shape)
fig.savefig("image_sigma8.png")
# 画像表示
#scale_factor=255.0/2.0
img2 = np.int16(gabor)     # convert to signed 16 bit integer to allow overflow
img2 = 255.0*gabor  # apply scale factor
print(np.amin(img2))
print(np.amax(img2))
img2 = np.clip(img2, 0, 255) # force all values to be between 0 and 255

# after clip img2 is effectively unsigned 8 bit, but make it explicit:
img2 = np.uint8(img2)
cv2.imshow(img2)
