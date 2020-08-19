import sys
sys.stdin= open("input_data/1193.txt",'r')

number = int(input())
num = 1
cnt = 1
while num +cnt < number:
    num += cnt
    cnt += 1
son =  1
count = num
mom = maximum = cnt

while count < number:
    count += 1
    if son == maximum:
        maximum +=1
        mom = maximum
        son = 1
    else:
        mom -=1
        son +=1
if maximum%2:
    print('{}/{}'.format(mom,son))
else:
    print('{}/{}'.format(son,mom))