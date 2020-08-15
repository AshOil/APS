import sys
sys.stdin = open('input_data/6485.txt','r')

T = int(input())

for t in range(1, T+1):
    bus_num = int(input())
    routes = []
    for route in range(bus_num):
        routes.append(list(map(int, input().split())))
    station_num = int(input())
    stations = {}
    for station in range(station_num):
        stations[input()] = 0

    for i in range(bus_num):
        for j in range(routes[i][0], routes[i][1]+1):
            if str(j) in stations.keys():
                stations[str(j)]+=1
    result = ' '.join(list(map(str,stations.values())))
    print('#{} {}'.format(t, result))


