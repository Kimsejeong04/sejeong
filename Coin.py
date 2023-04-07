charge = int(input("청구 금액(원): "))
inkum = 0
outkum = 0
payment = 0
cardstatus = 0

while True:
    payment = int(input("결제방법(현금이면 1, 아니면 0)? "))
    if payment:
        inkum = int(input("받은 금액(원): "))
        outkum = inkum - charge
        if outkum < 0:
            print("금액 부족!")
            continue
        else:
            print(outkum, "원 반환")
            print("감사합니다.")
            break
    else:
        cardstatus = int(input("카드상태(정상이면 1, 아니면 0)?: "))
        if not cardstatus:
            continue
        else:
            print("감사합니다.")
            break

