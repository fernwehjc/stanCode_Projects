"""
File: quadratic_solver.py
Name: Jade Yeh
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	User give 3 inputs (a, b, and c) for a quadratic equation: ax^2 + bx + c = 0.
	Coder will find the solutions of x for that quadratic equation.
	"""
	print('stanCode Quadratic Solver!')
	# ax^2 + bx + c = 0
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	# this value determine the number of root
	discriminant = b * b - 4 * a * c
	if discriminant >= 0:
		# >= 0 -> roots: x1 and x2
		x1 = (-b + math.sqrt(discriminant)) / 2 / a
		x2 = (-b - math.sqrt(discriminant)) / 2 / a
		if x1 != x2:
			# > 0 -> two roots: x1 and x2
			print('Two roots: ' + str(x1) + '  , ' + str(x2))
		else:
			#  = 0 -> one root: x1 = x2
			print('One root: ' + str(x1))
	else:
		# < 0 -> no real root
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
