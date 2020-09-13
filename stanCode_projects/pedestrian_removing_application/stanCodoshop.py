"""
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

This file help the user remove unexpected people or abnormal items in a set of pictures
    to get a clean picture of the landscape.
    - 1. Examine every pixel with the same position in each image the user loads.
    - 2. Find the best pixel with the least distance value from the average pixel.
    - 3. Add the best pixel in the new created blank image with the same size as the loaded images.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    # This formula defines color distance value for each pixel.
    color_distance = pow((pow((red - pixel.red), 2) + pow((green - pixel.green), 2) + pow((blue - pixel.blue), 2)),
                         (1/2))
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    # Count the total of the RGB value respectively.
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
    # return the average RGB in the form of a list.
    return [total_red//len(pixels), total_green//len(pixels), total_blue//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    min_dist = 9999999999999999999999999  # Set an initial value for comparing the distance value for each pixel.
    number = 0  # The index of the pixels list.
    for i in range(len(pixels)):
        pixel_dist = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        # Find the minimum distance value and the index of the pixel with that minimum value.
        if pixel_dist < min_dist:
            min_dist = pixel_dist
            number = i
    # Return the pixel with the minimum color distance value as the best pixel.
    return pixels[number]


def get_best_pixel_other_solution(pixels):
    avg = get_average(pixels)
    tuple_lst = []
    for i in range(len(pixels)):
        pixel_dist = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        tuple_lst.append((pixel_dist, pixels[i]))
    best_pair = min(tuple_lst, key=lambda e: e[0])
    return best_pair[1]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            # Get pixels in all images with the same position and make a list as pixel_list.
            pixel_list = []
            for img in range(len(images)):
                pixel_list.append(images[img].get_pixel(x, y))
            best = get_best_pixel(pixel_list)
            # Replace the pixel in blank image by the best pixel on the same position.
            result.get_pixel(x, y).red = best.red
            result.get_pixel(x, y).green = best.green
            result.get_pixel(x, y).blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
