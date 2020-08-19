import sys
sys.stdin= open("input_data/1225.txt",'r')

A, B = list(input().split())
A = sum(list(map(int,A)))
B = sum(list(map(int,B)))
print(A*B)
