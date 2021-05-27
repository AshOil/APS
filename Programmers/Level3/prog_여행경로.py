from copy import deepcopy
tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]

detartures = {"ICN" : 0}
translate = ["ICN"]
count = 1
routes = []

def DFS(x, route):
    route.append(translate[x])
    if len(route) == len(tickets)+1:
        if route not in routes:
            routes.append(deepcopy(route))
    for i in range(N):
        if Ground[x][i]:
            Ground[x][i] -= 1
            DFS(i, route)
            Ground[x][i] += 1
    route.pop()

for ticket in tickets:
    if ticket[0] not in detartures.keys():
        detartures[ticket[0]] = count
        translate.append(ticket[0])
        count+=1
    if ticket[1] not in detartures.keys():
        detartures[ticket[1]] = count
        translate.append(ticket[1])
        count+=1
N = len(detartures)

Ground = [[0]*N for _ in range(N)]
for ticket in tickets:
    Ground[detartures[ticket[0]]][detartures[ticket[1]]] += 1

DFS(0, [])
result = sorted(routes, key=lambda x : [x[i] for i in range(len(routes[0]))])
print(result[0])