import sys
sys.stdin = open("input_data/4865.txt")

T = int(input())
for t in range(1, T+1):
    short = input()
    long = input()
    results = {}
    for char in short:
        results[char] = long.count(char)
    print('#{} {}'.format(t, max(results.values())))



