__author__ = 'avarm1'
number = input()
number=int(number)
list=[]
while(number>0):
    temp = input()
    temp=temp.split(" ")
    if(len(temp)==3):
        eval("list.%s(%d,%d)"%(temp[0],int(temp[1]),int(temp[2])))

        number=number-1
    elif(len(temp)==2):
        eval("list.%s(%d)"%(temp[0],int(temp[1])))
        number=number-1
    elif(temp[0]=="print"):
        print(list)

    else:
        eval("list.%s()"%temp[0])
        number=number-1


