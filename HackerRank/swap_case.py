'''
Created on Dec 29, 2018

@author: K3NN!

url : https://www.hackerrank.com/challenges/swap-case/problem
'''


def swap_case(s):
    swap = []
    for letter in s:
        if letter.islower():
            letter = letter.upper()
            swap.append(letter)
        elif letter.isupper():
            letter = letter.lower()
            swap.append(letter)
        else:
            swap.append(letter)
    return ''.join(swap)


if __name__ == '__main__':
    print(swap_case('HackerRank.com presents "Pythonist 2".'))
