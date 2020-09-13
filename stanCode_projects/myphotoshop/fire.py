"""
File: fire.py
Author: Jade Yeh
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


# Control the degree of the R-value to be highlighted
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: SimpleImage, the original image
    :return: SimpleImage, fire is highlighted in the original image
    """
    # create a new image entirely the same as the original image ready to be highlighted
    img = SimpleImage(filename)
    # for all pixels in new image
    for pixel in img:
        # average of RGB-value in a pixel
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        # check if that pixel represent the fire user wished to be highlighted
        if pixel.red > avg * HURDLE_FACTOR:
            # replace the pixel with pure red color
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # for all the rest, grey-scaled the pixel
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    # return the highlighted image
    return img


def main():
    """
    User import a fire image.
    Coder will highlight the fire with red color in the image and turn other parts grey.
    """
    # Import a fire image
    original_fire = SimpleImage('images/greenland-fire.png')
    # Show the original fire image
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    # Show the highlighted fire image
    highlighted_fire.show()


if __name__ == '__main__':
    main()
