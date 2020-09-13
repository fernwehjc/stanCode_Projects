"""
File: shrink.py
Author: Jade Yeh
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: SimpleImage, the original image
    :return img: SimpleImage, every four pixels in original image are condensed in a corresponding pixel of new image
    """
    # The original image
    old_img = SimpleImage(filename)
    # Create a new, blank image with half width and half height as the original image
    new_img = SimpleImage.blank(old_img.width // 2, old_img.height // 2)
    # (x, y) represent every pixel in the new image
    for x in range(new_img.width):
        for y in range(new_img.height):
            # get pixel at (x, y) in new, blank image
            p_new = new_img.get_pixel(x, y)
            # p_old_'no.' represent pixels all corresponding to (x, y) for the proportional scaling
            p_old_1 = old_img.get_pixel(2 * x, 2 * y)
            p_old_2 = old_img.get_pixel(2 * x, 2 * y + 1)
            p_old_3 = old_img.get_pixel(2 * x + 1, 2 * y)
            p_old_4 = old_img.get_pixel(2 * x + 1, 2 * y + 1)
            # replace R-value at (x, y) with the average R-value of all corresponding points
            p_new.red = (p_old_1.red + p_old_2.red + p_old_3.red + p_old_4.red) // 4
            # replace G-value at (x, y) with the average G-value of all corresponding points
            p_new.green = (p_old_1.green + p_old_2.green + p_old_3.green + p_old_4.green) // 4
            # replace B-value at (x, y) with the average B-value of all corresponding points
            p_new.blue = (p_old_1.blue + p_old_2.blue + p_old_3.blue + p_old_4.blue) // 4
    # return the shrink image
    return new_img


def main():
    """
    User import a image.
    Coder will proportional scale the original image to a new image with half size.
    """
    # Import a image
    original = SimpleImage("images/poppy.png")
    # Show the original image
    original.show()
    after_shrink = shrink("images/poppy.png")
    # Show the shrink image
    after_shrink.show()


if __name__ == '__main__':
    main()
