import os, glob, sys, cv2, shutil
import argparse

def get_args():
    """
    コマンドライン因数を準備する関数
    img_cut.py -h で詳細
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--cd', type = str, dest = 'cd', default = "../data", help = "画像の入力元と出力先があるディレクトリ")
    parser.add_argument('--img_in', type = str, dest = 'img_in', default = "sample", help = "入力画像のディレクトリ")
    parser.add_argument('--img_out', type = str, dest = 'img_out', default = "hist", help = "出力画像のディレクトリ")
    parser.add_argument('--in_format', type = str, dest = 'in_format', default = "*.png", help = "入力ファイルフォーマット")

    return parser.parse_args()

def check(cd, img_in, img_out):
    print(os.path.join(cd, img_in), os.path.isdir(os.path.join(cd, img_in)))
    if not os.path.isdir(os.path.join(cd, img_in)):
        print("No such input directory")
        sys.exit()
    if not os.path.isdir(os.path.join(cd, img_out)):
        print("make output directory")
        os.makedirs(os.path.join(cd, img_out))
    print("Directory ready")

def read_img(cd, img_in, in_format):
    """
    入力フォーマットに合ったファイルのパスを列挙して返す関数

    """
    path = os.path.join(cd, img_in, in_format)
    img_path = glob.glob(path)

    return img_path

def hist(path, cd, img_out):
    for n, i in enumerate(path):
        im = cv2.imread(i)
        hist = cv2.calcHist([im],[0],None,[256],[0,256])
        w, b = 0, 0
        for i in range(0,10):
            w += hist[i][0]
            b += hist[255 - i][0]
        if b > 4200:
            shutil.move(i, os.path.join(cd, img_out))
            print("---move:" + i + "to" + os.path.join(cd, img_out))

if __name__ == '__main__':
    args = get_args()
    check(str(args.cd), str(args.img_in), str(args.img_out))

    path = read_img(str(args.cd), str(args.img_in), str(args.in_format))
    print(path)

    hist(path, str(args.cd), str(args.img_out))
