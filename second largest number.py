__author__ = 'avarm1'
"""Problem Statement

Now, lets delve into one of the most basic data types in python, LIST. You are given 'n' numbers. Store them in a list and find the second largest number. Easy enough!

NOTE : Don't use insertion sort

Input Format

First line contains N. Second line contains Array A[] of N integers each separated by a space.

Output Format

Value of the second largest number."""
import copy
number = int(input())
list = input()
list=list.split(" ")

list=[int(x) for x in list]

newlist=[int(x) for x in list if x!=max(list)]


print(max(newlist))