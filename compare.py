import sys
from PIL import Image, ImageChops


def cmp():
    """Compares two photos and shows their differences
       It will also save the result in a file
    """

    img1 = Image.open(sys.argv[1])
    img2 = Image.open(sys.argv[2])

    diff = ImageChops.difference(img1, img2)

    diff.show()
    diff.save('result.jpg')


if __name__ == "__main__":
    cmp()
