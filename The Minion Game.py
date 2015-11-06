def stuart():
    input_string=input()
    stuart_count=0
    kevin_count=0
    for length in (range(len(input_string)+1)[1:]):
        for start_index in range(len(input_string)):

            if(input_string[start_index] not in "AEIOU" and int((start_index+length)/(len(input_string)+1))==0):

               stuart_count=stuart_count+1

            elif(input_string[start_index]  in "AEIOU" and int((start_index+length)/(len(input_string)+1))==0):
                kevin_count=kevin_count+1

    if(stuart_count>kevin_count):
        print("Stuart",stuart_count)
    elif(kevin_count>stuart_count):
        print("Kevin",kevin_count)
    else:
        print("Draw")

def modifiedstuart():
    input_string=input()
    stuart_count=0
    kevin_count=0
    for start_index in range(len(input_string)):

            if(input_string[start_index] not in "AEIOU"):

               stuart_count=stuart_count+(len(input_string)-start_index)

            elif(input_string[start_index]  in "AEIOU"):
                kevin_count=kevin_count+(len(input_string)-start_index)

    if(stuart_count>kevin_count):
        print("Stuart",stuart_count)
    elif(kevin_count>stuart_count):
        print("Kevin",kevin_count)
    else:
        print("Draw")

modifiedstuart()