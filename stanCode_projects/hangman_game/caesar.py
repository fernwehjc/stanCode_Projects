"""
File: caesar.py
Auhtor: Jade YEH
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Re-construct the ALPHABET with the secret number offered by user.
    And encrypt the garbled message for the user to get the meaningful message.
    """
    # user's secret number
    secret = int(input('Secret number: '))
    # construct new alphabet system with the secret number
    new_alphabet == new_alphabet(secret)
    # user's garbled message
    code = input('What\'s the ciphered string? ')
    code = code.upper()
    print('The deciphered string is: ' + de_code(secret, code))


def new_alphabet(secret):
    """
    Re-construct sting-ALPHABET by pushing forward each alphabet in the string for "secret number" steps.
    Eg. ALPHABET = 'ABCDEF', secret number = 3 -> new alphabet = 'DEFABC'
    :param secret: int, user's secret number
    :return ans: str, new alphabet
    """
    ans = ''
    for i in range(len(ALPHABET)):
        if i < secret:
            ans += ALPHABET[(i + len(ALPHABET)) - secret]
        else:
            ans += ALPHABET[i - secret]
    return ans


def de_code(secret, code):
    """
    Cross-compare user's garbled message with the original ALPHABET to find the meaningful message.
    :param secret: int, user's secret number
    :param code: str, user's garbled message
    :return  ans: str, deciphered message
    """
    ans = ''
    for i in range(len(code)):
        # check whether code[i] is in the new alphabet
        if code[i] in new_alphabet(secret):
            # find the cross-referred alphabet in ALPHABET for each alphabet in the code
            ans += ALPHABET[new_alphabet(secret).find(code[i])]
        else:
            # keep all non-alphabet character in the code
            ans += code[i]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
