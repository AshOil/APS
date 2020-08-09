a = 10  # 전역 변수
b = 20  # 전역 변수


def enclosed():
    a = 30  # enclosed함수의 지역 변수

    def local():
        c = 40  # local함수의 지역 변수
        print(a, b, c)

    local()

    a = 50  # enclosed함수의 지역 변수이며, local함수에서는 Enclosed Scope


print(enclosed())  # 이게 어떤 값을 출력할지 예상해보고 확인해보세요.