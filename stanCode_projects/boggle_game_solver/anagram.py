"""
File: anagram.py
Name: Jade YEH
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
dictionary_lst = []           # This list will contains all vocabularies in dictionary.txt


def main():
    """
    Show message to the user and request a word from the user.
    Then call the functions to find all anagrams for the user's input.
    """
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    while True:
        look_up = input(f'Find anagrams for: ')
        if look_up == EXIT:
            break
        else:
            read_dictionary()
            find_anagrams(look_up)


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


def find_anagrams(s):
    """
    Call a helper function to find all anagrams for the user's input.
    :param s: str, The user's input.
    """
    # Create an index list which will be used to identify each alphabet in the string.
    ori_lst = []
    for i in range(len(s)):
        ori_lst.append(i)
    print(f'Searching...')
    # Receive a answer list with all anagrams.
    answers = find_anagrams_helper(s, ori_lst, [], len(ori_lst), [])
    print(f'{len(answers)} anagrams: {answers}')


def find_anagrams_helper(ori_str, ori_lst, current_ch_lst, len_ori_lst, ans_lst):
    """
    Find permutation of original string index and check if the found combination(string) is in the dictionary.
    :param ori_str: str, The user's input.
    :param ori_lst: list[int], All string index(integer) of the user's input.
    :param current_ch_lst: list[int], Current index combination.
    :param len_ori_lst: int, The length of the original index list.
    :param ans_lst: list[str], A list contains all anagrams.
    :return: list[str], The answers list(ans_lst).
    """
    # Base Case: when the length of current combination equals the length of the original index list
    if len(current_ch_lst) == len_ori_lst:
        ans_str = ''
        # Construct the word with the index combination
        for index in current_ch_lst:
            ans_str += ori_str[index]
        # Check if the ans_str exists in the dictionary AND Avoid the duplicate
        if ans_str in dictionary_lst and ans_str not in ans_lst:
            print(f'Found: {ans_str}')
            print(f'Searching...')
            ans_lst.append(ans_str)
    # Recursive Case: find all index combination
    else:
        for num in ori_lst:
            if num in current_ch_lst:
                pass
            else:
                current_ch_lst.append(num)
                current_str = ''
                for index in current_ch_lst:
                    current_str += ori_str[index]
                # If a word in the dictionary starts with the current found part-string, enter the other helper.
                if has_prefix(current_str):
                    find_anagrams_helper(ori_str, ori_lst, current_ch_lst, len_ori_lst, ans_lst)
                current_ch_lst.pop()
    return ans_lst


def has_prefix(sub_s):
    """
    Check if any word in the dictionary starts with the current found substring.
    :param sub_s: str, A substring that the coder found currently.
    :return: bool, If there is any words with prefix stored in sub_s.
    """
    for word in dictionary_lst:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
