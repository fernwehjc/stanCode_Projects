"""
File: mirror_lake.py
Author: Jade Yeh
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: SimpleImage, the original image
    :return:
    """
    # The original image
    img = SimpleImage(filename)
    # Create a new, blank image with the same width and two times height as the original image
    img_blank = SimpleImage.blank(img.width, img.height * 2)
    # (x, y) represent every pixel in the original image
    for x in range(img.width):
        for y in range(img.height):
            # get pixel at (x, y) in original image
            p_old = img.get_pixel(x, y)
            # get pixel at (x, y) in new, blank image
            p1 = img_blank.get_pixel(x, y)
            # get pixel at symmetrical point of (x, y) in new, blank image
            p2 = img_blank.get_pixel(x, img_blank.height - 1 - y)
            #  below 6 lines: copy the pixel in the original image for the new, blank image
            p1.red = p_old.red
            p1.green = p_old.green
            p1.blue = p_old.blue
            p2.red = p_old.red
            p2.green = p_old.green
            p2.blue = p_old.blue
    # return the vertically mirrored image
    return img_blank


def main():
    """
    User import a image.
    Coder will create an mirror image in the vertical direction.
    """
    # Import a image
    original_mt = SimpleImage('images/mt-rainier.jpg')
    # Show the original image
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    # Show the vertically mirrored image
    reflected.show()


if __name__ == '__main__':
    main()
