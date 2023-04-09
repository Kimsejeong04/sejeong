import random as r
rnum = r.randint(1, 20)
print("1 ~ 20 중에 하나의 난수를 발생했습니다.")

while True:
    try:
        innum = int(input("숫자 입력(1 ~ 20): "))
        if innum < 1 or innum >20:
            print("1~20 사이의 숫자를 입력해주세요.")

        else:
            if rnum < innum:
                print("Down!")

            elif rnum > innum:
                print("UP!")
        
            else:
                print("정답입니다!")
                break
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
