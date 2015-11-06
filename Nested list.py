__author__ = 'avarm1'

"""Problem Statement

Now we will see how to implement a nested list. There is a classroom of 'n' students and you are given their names and marks in physics.
 Store them in a nested list and print the name of each student who got the second lowest marks in physics.

NOTE: If there are more than one student getting same marks, make sure you print the names of all students in alphabetical order,
in different lines.

Input Format

Integer N followed by alternating sequence of N strings and N numbers.

Output Format

Name of student.

Constraints

1?N?5 """

#code begin

number = int(input())
primary_list=[[input(), input()] for _ in range(number)]
list_of_scores=[float(x[1]) for x in primary_list]
list_of_scores_with_min_removed=[x for x in list_of_scores if x!= min(list_of_scores) ]
list_of_scores_with_secondleast_removed=[x for x in primary_list if float(x[1])==min(list_of_scores_with_min_removed)]
list_with_min_removed=sorted(list_of_scores_with_secondleast_removed)
for x in list_with_min_removed:
    print(x[0])

