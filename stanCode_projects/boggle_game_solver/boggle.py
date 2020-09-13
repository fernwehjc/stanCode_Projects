"""
File: boggle.py
Name: Jade YEH
----------------------------------------
This program recursively finds all the answer(s)
for a 4x4 Alphabets input by user and terminates when the
input is not in the right format and all answers are found.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variable
dictionary_lst = []			# This list will contains all vocabularies in dictionary.txt
answer_lst = []				# This list will contains all answers.


def main():
	"""
	Request user to input 4 rows of letters
	and call a function to find all answers for the 4x4 Alphabets input by user.
	"""
	global answer_lst
	while True:
		# If switch is False, terminate the program.
		switch_on = True
		# Build a list contains all alphabet input by user in order.
		letters_lst = []
		for i in range(4):
			letters = input(f'{i+1} row of letters: ')
			# If the input is not in right format, break the for-loop and turn off the switch.
			if len(letters) != 7 or letters[1] != ' ' or letters[3] != ' ' or letters[5] != ' ':
				print(f'Illegal input')
				switch_on = False
				break
			# Only alphabet will be appended in the letters_lst.
			for j in range(0, 7, 2):
				if letters[j].isalpha():
					letters_lst.append(letters[j].lower())
				else:
					print(f'Illegal input')
					switch_on = False
					break
			if switch_on is False:
				break
		if switch_on is True:
			read_dictionary()
			boggle_ans_finder(letters_lst, list(range(0, 16)), [], answer_lst)
			print(f'There are {len(answer_lst)} words in total.')
			# When all answers are found, terminate the program.
			break
		# When switch is turned off because of the wrong input, terminate the program.
		else:
			break


def boggle_ans_finder(ori_lst, explore_lst, current_lst, ans_lst):
	"""
	Find all string index combination
	and check if the string formed with the found combination is in the dictionary.
	:param ori_lst: list[str], All alphabet input by the user.
	:param explore_lst: list[int], All other index that can be explore according to the current index position.
	:param current_lst: list[int], Current index combination.
	:param ans_lst: list, A list contains all answers.
	This function does not return anything.
	"""
	# Form a string with the current index combination.
	ans_str = ''
	for index in current_lst:
		ans_str += ori_lst[index]
	# If the string is in the dictionary, add the string into answers list.
	if ans_str in dictionary_lst and len(ans_str) >= 4 and ans_str not in ans_lst:
		print(f'Found \"{ans_str}\"')
		ans_lst.append(ans_str)
		# Check if there is any other answer which starts with the ans_str in the dictionary. <line 72-80>
		# If yes, keep explore. <line 72-80>
		prefix_lst = []
		for w in dictionary_lst:
			if w.startswith(ans_str):
				prefix_lst.append(w)
				if len(prefix_lst) > 1:
					break
		if len(prefix_lst) > 1:
			# Read the last index in the current list and assign a certain explore list.
			last_num = current_lst[len(current_lst) - 1]
			boggle_ans_finder_helper(ans_str, ori_lst, define_explore_range(last_num), current_lst, ans_lst)
	else:
		# Found all index combination which can potentially form an answer.
		for num in explore_lst:
			# Do not consider the index out of the range within the letters list.
			if num in current_lst or num < 0 or num > 15:
				pass
			else:
				current_lst.append(num)
				# Define a list containing all affiliated index with the current index for a further exploration.
				explore_lst = define_explore_range(num)
				current_str = ''
				for index in current_lst:
					current_str += ori_lst[index]
				# Check if any word in the dictionary starts with the string form by the current index combination.
				if has_prefix(current_str):
					boggle_ans_finder(ori_lst, explore_lst, current_lst, ans_lst)
				current_lst.pop()


def boggle_ans_finder_helper(ans_str, ori_lst, explore_lst, current_lst, ans_lst):
	"""
	Further explore for a longer answer when an answer had been found.
	:param ans_str: str, The current answer string.
	:param ori_lst: list[str], All alphabet input by the user.
	:param explore_lst: list[int], All other index that can be explore according to the current index position.
	:param current_lst: list[int], Current index combination.
	:param ans_lst: list, A list contains all answers.
	This function does not return anything.
	"""
	if len(current_lst) == len(ans_str) + 1:
		# Form a string with the current index combination.
		ans_str += ori_lst[current_lst[len(current_lst)-1]]
		for word in dictionary_lst:
			# If the string is completely the same with a word in the dictionary, add the string into answers list.
			if ans_str == word and ans_str not in ans_lst:
				print(f'Found \"{ans_str}\"')
				ans_lst.append(ans_str)
				# Check if there is any possibility for a longer answer in the dictionary. <line 118-124>
				# If yes, keep explore. <line 118-124>
				prefix_lst = []
				for w in dictionary_lst:
					if w.startswith(ans_str):
						prefix_lst.append(w)
				if len(prefix_lst) > 1:
					last_num = current_lst[len(current_lst) - 1]
					boggle_ans_finder_helper(ans_str, ori_lst, define_explore_range(last_num), current_lst, ans_lst)
	else:
		# Found all index combination which can potentially form an answer.
		for num in explore_lst:
			# Do not consider the index out of the range within the letters list.
			if num in current_lst or num < 0 or num > 15:
				pass
			else:
				current_lst.append(num)
				# Define a list containing all affiliated index with the current index for a further exploration.
				explore_lst = define_explore_range(num)
				current_str = ''
				for index in current_lst:
					current_str += ori_lst[index]
				# Check if any word in the dictionary starts with the string form by the current index combination.
				if has_prefix(current_str):
					boggle_ans_finder_helper(ans_str, ori_lst, explore_lst, current_lst, ans_lst)
				current_lst.pop()


def define_explore_range(num):
	"""
	Define a list of affiliated index with the current index for the further exploring.
	:param num: int, Current index in the letters list.
	:return: list[int], A list of all affiliated index for the further exploring.
	"""
	if num % 4 == 0:
		explore_lst = [num - 4, num - 3, num + 1, num + 4, num + 5]
	elif num % 4 == 3:
		explore_lst = [num - 5, num - 4, num - 1, num + 3, num + 4]
	else:
		explore_lst = [num - 5, num - 4, num - 3, num - 1, num + 1, num + 3, num + 4, num + 5]
	return explore_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list.
	"""
	global dictionary_lst
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			dictionary_lst.append(word)


def has_prefix(sub_s):
	"""
	Check if any word in the dictionary starts with the current found substring.
	:param sub_s: str, A substring that is constructed by neighboring letters on a 4x4 square grid.
	:return: bool, If there is any words with prefix stored in sub_s.
	"""
	for word in dictionary_lst:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
