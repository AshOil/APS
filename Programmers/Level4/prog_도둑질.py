money = [11,0,2,5,100,100,85,1]
N = len(money)
# 첫집 갈때, 안갈 때
money1 = money[:N-1]
money2 = money[1:]
visit1 = [0]*N
visit2 = [0]*N

visit1[0] = money1[0]
visit1[1] = money1[1]
for i in range(2, N-1):
    visit1[i] = money1[i] + max(visit1[i-3], visit1[i-2])
visit2[0] = money2[0]
visit2[1] = money2[1]
for i in range(2, N-1):
    visit2[i] = money2[i] + max(visit2[i-3], visit2[i-2])
print(max(visit1+visit2))

