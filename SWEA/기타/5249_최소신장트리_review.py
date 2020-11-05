# 0~V 까지 정점번호, V+1개
V, E = map(int, input().split())

# 간선들 [u,v, w] w는 가중치
edges = [list(map(int, input().split())) for _ in range(E)]

p = [i for i in range(V+1)]     # maket_set(x)
                                # 트리의 부모를 저장
def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])
edges.sort(reverse=True, key=lambda x: x[2])

count = ans = 0
while count < V:
    u, v, w = edges.pop()
    a, b = findSet(u), findSet(v)
    if a == b: continue
    p[a] = a
    ans += w
    count += 1
print(ans)