__author__ = 'avarm1'

"""Problem Statement

Task

Read N and print the decimal, octal, hexadecimal, and binary values from 1 to N with space padding so that all fields take the same width as the binary value.

Input Format
First line contains an integer N.

Constraints
1?N?99
Output Format
Print N lines. Formatted as width of binary value of N."""

number = int(input())
binary=bin(number)[2:]
length=(len(binary)+1)
for i in range(number+1)[1:]:
    print(("%"+str(length-1)+"s"+"%"+str(length)+"s"+"%"+str(length)+"s"+"%"+str(length)+"s")%(i,oct(i)[2:],hex(i)[2:].upper(),bin(i)[2:]))