import urllib.request
import os

os.makedirs("garden", exist_ok=True)

urls = [
    "https://picsum.photos/1024/1024?random=1",
    "https://picsum.photos/1024/1024?random=2",
    "https://picsum.photos/1024/1024?random=3",
    "https://picsum.photos/1024/1024?random=4"
]

for i, url in enumerate(urls, start=1):
    filename = f"garden/garden{i}.jpg"
    urllib.request.urlretrieve(url, filename)
    print("保存:", filename)

print("完成")
