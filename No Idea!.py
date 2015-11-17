__author__ = 'avarm1'
"""Problem Statement

There is an array of n integers, and 2 disjoint sets of m integers each A and B. You like all integers in A and dislike all integers in B. Your initial happiness is 0 and for each integer in the array, i, if i?A, you add 1 to your happiness, if i?B, you add ?1 to your happiness, else your happiness does not change. Output your final happiness at the end.

Note that since A and B are sets, they have no repeated elements. But, the array might contain duplicate elements.

Constraints
1?n?105
1?m?105
1?Any integer in the input?109

Input Format

First line contains n and m.
Second line contains n integers, the array.
Third and fourth lines contain m integers, A and B respectively.

Output Format

Output a single integer, the answer."""

list_size,set_size=[int(x) for x in input().strip().split(" ")]
array=[int(x) for x in input().strip().split(" ")]
set1,set2=((set(int(x) for x in input().strip().split(" "))) for _ in range(2))
happiness=0
for x in array:
    if x in set1:
        happiness=happiness+1
    if x in set2:
        happiness=happiness-1
print(happiness)