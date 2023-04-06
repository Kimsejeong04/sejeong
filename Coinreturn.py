#print("Hello, world")

totwon = 0 #청구금액
inwon = 0 #받은금액
outwon = 0 #거슬러줄 금액

totwon = int(input("청구한 금액(원)?")) #input = 사용자의 입력값을 받음
inwon = int(input("받은 금액 입력(원)?"))

outwon = inwon - totwon
print("거스름 총 금액: %d" %outwon)

if outwon >= 50000:  #각 지폐와 동전의 수를 계산할 때, 거스름돈에서 해당 지폐와 동전의 금액을 나눈 몫(//연산자 사용) 구하기
    coin = outwon // 50000
    print("50000권: %d" % coin)
    outwon %= 50000  #남은 금액에 대해 다음 단계의 거스름 돈 계산을 수행하기 위한 코드.

if outwon >= 10000:
    coin = outwon // 10000
    print("10000권: %d" % coin)
    outwon %= 10000

if outwon >= 5000:
    coin = outwon // 5000
    print("5000권: %d" % coin)
    outwon %= 5000

if outwon >= 1000:
    coin = outwon // 1000
    print("1000권: %d" % coin)
    outwon %= 1000

if outwon >= 100:
    coin = outwon // 100
    print("100권: %d" % coin)
    outwon %= 100

if outwon >= 50:
    coin = outwon // 50
    print("50권: %d" % coin)
    outwon %= 50

if outwon >= 10:
    coin = outwon // 10
    print("10권: %d" % coin)
    outwon %= 10

if outwon >= 1:
    coin = outwon // 1
    print("1권: %d" % coin)
    outwon %= 1 

