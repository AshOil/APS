N=5
number = 12
result = -1
results = [[] for _ in range(9)]
results[1].append(N)
now = 2

while now < 9:
    results[now].append(N*int("1"*now))
    for i in range(1, now//2+1):
        for num in results[i]:
            for num2 in results[now- i]:
                if num+num2 not in results[now]:
                    results[now].append(num+num2)
                if num - num2 not in results[now]:
                    results[now].append(num-num2)
                if num * num2 not in results[now]:
                    results[now].append(num*num2)
                if num2 and num//num2 not in results[now]:
                    results[now].append(num//num2)
                if num and num2//num not in results[now]:
                    results[now].append(num2//num)

    now +=1
for i in range(1, 9):
    if number in results[i]:
        result = i
        break
print(results)
print(result)
