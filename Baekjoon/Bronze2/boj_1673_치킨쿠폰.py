import sys
sys.stdin= open("input_data/1673.txt",'r')

while True:
    try:
        # data input 받아오기
        coupon, change_stamp = list(map(int,input().split()))
        my_stamp = 0
        my_chicken = 0

        # 쿠폰이 남았거나 / 교환할 도장이 있으면 계속진행
        while coupon != 0 or my_stamp >= change_stamp:
            # 쿠폰이 있으면 사용
            if coupon:
                my_chicken += 1
                my_stamp += 1
                coupon -= 1
            # 없으면 도장 있는거 교환하기
            else:
                coupon += 1
                my_stamp -= change_stamp
        print(my_chicken)
    except EOFError:
        break