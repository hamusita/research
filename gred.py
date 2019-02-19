from PIL import Image, ImageDraw
import random

black = (0, 0, 0)
red = (255, 0, 0)


def main():
    for i in range(100):
        gred(i)


def gred(cnt):
    filename = "/Users/hamusita/Dropbox/research/under/test_arange_" + str(cnt) +".png"
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    for i in range(64,512,64):
        draw.line((i, 0, i, 640), fill=red, width=1)
        draw.line((0, i, 640, i), fill=red, width=1)
    img.save("./sample/" + "{:0=5}".format(cnt) + ".jpg", quality=95)

if __name__ == '__main__':
    main()
