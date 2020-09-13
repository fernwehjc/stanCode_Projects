"""
File: similarity.py
Author: Jade YEH
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    User will given a long sequence DNA and a short sequence DNA.
    Coder will do several partial compare to find the highest similarity between the two give DNA sequences.
    """
    # User give a long sequence
    long_sequence = input('Please give me a DNA sequence to search: ')
    long_sequence = long_sequence.upper()
    # User give a short sequence
    short_sequence = input('What sequence would you like to match? ')
    short_sequence = short_sequence.upper()
    print('The best match is ' + homology(long_sequence, short_sequence))


def homology(long_sequence, short_sequence):
    """
    Cross-compare to find the strand of long sequence with the highest similarity with the short sequence.
    :param long_sequence: str
    :param short_sequence: str
    :return ans: str, the strand of long sequence with the highest similarity with the short sequence
    """
    # number of characters in the long sequence
    i = len(long_sequence)
    # number of characters in the short sequence
    j = len(short_sequence)
    # number of the same element between long- and short- sequence in a certain part of the long sequence
    max_match = 0
    # position where the max_match begins in long sequence
    max_match_point = 0
    ans = ''
    # (i - j +  1) = times needed for cross-comparison
    for k in range(i - j + 1):
        match = 0
        for n in range(j):
            # if find the same element in the same position of long- and short- sequence, count one
            if short_sequence[n] == long_sequence[n+k]:
                match += 1
        # find the biggest match, and the start position(k) in long sequence
        if match > max_match:
            max_match = match
            max_match_point = k
    # the strand of long sequence with the highest similarity with the short sequence
    ans = long_sequence[max_match_point:(max_match_point + j)]
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
