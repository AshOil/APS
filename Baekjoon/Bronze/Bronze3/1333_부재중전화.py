import sys; sys.stdin = open("input_data/1333.txt")

def can_check(length_song, num_song):



num_song, length_song, phone_call = map(int, input().split())
track, call_num = 1, 1
now_song = (length_song + 5) * track
now_call = phone_call * call_num
status = False
while not status:
