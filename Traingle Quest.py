__author__ = 'avarm1'

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int( i*(10**(i-1))+i*10**((i)-2)+i*10**((i)-3)+i*10**((i)-4)+i*10**((i)-5)+i*10**((i)-6)+i*10**((i)-7)+i*10**((i)-8)+i*10**((i)-9)))