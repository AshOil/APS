import sys
sys.stdin= open("input_data/1362.txt",'r')

# 데이터 전체 불러오기

def ConditionCheck(now):
    if standard/2 < now < standard*2:
        print("{} :-)".format(count))
    elif now <= 0:
        print("{} RIP".format(count))
        still_alive = False
    else:
        print("{} :-(".format(count))


count = 0
still_alive = True
while still_alive:
    try:
        input_data = list(input().split())
        if input_data[0] == 0:
            break
        else:
            if input_data[0].isalpha():
                if input_data[0] == 'F':
                    now_weight += int(input_data[1])
                elif input_data[0] == "E":
                    now_weight -= int(input_data[1])
            elif input_data[0] == '#':
                count +=1
                ConditionCheck(now_weight)
            else:
                standard, now_weight = map(int, input_data)
    except EOFError:
        break
