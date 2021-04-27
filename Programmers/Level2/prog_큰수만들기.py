
number = '417725241'
k = 4
number = list(number)
now = 0
first_max = number.index(max(number))
if first_max < k:
    number = number[first_max:]
    k -= first_max
while k:
    while k and number[now] < number[now+1]:
        number.pop(now)
        k -= 1
        if now:
            now -= 1
        if number == sorted(number, reverse=True):
            while k:
                number.pop()
                k -= 1
        continue
    else:
        now += 1
print(''.join(number))
