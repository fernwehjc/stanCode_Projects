"""
File: green_screen.py
Author: Jade Yeh
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the green screen figure image
    :return: SimpleImage, the green screen pixels are replaced with pixels of background image
    """
    # (x, y) represent every pixel in the figure image
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            # get pixel at (x, y) in figure image
            pixel_fg = figure_img.get_pixel(x, y)
            # find the maximum value between R-value and B-value at (x, y)
            bigger = max(pixel_fg.red, pixel_fg.blue)
            # check whether pixel at (x, y) is green screen
            if pixel_fg.green > bigger * 2:
                # get pixel at (x, y) in background image
                pixel_bg = background_img.get_pixel(x, y)
                # replace figure image's R-value at (x, y) with background image's R-value at (x, y)
                pixel_fg.red = pixel_bg.red
                # replace figure image's G-value at (x, y) with background image's G-value at (x, y)
                pixel_fg.green = pixel_bg.green
                # replace figure image's B-value at (x, y) with background image's B-value at (x, y)
                pixel_fg.blue = pixel_bg.blue
    # return the combined image
    return figure_img


def main():
    """
    User import a background image and a figure image in the green screen.
    Coder will show combined image by replacing the green screen pixel with pixels of background image.
    """
    # Import background image
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    # Import figure image in the green screen
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    # Show the combined image
    result.show()


if __name__ == '__main__':
    main()
