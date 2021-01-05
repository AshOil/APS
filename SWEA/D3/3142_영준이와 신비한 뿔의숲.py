import sys; sys.stdin = open('input_data/3142.txt')

for t in range(1, int(input()) + 1):
    horns, animals = map(int, input().split())
    twinhorn = horns - animals
    print("#{} {} {}".format(t, animals - twinhorn, twinhorn))