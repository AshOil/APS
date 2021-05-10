import sys; sys.stdin = open('input_data/9095.txt')

N = int(input())
nums = [int(input()) for _ in range(N)]

check = [0] * 11
# 요 3개는 직접 세었음
check[1] = 1
check[2] = 2
check[3] = 4

for i in range(4, 11):
    # 이 3개를 더하는 이유 :
    # i-1에 있는 항목들에 +1 를 뒤에다 붙여주고
    # i-2에 있는 항목들에 +2 를 뒤에다 붙여주고
    # i-3에 있는 항목들에 +3 을 뒤에다 붙여준다.
    # 애초에 1,2,3 체크할 때 더하기 순서도 반영했기 때문에 요렇게만 가도 된다.
    check[i] = check[i-1] + check[i-2] + check[i-3]
for num in nums:
    print(check[num])
