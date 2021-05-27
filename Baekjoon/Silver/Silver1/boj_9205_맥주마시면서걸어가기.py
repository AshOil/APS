import sys; sys.stdin = open('input_data/9205.txt')

def get_distance(place_a, place_b):
    if abs(place_a[0]-place_b[0]) + abs(place_a[1]-place_b[1]) <= 1000:
        return True
    else:
        return False
    
def DFS(place):
    global result
    if result == "happy": return
    if get_distance(place[1:], destination):
        result ="happy"
        return

    for store in stores:
        if not visit[store[0]] and get_distance(place[1:], store[1:]):
            visit[store[0]] = 1
            DFS(store)
            visit[store[0]] = 0



for t in range(int(input())):
    num_store = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(num_store)]
    destination = list(map(int, input().split()))
    visit = [0]* num_store
    result = "sad"
    for idx, store in enumerate(stores):
        store.insert(0, idx)

    now = list(home)
    for store in stores:
        if get_distance(now, store[1:]):
            visit[store[0]] = 1
            DFS(store)
            visit[store[0]] = 0
        if result == "happy":
            break
    print(result)