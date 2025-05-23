from PIL import Image
import os

# ขนาดเป้าหมาย
sizes = [
    (1280, 1280),
    (1440, 1440)
    # (1280, 720),
    # (854, 480),
    # (640, 360),
    # (320, 240),
    # (160, 120),
    # (100, 100)
]

# โหลดภาพต้นฉบับ
image_path = "img/input_10.jpeg"  # รองรับ .png, .jpg, .jpeg
img = Image.open(image_path)

for w, h in sizes:
    img_copy = img.copy()
    img_copy.thumbnail((w, h))

    # ✅ แปลงเป็น RGB ก่อน save เป็น .jpg
    rgb_img = img_copy.convert("RGB")

    filename = f"resized_{w}x{h}.jpg"
    rgb_img.save(filename)

print("✅ บันทึกเสร็จแล้วทุกขนาด!")
