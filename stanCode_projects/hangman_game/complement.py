"""
File: complement.py
Author: Jade YEH
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    User will be requested to give a DNA sequence.
    And coder will provide a complement strand of a DNA sequence.
    """
    # user provide a DNA
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    print('The complement of ' + dna + ' is ' + built_complement(dna))


def built_complement(dna):
    """
    Assign a certain complement element for each nucleotide.
    :param dna: str, user's DNA sequence
    :return ans: str, a complement strand of a DNA sequence
    """
    ans = ''
    # only works for nucleotide in given DNA sequence
    for nucleotide in dna:
        if nucleotide == 'A':
            # assign T as the complement for A
            ans += 'T'
        elif nucleotide == 'T':
            # assign A as the complement for T
            ans += 'A'
        elif nucleotide == 'C':
            # assign G as the complement for C
            ans += 'G'
        else:
            # assign C as the complement for G
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
