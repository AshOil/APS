import sys
sys.stdin = open('input_data/1244.txt','r')

# 데이터 불러오기
length = int(input())
switch = list(map(int,input().split()))
students = int(input())
push = []
for _ in range(students):
    push.append(list(map(int,input().split())))

# 남학생
for click in push:
    if click[0] == 1:
        count = 2
        num = click[1]
        while num <= length:
            if switch[num-1] == 1:
                switch[num - 1] = 0
            else:
                switch[num - 1] = 1
            num = click[1] * count
            count +=1
#여학생
    else:
        i = j = click[1]-1
        while i-1>=0 and j+1<length and switch[i-1] == switch[j+1] :
            i -= 1
            j += 1
        for num in range(i,j+1):
            if switch[num]:
                switch[num]=0
            else:
                switch[num]=1
    print(switch)
