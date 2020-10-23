import sys; sys.stdin = open('input_data/1240.txt')

secret = {
    '0001101' : 0, '0011001' : 1,
    '0010011' : 2, '0111101' : 3,
    '0100011' : 4, '0110001' : 5,
    '0101111' : 6, '0111011' : 7,
    '0110111' : 8, '0001011' : 9
}

for t in range(1, int(input()) + 1):
    height, width = map(int,input().split())
    for _ in range(height):
        code = input()
        if '1' in code:
            check = code
    for i in range(width-1, 0, -1):
        if check[i] == '1':
            end = i
            break
    password = []
    for i in range(end - 55, end+1, 7):
        password.append(check[i: i+7])
    decode = []
    for code in password:
        decode.append(secret[code])
    sum_code = 0
    for i in range(7):
        if i % 2:
            sum_code += decode[i]
        else:
            sum_code += decode[i]*3
    if (sum_code + decode[7]) % 10:
        print('#{} 0'.format(t))
    else:
        print('#{} {}'.format(t, sum(decode)))
