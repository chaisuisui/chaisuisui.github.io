import os
import cv2
import numpy as np

os.makedirs("video", exist_ok=True)

# 视频参数
width, height = 640, 480
fps = 24
duration = 2  # 秒

for i in range(1, 13):
    filename = f"video/video{i}.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    # 随机颜色
    color = np.random.randint(0, 255, size=3)

    for _ in range(fps * duration):
        frame = np.full((height, width, 3), color, dtype=np.uint8)
        out.write(frame)

    out.release()
    print(f"生成 {filename}")

print("全部完成")
