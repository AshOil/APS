import sys; sys.stdin = open('input_data/2206.txt')
from pprint import pprint

height, width = map(int,input().split())
Ground = [list(map(int,' '.join(input()).split())) for _ in range(height)]
pprint(Ground)
