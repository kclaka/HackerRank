'''
Created on Dec 28, 2018

@author: K3NN!

url : https://www.hackerrank.com/challenges/py-if-else/problem

Task 
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

Input Format
A single line containing a positive integer,n .

Constraints
1 <= n <= 100
Output Format
Print Weird if the number is weird; otherwise, print Not Weird.
'''


N = int(input())

if (N % 2 == 0) and (2 < N < 6):
    print("Not Weird")
elif (N % 2 == 0) and (5 < N < 21):
    print("Weird")
elif (N % 2 == 0) and (N > 20):
    print("Not Weird")
else:
    print("Weird")
    

if __name__ == '__main__':
    pass