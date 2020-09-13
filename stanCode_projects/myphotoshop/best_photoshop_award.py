"""
File: best_photoshop_award.py
Author: Jade Yeh
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.07
# Controls the upper bound for black pixel
BLACK_PIXEL = 227


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
            # average of RGB-value in pixel at (x, y)
            avg = (pixel_fg.red + pixel_fg.green + pixel_fg.blue) // 3
            # total RGB-value in pixel at (x, y)
            total = pixel_fg.red + pixel_fg.green + pixel_fg.blue
            # check whether pixel at (x, y) is green screen
            if pixel_fg.green > avg * THRESHOLD and total > BLACK_PIXEL:
                # get pixel at (x, y) in background image
                pixel_bg = background_img.get_pixel(x, y)
                # replace figure image's R-value at (x, y) with background image's R-value at (x, y)
                pixel_fg.red = pixel_bg.red
                # replace figure image's G-value at (x, y) with background image's G-value at (x, y)
                pixel_fg.green = pixel_bg.green
                # # replace figure image's B-value at (x, y) with background image's B-value at (x, y)
                pixel_fg.blue = pixel_bg.blue
    # return the combined image
    return figure_img


def main():
    """
    User import a background image and a figure image in the green screen.
    Coder will show combined image by replacing the green screen pixel with pixels of background image.
    """
    # Import background image
    background = SimpleImage('image_contest/ArtPark.jpg')
    # Import figure image in the green screen
    figure = SimpleImage('image_contest/Jade.jpg')
    result = combine(background, figure)
    # Show the combined image
    result.show()


if __name__ == '__main__':
    main()
