import sys; sys.stdin = open('input_data/1952.txt')

def payment(schedule, month, total_pay):
    global min_num
    if total_pay > min_num:
        return
    if month >= 13:
        if total_pay < min_num:
            min_num = total_pay
            return
        return
    if schedule[month]:
        # 3달권
        # if month % 3 == 1:
        total_pay += price[2]
        payment(schedule, month + 3, total_pay)
        total_pay -= price[2]
        # 1달
        if price[1] < schedule[month] * price[0]:
            total_pay += price[1]
            payment(schedule, month + 1, total_pay)
            total_pay -= price[1]
        else:
            total_pay += schedule[month] * price[0]
            payment(schedule, month + 1, total_pay)
            total_pay -= schedule[month] * price[0]
    else:
        payment(schedule, month + 1, total_pay)



for t in range(1, int(input()) + 1):
    price = list(map(int, input().split()))
    schedule = [0] + list(map(int, input().split())) + [0] * 3
    min_num = price[3]
    payment(schedule, 1, 0)
    print('#{} {}'.format(t, min_num))
