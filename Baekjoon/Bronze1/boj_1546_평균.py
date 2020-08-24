import sys
sys.stdin = open('input_data/1546.txt', "r")

number = int(input())
tests = list(map(int,input().split()))
max_grade = max(tests)
# 새로 계산한 점수 넣을 곳
new_tests = []
for test in tests:
    new_tests.append((test/max_grade)*100) # 주어진 수식 적용
print(sum(new_tests)/number)