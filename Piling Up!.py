__author__ = 'avarm1'

"""There is a horizontal row of n cubes. Side length of each cube from left to right is given. You need to create a new vertical pile of cubes. The new pile should be such that if cubei is on cubej then sideLengthj?sideLengthi. But at a time, you can only pick either the leftmost or the rightmost cube only. Print "Yes" if its possible, "No" otherwise.

Input Format

First line contains a single integer T, denoting the number of test cases.
For each testcase, there are 2 lines.
First line of each test case contains n.
Second line of each test case contains n space separated integers, the sideLengths of the cubes in that order.

Constraints
1?T?5
1?n?105
1?sideLength<231
Output Format

For each testcase, output a single line containing a single word, either a "Yes" or a "No"."""

no_test_cases=int(input())
while(no_test_cases>0):
    dumy=input()
    stream=(input())
    flag=True
    stream=[int(x) for x in stream.strip().split(" ")]
    number=2**32


    while(len(stream)>0):
        left,right=stream[0],stream[-1]
        if((right>=left and right<=number) or (right<=left and right<=number and left>number)):
            number=right
            stream.pop()

        elif(left<=number):
            number=left
            stream.pop(0)

        else:
            print("No")
            flag=False
            break
    if(flag==True):
        print("Yes")
    no_test_cases=no_test_cases-1


