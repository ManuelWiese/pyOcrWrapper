from PIL import Image
import pytesseract

from subprocess import Popen, PIPE

import cv2


def tesseract(mat, config=None):
    if config is None:
        text = pytesseract.image_to_string(Image.fromarray(mat))
    else:
        text = pytesseract.image_to_string(Image.fromarray(mat), config=config)

    return text


def gocr(mat, encoding="utf-8"):
    p = Popen(["gocr", "-"], stdin=PIPE, stdout=PIPE)
    retval, buf = cv2.imencode(".pgm", mat)
    # print buf
    p.stdin.write(buf)
    p.stdin.close()
    p.wait()
    text = p.stdout.read()
    p.stdout.close()

    return text.decode(encoding).strip("\n")


def ocrad(mat, encoding="utf-8"):
    p = Popen(["ocrad", "-"], stdin=PIPE, stdout=PIPE)
    retval, buf = cv2.imencode(".pgm", mat)
    # print buf
    p.stdin.write(buf)
    p.stdin.close()
    p.wait()
    text = p.stdout.read()
    p.stdout.close()

    return text.decode(encoding).strip("\n")


if __name__ == '__main__':
    image = cv2.imread("joy_of_data.png", 0)

    print("Original text: \"joy of data\"")
    print("pytesseract:", tesseract(image))
    print("gocr: ", gocr(image))
    print("ocrad: ", ocrad(image))
