__author__ = 'avarm1'

year=[31,28,31,30,31,30,31,31,30,31,30,31]
start_date="9-29"
end_date="12-06"
start_month,start_day =start_date.split("-")
end_month,end_day = end_date.split("-")
for m in range(int(end_month)+1)[int(start_month):]:
    if m == int(start_month):
        for d in range(year[m-1]+1)[int(start_day):]:
            print(m,d)
    elif m==int(end_month):
        for d in range(int(end_day)+1)[1:]:
            print(m,d)
    else:
        for d in range(year[m-1]+1)[1:]:
            print(m,d)



