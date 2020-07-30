import sys
sys.stdin = open('input_data/1959.txt',"r")

T = int(input())

for t in range(1, T+1):
    mn_number = list(map(int, input() .split()))
    n_length = mn_number[0]
    m_length = mn_number[1]
    n_list = list(map(int, input() .split()))
    m_list = list(map(int, input() .split()))
    count_list = []
    if n_length < m_length:
        for _ in range(m_length - n_length + 1):
            count = 0
            for num in range(n_length):
                count += n_list[num] * m_list[num]
            count_list.append(count)
            m_list.pop(0)
            max_num = max(count_list)
        print('#{} {}'.format(t,max_num))
    else:
        n_length, m_length = m_length, n_length
        n_list, m_list = m_list, n_list
        for _ in range(m_length - n_length + 1):
            count = 0
            for num in range(n_length):
                count += n_list[num] * m_list[num]
            count_list.append(count)
            m_list.pop(0)
            max_num = max(count_list)
        print('#{} {}'.format(t,max_num))
        