import sys
sys.stdin = open('input_data/1204.txt','r')

T = int(input())
for t in range(1, T+1):
    case_number = int(input())
    numbers = list(map(int, input() .split()))

    numbers_dict = {}
    for number in numbers:
        numbers_dict[str(number)] = numbers.count(number)
    max_number = max(list(numbers_dict.values()))
    standard_value = 0
    that_number = []
    for idx, key in enumerate(numbers_dict):
        if numbers_dict[key] > standard_value:
            that_number = []
            standard_value = numbers_dict[key]
            that_number.append(idx)
        elif numbers_dict[key] == standard_value:
            that_number.append(idx)
    result_list=[]
    for num in that_number:
        result_list.append(list(numbers_dict.keys())[num])
    final_list = str(max(map(str,result_list)))
    print('#{} {}'.format(t, final_list))
            
