import cv2
import numpy as np

# 連結する画像ファイルのパスリスト
#image_paths = ['image0.jpg', 'image1.jpg', 'image2.jpg']
#image_paths = ['image3.jpg', 'image4.jpg', 'image5.jpg']
image_paths = ['image6.jpg', 'image7.jpg', 'image8.jpg']

# 画像を読み込んでリストに保存
images = []
for path in image_paths:
    image = cv2.imread(path)
    images.append(image)

# 画像のサイズを取得
height = images[0].shape[0]
width = sum(image.shape[1] for image in images)

# 連結された画像用のキャンバスを作成
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# 画像をキャンバス上に連結
x = 0
for image in images:
    w = image.shape[1]
    canvas[:, x:x+w, :] = image
    x += w

# 連結された画像を保存
cv2.imwrite('merged_image3.jpg', canvas)

