fee = 10000
print("입장료는 %d원입니다." %fee)
print("신분이 어떻게 되는지 y나 기타 키로 답하세요.")

status = input("70세 이상이신가요(y)?").strip().lower()
if status == 'y':
    fee = int(fee * 100/100)
    print("100%가 할인되어 입장료는 무료입니다.")

else:
    status = input("지역주민이신가요(y)?").strip().lower()
    if status == 'y':
        fee = int(fee * 100/50)
        print("50%가 할인되어 입장료는 5000원입니다.")

    status = input("국가유공자 또는 현역군인이신가요(y)?")
    if status == 'y':
        fee = int(fee * 100/30)
        print("30%가 할인되어 입장료는 7000원입니다.")