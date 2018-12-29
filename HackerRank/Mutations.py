'''
Created on Dec 29, 2018

@author: K3NN!
url : https://www.hackerrank.com/challenges/python-mutations/problem
'''


def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


if __name__ == '__main__':
    pass
