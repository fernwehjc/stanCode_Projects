"""
File: hangman.py
Author: Jade YEH
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    User will be requested to guess a random word.
    And the user will be given 7 chances to get wrong.
    And the user can only guess one character at a single time.
    After 7 wrong guesses, the user loses the game.
    """
    # come out a random word
    ans = random_word()
    # hide the answer with '-'
    riddle = hide(ans)
    # the number of guess the player has
    chance_left = N_TURNS
    print('The word looks like: ' + hide(ans))
    print('You have ' + str(chance_left) + ' guesses left.')
    guess(ans, riddle, chance_left)


def guess(ans, riddle, chance_left):
    """
    User play and get feedback.
    :param ans: str, the initiated random word
    :param riddle: str, has an identical length of ans but with each alphabet covered with '-'
    :param chance_left: int, the number of guess the player has
    """
    while True:
        # User make a guess
        idea = input('Your guess: ')
        idea = idea.upper()
        # check whether the user's input is valid
        if str.isalpha(idea):
            # check whether the input is only one character
            if len(idea) == 1:
                # check whether right guess
                if ans.find(idea) != -1:
                    # right guess -> chance remain the same
                    chance_left += 0
                    # show clear riddle with user's right guess
                    clear_riddle(riddle, idea, ans)
                    riddle = clear_riddle(riddle, idea, ans)
                    # check whether user win the game
                    win_check(riddle)
                    if win_check(riddle) == 0:
                        # user find the whole word
                        win(ans)
                        break
                    else:
                        # user can continue guess
                        right_continue(riddle, chance_left)
                else:
                    # wrong guess -> reduce one chance
                    chance_left += -1
                    # check whether user lose the game
                    if chance_left == 0:
                        # user fail to find the whole word with limited chances
                        hung(idea, ans)
                        break
                    else:
                        # user can continue guess
                        wrong_continue(idea, riddle, chance_left)
            else:
                # input is string but more than one alphabet -> show message to user, chance remain the same
                print('Illegal format.')
                chance_left += 0
        else:
            # inputs are not entirely all alphabet -> show message to user, chance remain the same
            print('Illegal format.')
            chance_left += 0


def wrong_continue(idea, riddle, chance_left):
    """
    Message for user who guess wrong but still have chance to play
    :param idea: str, the user's guess
    :param riddle: str, the latest guess result
    :param chance_left:
    :return: message to user
    """
    print('There is no ' + idea + '\'s in the word.')
    print('The word looks like: ' + riddle)
    print('You have ' + str(chance_left) + ' guesses left.')


def hung(idea, ans):
    """
    Message for user who guess wrong and have no more chance to play
    :param idea: str, the user's guess
    :param ans: str, the initiated random word
    :return: message to user
    """
    print('There is no ' + idea + '\'s in the word.')
    print('You are completely hung : (')
    print('The word was: ' + ans)


def right_continue(riddle, chance_left):
    """
    Message for user who guess right but still need to continue guess
    :param riddle: str, the latest guess result
    :param chance_left: int, the number of guess the player has
    :return: message to user
    """
    print('You are correct!')
    print('The word looks like: ' + riddle)
    print('You have ' + str(chance_left) + ' guesses left.')


def win(ans):
    """
    Message for user who win the game by solving the whole word within limited guess chance
    :param ans: str, the initiated random word
    :return: message to user
    """
    print('You are correct!')
    print('YOU WIN!!!')
    print('The word was: ' + ans)


def win_check(riddle):
    """
    Check whether user have get the whole word.
    :param riddle: str, user's guess
    :return win: int, 0 = no any un-found alphabet
    """
    win = 0
    for i in range(len(riddle)):
        # check whether any character other than alphabet exist
        if str.isalpha(riddle[i]):
            win += 0
        else:
            # for each un-found alphabet -> count one
            win += 1
    return win


def clear_riddle(riddle, idea, ans):
    """
    Re-construct the riddle with user's right guess
    :param riddle: str, the latest guess result
    :param idea: str, the user's guess
    :param ans: str, the initiated random word
    :return new_riddle: str, the updated guess result
    """
    new_riddle = ''
    for i in range(len(ans)):
        if idea in ans[i]:
            # update the right guess in the right position
            new_riddle += idea
        elif str.isalpha(riddle[i]):
            # keep previous right guess
            new_riddle += riddle[i]
        else:
            # remain unsolved part
            new_riddle += '-'
    return new_riddle


def hide(ans):
    """
    To hide the answer form the user.
    :param ans: str, the initiated random word
    :return riddle: str, has an identical length of ans but with each alphabet covered with '-'
    """
    riddle = ''
    for i in range(len(ans)):
        riddle += '-'
    return riddle


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
