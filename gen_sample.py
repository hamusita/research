from PIL import Image, ImageDraw, ImageFont
import numpy as np


def main():
    drowLine()

def drowLine():
    img = Image.new("RGB", (640, 640), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.line((160, img.height, 480, img.height), fill=(255, 255, 255), width=20)
    img.show()

if __name__ == '__main__':
    main()
