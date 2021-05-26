from itertools import combinations
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

result = []
for i in course:
    all_combiation = {}
    for order in orders:
        com_results = list(map(list,combinations(order, i)))
        for com_result in com_results:
            com_result.sort()
            now = "".join(com_result)
            if now in all_combiation.keys():
                all_combiation[now] += 1
            else:
                all_combiation[now] = 1
    sorted_combi = sorted(all_combiation.items(), key=lambda x: (x[1]), reverse=True)
    if sorted_combi:
        count = sorted_combi[0][1]
        if count > 1:
            for nomi in sorted_combi:
                if nomi[1] == count:
                    result.append(nomi[0])
result.sort()
print(result)
