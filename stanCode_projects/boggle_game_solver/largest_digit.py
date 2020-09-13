"""
File: largest_digit.py
Name: Jade YEH
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, A number that the user want to look up for its biggest digit.
	:return: int, The largest digit found in a certain number.
	"""
	# Remove the minus sign.
	if n < 0:
		n = -n
	return find_largest_digit_helper(0, n)


def find_largest_digit_helper(max_digit, current):
	"""
	This function will help the user find the largest digit in a certain number
	by continuously dividing 10 to get every digit within the number.
	:param max_digit: int, An initial value for comparison.
	:param current: int, Each digit found in a certain number.
	:return: int, The largest digit found in a certain number after checking all digits within the number.
	"""
	if current == 0:
		# Return the largest digit after all digits has been cross-compared.
		return max_digit
	else:
		# Get each digit.
		digit = current % 10
		# Compare the obtained digit with the current max_digit.
		if digit > max_digit:
			max_digit = digit
		# Delete the last digit for the next round of comparison
		current = current // 10
		return find_largest_digit_helper(max_digit, current)


if __name__ == '__main__':
	main()
