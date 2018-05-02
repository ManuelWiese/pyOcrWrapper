from PIL import Image
import pytesseract
import uuid
import os

from subprocess import Popen, PIPE, call

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

    p.stdin.write(buf)
    p.stdin.close()
    p.wait()
    text = p.stdout.read()
    p.stdout.close()

    return text.decode(encoding).strip("\n")


def ocrad(mat, encoding="utf-8"):
    p = Popen(["ocrad", "-"], stdin=PIPE, stdout=PIPE)
    retval, buf = cv2.imencode(".pgm", mat)

    p.stdin.write(buf)
    p.stdin.close()
    p.wait()
    text = p.stdout.read()
    p.stdout.close()

    return text.decode(encoding).strip("\n")

def cuneiform(mat):
    file_prefix = str(uuid.uuid4())
    image_path = "/tmp/" + file_prefix + ".png"
    data_path = "/tmp/" + file_prefix + ".txt"

    cv2.imwrite(image_path, mat)

    FNULL = open(os.devnull, 'w')
    call(["cuneiform", image_path, "-o", data_path], stdout=FNULL)

    with open(data_path) as file_handler:
        value = file_handler.read()

    os.remove(image_path)
    os.remove(data_path)

    return value.strip("\n")


if __name__ == '__main__':
    from time import time

    image = cv2.imread("joy_of_data.png", 0)
    print("Original text: \"joy of data\"")

    number_of_runs = 10
    pre = time()
    for i in range(number_of_runs):
        result = tesseract(image)
    print("pytesseract: {}, took {}s for {} runs".format(result, time() - pre, number_of_runs))

    pre = time()
    for i in range(number_of_runs):
        result = gocr(image)
    print("gocr: {}, took {}s for {} runs".format(result, time() - pre, number_of_runs))

    pre = time()
    for i in range(number_of_runs):
        result = ocrad(image)
    print("ocrad: {}, took {}s for {} runs".format(result, time() - pre, number_of_runs))

    pre = time()
    for i in range(number_of_runs):
        result = cuneiform(image)
    print("cuneiform: {}, took {}s for {} runs".format(result, time() - pre, number_of_runs))
