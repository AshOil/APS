import sys
sys.stdin = open("input_data/1933.txt","r")

number = int(input())

for i in range(1,number+1):
    if number%i:
        pass
    else:
        print(i,end=' ')