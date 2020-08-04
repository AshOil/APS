import sys
sys.stdin = open('input_data/1940.txt',"r")

T = int(input())
for t in range(1, T+1):
    total_speed = 0
    distance = 0
    turn = int(input())
    for _ in range(turn):
        numbers = list(map(int, input() .split()))
        print(len(numbers))

        if len(numbers) > 1:
            way, speed = numbers
            if way == 1 :
                total_speed += speed
                distance += abs(total_speed)
            else:
                total_speed -= speed
                distance += abs(total_speed)
        else:
            distance += abs(total_speed)

    print('#{} {}'.format(t, distance))
            
