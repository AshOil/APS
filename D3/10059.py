import sys
sys.stdin = open('input_data/10059.txt',"r")

T = int(input())

for t in range(1,T+1):
    sample_date = str(input())
    MM = int(sample_date[0:2])
    YY = int(sample_date[2:4])
    if 13> MM >0 and 13 > YY > 0:
        print('#{} AMBIGUOUS'.format(t))
    elif 13> MM >0 and YY >12:
        print('#{} MMYY'.format(t))
    elif MM >12 and 13 > YY > 0:
        print('#{} YYMM'.format(t))
    else:
        print('#{} NA'.format(t))





            