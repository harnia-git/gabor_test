import cv2
import numpy as np

# グレースケールのJPG画像ファイルパス
image_path = 'merged_imagecol.jpg'

# グレースケール画像を読み込む
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 4チャンネルの透過度付き画像に変換する
height, width = image.shape[:2]
image_with_alpha = np.zeros((height, width, 4), dtype=np.uint8)
image_with_alpha[:, :, 0] = image
image_with_alpha[:, :, 1] = image
image_with_alpha[:, :, 2] = image
image_with_alpha[:, :, 3] = 128  # 透過度を設定（0は完全透明、255は完全不透明）

# すべての画素の透過度を50%にする
#image_with_alpha[:, :, 3] = 128  # 透過度を設定（0は完全透明、255は完全不透明）

# PNG画像として保存する
output_path = 'merged_imagecol.png'
cv2.imwrite(output_path, image_with_alpha)


# # 薄桃色のRGB値
# tint_color = (255, 218, 185)

# # 色の変換
# #colored_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # グレースケールからBGRへ変換
# colored_image = np.where(image_with_alpha < 200, image_with_alpha + np.array(tint_color, dtype=np.uint8), 255)  # しきい値以下の値に薄桃色を加算

# # 修正された画像を保存
# output_path = 'colored_image_alpha.png'
# cv2.imwrite(output_path, colored_image)
