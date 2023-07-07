import cv2
import numpy as np

# グレースケールの画像ファイルパス
image_path = 'merged_imagecol.png'

# 画像を読み込む
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# カラーマップを適用
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# 修正された画像を保存
output_path = 'colored_image.png'
cv2.imwrite(output_path, colored_image)
