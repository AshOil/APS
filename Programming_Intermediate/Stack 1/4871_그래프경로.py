import sys
sys.stdin = open("input_data/4871.txt", 'r')

# 테스트 케이스 갯수 input
T = int(input())
for t in range(1, T+1):
    # `점 갯수`랑 `선 갯수` input
    V, E = map(int, input().split())

    # 선 갯수만큼 `선 위치정보` input
    arr = [list(map(int,input().split()))for _ in range(E)]

    # 점 `시작점`, `끝점` 정보 input
    start, end = map(int, input().split())

    # 0으로 구성된 점연결 Table 구성 (V+1) X (V+1)
    G = [[0] * (V+1) for _ in range(V+1)]

    # 점 방문 여부 확인할 0으로 구성된 list 형성 (V+1)
    visit = [0] * (V+1)

    # 선 위치정보 Table에 입력하기 (기존 0으로 되어있던 걸 1로)
    for in_arr in arr:
        u, v = in_arr[0], in_arr[1]
        G[u][v] = 1

    # S list만들기 (방문했던곳 적어놓고 하나씩 뒤돌아옴(헨젤과 그레텔 빵조각) // 다 뒤돌아오면 종료)
    S=[start]
    visit[start] = 1
    v = start

    # S를 다 둘러볼 동안
    while S:
        # w : 다음 갈 방향 확인 (점 갯수 전체 파악)
        for w in range(1,V+1):
            # G[v][w] : 만약 길이 있고 // not visit[w] 방문했던 곳이 아니라면
            if G[v][w] and not visit[w]:
                # 방문일지에 적고
                visit[w] = 1
                # 왔던 길 안잃어버리게 적어놓고
                S.append(v)
                # 가자!
                v = w
                break
        # 갈일이 없네.. 뒤돌아가서 다른길 찾아보자
        else:
            v = S.pop()
    print('#{} {}'.format(t, visit[end]))

