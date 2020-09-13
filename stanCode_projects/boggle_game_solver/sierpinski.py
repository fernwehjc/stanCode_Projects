"""
File: sierpinski.py
Name: Jade YEH
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY = 100          	   # The pause time in miliseconds

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Draw a regular triangle in the middle of the window,
	then draw three regular triangles with half length at three vertices.
	Follow the above pattern and the designated order number to draw certain rounds.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, Indicate how many rounds to draw.
	:param length: int, The side length of the regular triangle.
	:param upper_left_x: int, The x-coordinate for the triangle.
	:param upper_left_y: int, The y-coordinate for the triangle.
	This function does not return anything.
	"""
	if order == 0:
		pass
	else:
		pause(DELAY)
		# Draw a regular triangle.
		triangle_up_edge = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		triangle_left_edge = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		triangle_right_edge = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5,
									upper_left_y + length * 0.866)
		window.add(triangle_up_edge)
		window.add(triangle_left_edge)
		window.add(triangle_right_edge)
		# Draw three triangles on the three vertices of the previous triangle AND Count down the order.
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.5, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.5 * 0.5, upper_left_y + length * 0.866 * 0.5)


if __name__ == '__main__':
	main()