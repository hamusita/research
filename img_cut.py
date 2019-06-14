import os, glob, sys
import argparse
from PIL import Image

def get_args():
    """
    コマンドライン因数を準備する関数
    img_cut.py -h で詳細
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--cd', type = str, dest = 'cd', default = "../data", help = "画像の入力元と出力先があるディレクトリ")
    parser.add_argument('--img_in', type = str, dest = 'img_in', default = "sample", help = "入力画像のディレクトリ")
    parser.add_argument('--img_out', type = str, dest = 'img_out', default = "output", help = "出力画像のディレクトリ")
    parser.add_argument('--img_size', type = int, dest = 'img_size', default = 64, help = "出力画像のサイズ")
    parser.add_argument('--img_interval', type = int, dest = 'img_interval', default = 64, help = "画像の切り出し間隔. img_sizeより小さいと重なって切り出される")
    parser.add_argument('--in_format', type = str, dest = 'in_format', default = "*.png", help = "入力ファイルフォーマット")
    parser.add_argument('--out_format', type = str, dest = 'out_format', default = "png", help = "出力ファイルフォーマット")

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

def cut(path, cd, img_out, img_size, img_interval, out_format):
    for i in path:
        im = Image.open(i)
        w, h = im.size
        print("fin:" + i)
        for j in range(0, h - (h % img_size), img_interval):
            for k in range(0, w - (w % img_size), img_interval):
                im.crop((k, j, k + img_size, j + img_size)).save(os.path.join(cd, img_out, str(int(j / img_interval)) +  "_" + str(int(k / img_interval)) + "." + out_format), quality=95)
                print("---out:" + os.path.join(cd, img_out, str(int(j / img_interval)) +  "_" + str(int(k / img_interval)) + "." + out_format))

if __name__ == '__main__':
    args = get_args()
    check(str(args.cd), str(args.img_in), str(args.img_out))

    path = read_img(str(args.cd), str(args.img_in), str(args.in_format))
    print(path)

    cut(path, str(args.cd), str(args.img_out), int(args.img_size), int(args.img_interval), str(args.out_format))