"""
File: blur.py
Author: Jade Yeh
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


# Controls the times for blurring import image
BLUR_TIMES = 5


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the original image is blurred
    """
    # create a new, blank image with the same size as the original image which is ready to be blurred
    new_img = SimpleImage.blank(img.width, img.height)
    # (x, y) represent every pixel in the original image
    for x in range(img.width):
        for y in range(img.height):
            # get pixel at (x, y) in original image
            p_old = img.get_pixel(x, y)
            # get pixel at (x, y) in new, blank image
            p_new = new_img.get_pixel(x, y)
            # for the left edge
            if x == 0:
                # for the pixel at top-left point
                if y == 0:
                    # p_old_'no.' represent pixels at all adjacent points to (x, y)
                    p_old_1 = img.get_pixel(x, y + 1)
                    p_old_2 = img.get_pixel(x + 1, y)
                    p_old_3 = img.get_pixel(x + 1, y + 1)
                    # replace R-value at (x, y) with the average R-value of all adjacent points, including (x, y)
                    p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red) // 4
                    # replace G-value at (x, y) with the average G-value of all adjacent points, including (x, y)
                    p_new.green = (p_old.green + p_old_1.green + p_old_2.green + p_old_3.green) // 4
                    # replace B-value at (x, y) with the average B-value of all adjacent points, including (x, y)
                    p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue + p_old_3.blue) // 4
                # for the pixel at bottom-left point
                elif y == img.height-1:
                    p_old_1 = img.get_pixel(x, y - 1)
                    p_old_2 = img.get_pixel(x + 1, y - 1)
                    p_old_3 = img.get_pixel(x + 1, y)
                    p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red) // 4
                    p_new.green = (p_old.green + p_old_1.green + p_old_2.green + p_old_3.green) // 4
                    p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue + p_old_3.blue) // 4
                # for the pixels at left edge except for two extremes
                else:
                    p_old_1 = img.get_pixel(x, y - 1)
                    p_old_2 = img.get_pixel(x, y + 1)
                    p_old_3 = img.get_pixel(x + 1, y - 1)
                    p_old_4 = img.get_pixel(x + 1, y)
                    p_old_5 = img.get_pixel(x + 1, y + 1)
                    p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red + p_old_4.red + p_old_5.red) // 6
                    p_new.green = (p_old.green + p_old_1.green + p_old_2.green
                                   + p_old_3.green + p_old_4.green + p_old_5.green) // 6
                    p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue
                                   + p_old_3.blue + p_old_4.blue + p_old_5.blue) // 6
            # for the right edge
            elif x == img.width-1:
                # for the pixel at top-right point
                if y == 0:
                    p_old_1 = img.get_pixel(x - 1, y)
                    p_old_2 = img.get_pixel(x - 1, y + 1)
                    p_old_3 = img.get_pixel(x, y + 1)
                    p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red) // 4
                    p_new.green = (p_old.green + p_old_1.green + p_old_2.green + p_old_3.green) // 4
                    p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue + p_old_3.blue) // 4
                # for the pixel at bottom-right point
                elif y == img.height-1:
                    p_old_1 = img.get_pixel(x - 1, y - 1)
                    p_old_2 = img.get_pixel(x - 1, y)
                    p_old_3 = img.get_pixel(x, y - 1)
                    p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red) // 4
                    p_new.green = (p_old.green + p_old_1.green + p_old_2.green + p_old_3.green) // 4
                    p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue + p_old_3.blue) // 4
                # for the pixels at right edge except for two extremes
                else:
                    p_old_1 = img.get_pixel(x - 1, y - 1)
                    p_old_2 = img.get_pixel(x - 1, y)
                    p_old_3 = img.get_pixel(x - 1, y + 1)
                    p_old_4 = img.get_pixel(x, y - 1)
                    p_old_5 = img.get_pixel(x, y + 1)
                    p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red + p_old_4.red + p_old_5.red) // 6
                    p_new.green = (p_old.green + p_old_1.green + p_old_2.green
                                   + p_old_3.green + p_old_4.green + p_old_5.green) // 6
                    p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue
                                  + p_old_3.blue + p_old_4.blue + p_old_5.blue) // 6
            # for the pixels at top edge except for two extremes
            elif y == 0:
                p_old_1 = img.get_pixel(x - 1, y)
                p_old_2 = img.get_pixel(x - 1, y + 1)
                p_old_3 = img.get_pixel(x, y + 1)
                p_old_4 = img.get_pixel(x + 1, y)
                p_old_5 = img.get_pixel(x + 1, y + 1)
                p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red + p_old_4.red + p_old_5.red) // 6
                p_new.green = (p_old.green + p_old_1.green + p_old_2.green
                               + p_old_3.green + p_old_4.green + p_old_5.green) // 6
                p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue
                              + p_old_3.blue + p_old_4.blue + p_old_5.blue) // 6
            # for the pixels at bottom edge except for two extremes
            elif y == img.height - 1:
                p_old_1 = img.get_pixel(x - 1, y - 1)
                p_old_2 = img.get_pixel(x - 1, y)
                p_old_3 = img.get_pixel(x, y - 1)
                p_old_4 = img.get_pixel(x + 1, y - 1)
                p_old_5 = img.get_pixel(x + 1, y)
                p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red + p_old_4.red + p_old_5.red) // 6
                p_new.green = (p_old.green + p_old_1.green + p_old_2.green
                               + p_old_3.green + p_old_4.green + p_old_5.green) // 6
                p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue
                              + p_old_3.blue + p_old_4.blue + p_old_5.blue) // 6
            # for all pixels not on the edge of the image
            else:
                p_old_1 = img.get_pixel(x - 1, y - 1)
                p_old_2 = img.get_pixel(x - 1, y)
                p_old_3 = img.get_pixel(x - 1, y + 1)
                p_old_4 = img.get_pixel(x, y - 1)
                p_old_5 = img.get_pixel(x, y + 1)
                p_old_6 = img.get_pixel(x + 1, y - 1)
                p_old_7 = img.get_pixel(x + 1, y)
                p_old_8 = img.get_pixel(x + 1, y + 1)
                p_new.red = (p_old.red + p_old_1.red + p_old_2.red + p_old_3.red + p_old_4.red
                             + p_old_5.red + p_old_6.red + p_old_7.red + p_old_8.red) // 9
                p_new.green = (p_old.green + p_old_1.green + p_old_2.green + p_old_3.green + p_old_4.green
                               + p_old_5.green + p_old_6.green + p_old_7.green + p_old_8.green) // 9
                p_new.blue = (p_old.blue + p_old_1.blue + p_old_2.blue + p_old_3.blue + p_old_4.blue
                              + p_old_5.blue + p_old_6.blue + p_old_7.blue + p_old_8.blue) // 9
    # return the blurred image
    return new_img


def main():
    """
    User import a image.
    Coder will blur the image for certain times the user request.
    """
    # Import a image ready to be blurred
    old_img = SimpleImage("images/smiley-face.png")
    # Show the original image
    old_img.show()

    # Blur the original for one time
    blurred_img = blur(old_img)
    # Keep to blur the blurred image till the total times that user wished to blur the image are completed
    for i in range(BLUR_TIMES - 1):
        blurred_img = blur(blurred_img)
    # Show the final blurred image
    blurred_img.show()


if __name__ == '__main__':
    main()
