import sys; sys.stdin = open('input_data/4366.txt')

for t in range(1, int(input()) + 1):
    twojin = list(' '.join(input()).split())
    threejin = list(' '.join(input()).split())
    twojin_list = []
    for i in range(len(twojin)):
        if twojin[i] == '1':
            twojin[i] = '0'
            twojin_list.append(int(''.join(twojin), 2))
            twojin[i] = '1'
        else:
            twojin[i] = '1'
            twojin_list.append(int(''.join(twojin), 2))
            twojin[i] = '0'
    for i in range(len(threejin)):
        if threejin[i] == '1':
            threejin[i] = '0'
            threejin_num = int(''.join(threejin), 3)
            if threejin_num in twojin_list:
                print('#{} {}'.format(t, threejin_num))
                break
            threejin[i] = '2'
            threejin_num = int(''.join(threejin), 3)
            if threejin_num in twojin_list:
                print('#{} {}'.format(t, threejin_num))
                break
            threejin[i] = '1'
        elif threejin[i] == '2':
            threejin[i] = '0'
            threejin_num = int(''.join(threejin), 3)
            if threejin_num in twojin_list:
                print('#{} {}'.format(t, threejin_num))
                break
            threejin[i] = '1'
            threejin_num = int(''.join(threejin), 3)
            if threejin_num in twojin_list:
                print('#{} {}'.format(t, threejin_num))
                break
            threejin[i] = '2'
        else:
            threejin[i] = '1'
            threejin_num = int(''.join(threejin), 3)
            if threejin_num in twojin_list:
                print('#{} {}'.format(t, threejin_num))
                break
            threejin[i] = '2'
            threejin_num = int(''.join(threejin), 3)
            if threejin_num in twojin_list:
                print('#{} {}'.format(t, threejin_num))
                break
            threejin[i] = '0'