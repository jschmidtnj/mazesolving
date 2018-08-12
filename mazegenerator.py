from daedalus import Maze
# https://github.com/wroberts/pydaedalus
from PIL import Image
# Read command line arguments - the python argparse class is convenient here.
import argparse
import os


def blackWhiteReversal(im):
    whitecolor = 255
    blackcolor = 0
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            #print(pixels[i, j])
            if pixels[i, j] == whitecolor:
                pixels[i, j] = blackcolor
            else:
                pixels[i, j] = whitecolor
    crop_width = im.size[0]
    crop_height = im.size[1]
    if im.size[0] % 2 == 0:
        crop_width -= 1
        #print(crop_width)
    if im.size[1] % 2 == 0:
        crop_height -= 1
        #print(crop_height)
    #print(crop_width, crop_height)
    croppedimg = im.crop((0, 0, crop_width, crop_height))
    return croppedimg


def generatemaze(width, height, output_file, generate_bmp):
    maze = Maze(width, height)
    maze.create_perfect()
    maze.create_perfect()
    maze.save_bitmap(output_file + '.bmp')
    img = Image.open(output_file + '.bmp')
    blackWhiteReversal(img).save(output_file + '.png', 'png')
    print("generated maze")
    if not generate_bmp:
        os.remove(output_file + '.bmp')


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("width")
    parser.add_argument("height")
    parser.add_argument("output_file")
    parser.add_argument("generate_bmp", nargs='?', default='no')
    args = parser.parse_args()
    generate_bmp_bool = str2bool(args.generate_bmp)
    width = 0
    height = 0
    try:
        width = int(args.width)
    except:
        raise argparse.ArgumentTypeError('Width must be an integer.')
    try:
        height = int(args.height)
    except:
        raise argparse.ArgumentTypeError('Height must be an integer.')
    #print(width, height, args.output_file, generate_bmp_bool)
    generatemaze(width, height, args.output_file, generate_bmp_bool)


if __name__ == "__main__":
    main()
