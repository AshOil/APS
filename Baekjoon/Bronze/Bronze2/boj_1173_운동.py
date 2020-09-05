# 진행중

import sys
sys.stdin= open("input_data/1173.txt",'r')

time, now_hb, max_hb, up_hb, down_hb = list(map(int,input().split()))

result = 0
exercise = 0
start_hb = now_hb

if max_hb - now_hb < up_hb:
    print(-1)
else:
    for _ in range(100):
        if now_hb + up_hb <= max_hb:
            result +=1
            exercise +=1
            now_hb += up_hb
        else:
            result+=1
            now_hb -= down_hb
            if now_hb < start_hb:
                now_hb = start_hb
        if exercise == time:
            break
    print(result)


