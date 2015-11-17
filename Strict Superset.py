__author__ = 'avarm1'


superset=set([int(x) for x in input().strip().split(" ")])
N=int(input())
data = [set(int(x) for x in input().strip().split(" ")) for _ in range(N)]
flag=True
for x in data:
    if(not superset.issuperset(x) or (superset.issuperset(x) and len(superset)==len(x))):
        flag=False
print(flag)