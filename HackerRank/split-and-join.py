'''
Created on Dec 29, 2018

@author: K3NN!
url = https://www.hackerrank.com/challenges/python-string-split-and-join/problem
'''


def split_and_join(line):
   line = line.split(" ")
   line = '-'.join(line)
   return line
    
    
if __name__ == '__main__':
    print(split_and_join('this is a string')) 