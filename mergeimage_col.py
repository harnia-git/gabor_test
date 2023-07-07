import cv2
import numpy as np

# 連結する画像ファイルのパスリスト
image_paths = ['merged_image2.jpg', 'merged_image3.jpg', 'merged_image2.jpg']

# 画像を読み込んでリストに保存
images = []
for path in image_paths:
    image = cv2.imread(path)
    images.append(image)

# 画像のサイズを取得
width = images[0].shape[1]
height = sum(image.shape[0] for image in images)


# 連結された画像用のキャンバスを作成
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# 画像をキャンバス上に連結
y = 0
for image in images:
    h = image.shape[0]
    canvas[y:y+h,: ,:] = image
    y += h

# 連結された画像を保存
cv2.imwrite('merged_imagecol.jpg', canvas)

