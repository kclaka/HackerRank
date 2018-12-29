'''
Created on Dec 29, 2018

@author: K3NN!
url : https://www.hackerrank.com/challenges/whats-your-name/problem
'''


def print_full_name(a, b):
    print("Hello " + a + ' ' + b + "! You just delved into python.")


if __name__ == '__main__':
    a = str(input())
    b = str(input())
    print_full_name(a, b)
