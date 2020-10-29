import sys; sys.stdin =open('input_data/1242.txt')

T = int(input())
for t in range(1, 10):
    height, length = map(int, input().split())
    password_list = []
    for _ in range(height):
        line = input()
        check = ''
        for i in range(length-1, -1, -1):
            if not line[i] == '0':
                check = line[i] + check
        if check and check not in password_list:
            password_list.append(check)
            print(len(check))
    for password in password_list:
        print(password_list)
