from PIL import Image, ImageDraw
import sys
import random

black = (0, 0, 0)
white = (255, 255, 255)


def main():
    for i in range(int(sys.argv[1])):
        drowEdge(i + 1)


def drowEdge(cnt):
    img = Image.new("RGB", (640, 640), white)
    draw = ImageDraw.Draw(img)
    draw.line((160, 0, 160, 640), fill=black, width=20)
    draw.line((480, 0, 480, 640), fill=black, width=20)

    left, right = CoordinateGen(random.randint(5, 10))
    left.sort(key=lambda x: x[1])
    right.sort(key=lambda x: x[1])
    l, r = len(left), len(right)
    left.append((640, 640))
    right.append((640, 640))

    print(left, right)

    for i in range(l):
        yn = left[i + 1][1]
        x1, y1, x2 = left[i][0], left[i][1], 160
        if abs(x1 - x2) > abs(y1 - yn):
            y = random.randint(min(y1, yn), max(y1, yn))
        else:
            y = random.randint(min(y1, y1 + abs(x1 - x2)),
                               max(y1, y1 + abs(x1 - x2)))
        if y >= 640:
            y = 640
        draw.line((x1, y1, x2, y), fill=black, width=10)
        print(x1, y1, x2, y)
    for i in range(r):
        yn = right[i + 1][1]
        x1, y1, x2 = right[i][0], right[i][1], 480
        if abs(x1 - x2) > abs(y1 - yn):
            y = random.randint(min(y1, yn), max(y1, yn))
        else:
            y = random.randint(min(y1, y1 + abs(x1 - x2)),
                               max(y1, y1 + abs(x1 - x2)))
        if y >= 640:
            y = 640
        print(x1, y1, x2, y)
        draw.line((x1, y1, x2, y), fill=black, width=10)

    img.save("./" + "{:0=5}".format(cnt) + ".jpg", quality=95)


def CoordinateGen(r):
    right, left = [], []
    num = [i for i in range(0, 640, 10)]
    a = random.sample([i for i in num if i <= 80 or (
        i >= 240 and i <= 400) or i >= 560], r)
    b = random.sample(num, r)
    for i, j in zip(a, b):
        if i < 320:
            left.append((i, j))
        else:
            right.append((i, j))
    return left, right


if __name__ == '__main__':
    main()
