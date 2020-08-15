import sys
sys.stdin = open('input_data/2615.txt','r')

numbers=[]
for _ in range(19):
    numbers.append(list(map(int,input().split())))
for idx1, number in enumerate(numbers):
    for idx2, num in enumerate(number):
        count = 0
        my_num = 0
        if num:
            if num == my_num:
                count += 1
                if count == 5:
                    x, y = idx1 + 1, idx2 +1 -5
            else:
                my_num = num
                count = 1
    if count == 5:
        result = True
        if my_num == 1:
            print(1)
        else:
            print(2)
        print(x, y)

result = False
for i in range(19):
    for j in range(19):
        count = 0
        my_num = 0
        if numbers[j][i]:
            if numbers[j][i] == my_num:
                count += 1
                if count == 5:
                    x, y = j -5 , i
            else:
                my_num = numbers[j][i]
                count = 1
    if count == 5:
        result = True
        if my_num == 1:
            print(1)
        else:
            print(2)
        print(x,y)

#위 위
for idx, j in enumerate(range(18,-1,-1)):
    count = 0
    my_num = 0
    number = []
    for i in range(19-idx):
        if numbers[i][i+idx]:
            if numbers[i][i+idx] == my_num:
                count += 1
                if count == 5:
                    x, y = i +2-5 , i+idx -5 +2
            else:
                my_num = numbers[i][i+idx]
                count = 1
    if count == 5:
        result =True
        if my_num == 1:
            print(1)
        else:
            print(2)
        print(x,y)

# 위 아래
for idx, j in enumerate(range(18,-1,-1)):
    count = 0
    my_num = 0
    number = []
    for i in range(19-idx):
        if numbers[i+idx][i]:
            if numbers[i + idx][i] == my_num:
                count += 1
                if count ==5:
                    y, x = i -5 +2 , i+idx -5 +2
            else:
                my_num = numbers[i + idx][i]
                count = 1
        if count == 5:
            result = True
            if my_num == 1:
                print(1)
            else:
                print(2)
            print(x,y)



# 아래 위
for idx, j in enumerate(range(18,-1,-1)):
    count =0
    my_num = 0
    number = []
    for i in range(19-idx):
        if numbers[j-i][i]:
            if numbers[j-i][i] == my_num:
                count += 1
                if count ==5:
                    x, y = j-i +1 , i + 1
            else:
                my_num = numbers[j-i][i]
                count = 1
        if count == 5:
            result = True
            if my_num == 1:
                print(1)
            else:
                print(2)
            print(x,y)

# 아래 아래
for idx, j in enumerate(range(18,-1,-1)):
    number = []
    my_num = 0
    count = 0
    for i in range(idx, 19):
        if numbers[i][18-i]:
            if numbers[i][18-i] == my_num:
                count += 1
                if count == 5:
                    x, y = i +1 , 18- i +1
            else:
                my_num = numbers[i][18-i]
                count = 1
        if count == 5:
            result = True
            if my_num == 1:
                print(1)
            else:
                print(2)
            print(x,y)

if result == False:
    print(0)