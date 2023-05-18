menu = {'COFFEE': [['에스프레소', 3.0], ['아메리카노', 3.0], ['카페라떼', 4.0], ['카프치노', 4.0]],
          'LATTE': [['말차라떼', 4.0], ['초코라떼', 4.0], ['카페라떼', 4.0]],
          'TEA': [['청귤차', 4.0], ['자몽차', 4.0], ['레몬차', 4.0], ['카모마일', 4.5]],
          'ADE': [['자몽에이드', 4.5], ['레몬에이드', 4.5], ['청포도에이드', 4.5]],
          'JUICE': [['망고', 4.5], ['바나나', 4.5], ['딸기', 4.5], ['키위', 4.5]],
          'SMOOTHIE': [['청귤스무디', 4.5], ['요거트스무디', 4.5]],
          'MILK TEA': [['흑당밀크티', 4.5], ['달고나밀크티', 4.5]]}

print("\n [[ 소분류 메뉴 ]]")
for title, mlist in menu.items():
    print(title)
    for mmenu, price in mlist:
        print(mmenu, '\t', price)
    print()

menugroup = {}
no = 0
for title in menu.keys():
    menugroup[no] = title
    no += 1

'''for no, title in menugroup.items():
    print(no, title)'''
selmlist = []
while True:
    print("\n>> [선택] 대분류 메뉴 <<")
    for no, title in menugroup.items():
        print("[%d] %s" % (no, title))  # 대분류 메뉴 출력
    mcnt = len(menugroup)
    nogroup = -1   #변수사용할 떼 초기값 유의
    while nogroup < 0 or nogroup >= mcnt:
        nogroup = int(input(">>메뉴 그룹(번호) 선택: "))
    inkey = menugroup.get(nogroup)
    mlist = menu.get(inkey)

    print("\n>> [선택] 소분류 메뉴 <<")
    seq = 0
    for mmenu, price in mlist:
        print("[%d] %s %.1f" %(seq, mmenu, price))
        seq += 1
    nomenu = int(input(">>메뉴(번호) 선택: "))
    selected = mlist[nomenu][0]
    print(selected)
    inqty = int(input(">>몇 잔을 원하십니까? "))
    print("> [%s]를 [%d]잔을 선택히셨습니다." %(mlist[nomenu][0], inqty))
    totprice = mlist[nomenu][1] * inqty * 1000
    slist = [selected, mlist[nomenu][1], inqty, totprice]
    selmlist.append(slist)
    insel = input(">>계속 주문을 하시겠습니까? [종료: x, 계속: Enter] ")
    if insel == 'x' or insel == 'X':
        break

print("========<< 주문 내역 >>========")
totqty = 0
totwon = 0
for x in selmlist:
    mmenu, price, inqty, totprice = x
    totqty += inqty
    totwon += totprice
    print(f"{mmenu}\t가격: {price}\t수량: {inqty}\t총 가격: {totprice}")
print(f"총 주문 수량: {totqty}\t총 주문 가격: {totwon}")
print("------------------------------")
