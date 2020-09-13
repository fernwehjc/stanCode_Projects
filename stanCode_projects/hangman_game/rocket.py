"""
File: rocket.py
Author: Jade YEH
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# Controls the size of the rocket
SIZE = 3


def main():
	"""
	Built up a rocket of designated size by combining 6 part of work.
	"""
	head()
	belt()
	upper_body()
	lower_body()
	belt()
	head()


def head():
	"""
	Build the head with three elements: ' ', '/', and '\'
	"""
	# (i,j) represent every single space in the head
	for i in range(SIZE):
		for j in range(SIZE * 2 + 2):
			# left-half side
			if j <= SIZE:
				if j >= SIZE - i:
					print('/', end='')
				else:
					print(' ', end='')
			# right-half side
			elif j <= SIZE + i + 1:
				if j >= SIZE + 1:
					print('\\', end='')
			else:
				print(' ', end='')
		print('')


def belt():
	"""
	Built the belt with two elements: '+' and '='
	"""
	# (i,j) represent every single space in the belt
	for j in range(SIZE * 2 + 2):
		# left edge
		if j == 0:
			print('+', end='')
		# middle
		elif j <= (SIZE * 2):
			if j > 0:
				print('=', end='')
		# right edge
		else:
			print('+', end='')
	print('')


def upper_body():
	"""
	Built the upper body with four elements: '|', '.', '/', and '\'
	"""
	# (i,j) represent every single space in the upper body
	for i in range(SIZE):
		for j in range(SIZE * 2 + 2):
			# left edge
			if j == 0:
				print('|', end='')
			# right edge
			elif j == SIZE * 2 + 1:
				print('|', end='')
			# upper-left small triangle area
			elif i + j < SIZE:
				print('.', end='')
			# upper-right small triangle area
			elif j > SIZE + i + 1:
				if j <= SIZE * 2:
					print('.', end='')
			# middle big triangle area
			else:
				if is_odd(i + j) == is_odd(SIZE):
					print('/', end='')
				else:
					print('\\', end='')
		print('')


def lower_body():
	"""
	Built the upper body with four elements: '|', '.', '/', and '\'
	"""
	# (i,j) represent every single space in the upper body
	for i in range(SIZE):
		for j in range(SIZE * 2 + 2):
			# left edge
			if j == 0:
				print('|', end='')
			# right edge
			elif j == SIZE * 2 + 1:
				print('|', end='')
			# lower-left small triangle area
			elif i >= j:
				if j < SIZE:
					print('.', end='')
			# lower-right small triangle area
			elif j > SIZE * 2 - i:
				print('.', end='')
			# middle big triangle area
			else:
				if is_odd(SIZE):
					# drawing pattern for odd size rocket
					if is_odd(i + j) == is_odd(SIZE):
						print('\\', end='')
					else:
						print('/', end='')
				else:
					# drawing pattern for even size rocket
					if is_odd(i + j) == is_odd(SIZE):
						print('/', end='')
					else:
						print('\\', end='')
		print('')


def is_odd(n):
	"""
	Determine whether n is odd.
	:parameter n: int, n > 0
	:return: bool, if it's odd
	"""
	return n % 2 != 0


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()