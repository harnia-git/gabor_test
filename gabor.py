import cv2
import matplotlib.pyplot as plt

# sigma
axes=[]
fig=plt.figure()
t = 'ksize=(100,100), theta=0, lambd=10, gamma=0.5, psi=0'
fig.text(0.2, 0.1, t ,wrap=True)
lstSigma = [4,8,12]
for i, sigma in enumerate(lstSigma):
    gabor = cv2.getGaborKernel(ksize=(100,100), sigma=sigma, theta=0, lambd=10, gamma=0.5, psi=0)
    axes.append( fig.add_subplot(1, len(lstSigma), i+1) )
    subplot_title=("sigma="+str(sigma))
    axes[-1].set_title(subplot_title)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(gabor,cmap="gray")
fig.tight_layout()
fig.savefig("image_sigma.png")
plt.show(block=True)
# lambd
axes=[]
fig=plt.figure()
t = 'ksize=(100,100), sigma=8, theta=0, gamma=0.5, psi=0'
fig.text(0.2, 0.1, t ,wrap=True)
lstLambd = [4,8,12]
for i, lambd in enumerate(lstLambd):
    gabor = cv2.getGaborKernel(ksize=(100,100), sigma=8, theta=0, lambd=lambd, gamma=0.5, psi=0)
    axes.append( fig.add_subplot(1, len(lstLambd), i+1) )
    subplot_title=("lambd="+str(lambd))
    axes[-1].set_title(subplot_title)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(gabor,cmap="gray")
fig.tight_layout()
fig.savefig("image_lambd.png")
plt.show(block=True)
# theta
axes=[]
fig=plt.figure()
t = 'ksize=(100,100), sigma=8, lambd=10, gamma=0.5, psi=0'
fig.text(0.2, 0.1, t ,wrap=True)
lstTheta = [0,45,90]
for i, theta in enumerate(lstTheta):
    gabor = cv2.getGaborKernel(ksize=(100,100), sigma=8, theta=numpy.radians(theta), lambd=10, gamma=0.5, psi=0)
    axes.append( fig.add_subplot(1, len(lstTheta), i+1) )
    subplot_title=("theta="+str(theta))
    axes[-1].set_title(subplot_title)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(gabor,cmap="gray")
fig.tight_layout()
fig.savefig("image_theta.png")
plt.show(block=True)
# gamma
axes=[]
fig=plt.figure()
t = 'ksize=(100,100), sigma=8, theta=0, lambd=10, psi=0'
fig.text(0.2, 0.1, t ,wrap=True)
lstGamma = [0.5,0.75,1]
for i, gamma in enumerate(lstGamma):
    gabor = cv2.getGaborKernel(ksize=(100,100), sigma=8, theta=0, lambd=10, gamma=gamma, psi=0)
    axes.append( fig.add_subplot(1, len(lstGamma), i+1) )
    subplot_title=("gamma="+str(gamma))
    axes[-1].set_title(subplot_title)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(gabor,cmap="gray")
fig.tight_layout()
fig.savefig("image_gamma.png")
plt.show(block=True)
# psi
axes=[]
fig=plt.figure()
t = 'ksize=(100,100), sigma=8, theta=0, lambd=10, gamma=0.5'
fig.text(0.2, 0.1, t ,wrap=True)
lstPsi = [0,1,1.5]
for i, psi in enumerate(lstPsi):
    gabor = cv2.getGaborKernel(ksize=(100,100), sigma=8, theta=0, lambd=10, gamma=0.5, psi=psi)
    axes.append( fig.add_subplot(1, len(lstPsi), i+1) )
    subplot_title=("psi="+str(psi))
    axes[-1].set_title(subplot_title)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.imshow(gabor,cmap="gray")
fig.tight_layout()
fig.savefig("image_psi.png")
plt.show(block=True)