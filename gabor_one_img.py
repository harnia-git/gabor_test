# ksize	ガボールフィルタのサイズ(n,n)
# sigma	ガウシアン包絡線の標準偏差
# theta	ガボール関数の平行縞に対する法線の向き
# lambd	正弦波因子の波長
# gamma	空間アスペクト比
# psi	位相オフセット
# ktype	フィルタ係数の種類．CV_32F または CV_64F
import cv2
import numpy as np
import matplotlib.pyplot as plt
t = 'ksize=(100,100), theta=0, lambd=10, gamma=0.5, psi=0'
lstSigma = [4,8,12]
theta=[0,45,90]
sigma=lstSigma[1]
lambd=[4,8,12]
gamma=[0.5,0.75,1]
psi=[0,1,1.5]

gabor = cv2.getGaborKernel(ksize=(100,100), sigma=sigma, theta=90, lambd=10, gamma=0.5, psi=0)

# 画像のサイズをリサイズ
resized_gabor = cv2.resize(gabor, (200, 200))

# 画像を0-255の範囲に正規化
normalized_gabor = cv2.normalize(resized_gabor, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# 画像を保存
cv2.imwrite('imageone1.jpg', normalized_gabor)
