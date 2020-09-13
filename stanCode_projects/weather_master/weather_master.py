"""
File: weather_master.py
Name: Jade Yeh
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop to give a result
EXIT = -100


def main():
	"""
	When User request a result after inputting a number of temperature data,
	the coder will give a result about:
		1. Highest temperature
		2. Lowest temperature
		3. Average temperature
		4. Number of cold days(temperature below 16)
	"""
	print("stanCode \"Weather Master 4.0\"!")
	# 1st input
	t1 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	# highest temperature
	maximum = t1
	# lowest temperature
	minimum = t1
	# t = the sum of all input temperature
	t = t1
	# d = the number of days recorded
	d = 1
	# the average temperature during the recording period
	average = t / d
	# c = the number of cold days
	if t1 < 16:
		c = 1
	else:
		c = 0
	# check whether User request for a result
	if t1 == EXIT:
		print('No temperatures were entered.')
	else:
		while True:
			# new input
			t2 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			# check whether User request for a result
			if t2 == EXIT:
				break
			else:
				maximum = find_max(maximum, t2)
				minimum = find_min(minimum, t2)
				t += t2
				d += 1
				average = t / d
				if t2 < 16:
					c += 1
		print('Highest Temperature = ' + str(maximum))
		print('Lowest Temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(c) + ' cold day(s)')


def find_max(maximum, t2):
	"""
	Find the maximum.
	ans = find_max(10, 9) = 10
	ans = find_max(1, 7) = 7
	ans = find_max(3, 3) = 3
	"""
	if maximum < t2:
		return t2
	return maximum


def find_min(minimum, t2):
	"""
	Find the minimum.
	ans = find_min(10, 9) = 9
	ans = find_min(1, 7) = 1
	ans = find_min(3, 3) = 3
	"""
	if minimum > t2:
		return t2
	return minimum


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
