n = int(input("층 수(0~100): ")) #input = 사용자의 입력값을 받음 n은 층수.

for i in range(1, n+1, 1): #i = 초기값 지정한 범위에서 1씩 증가.
    print(" " * (n-i) + "*" *(2*i-1)) #피라미드 형식으로 만드려면 *은 2씩 증가.    2*i(1)-1=1, 2*i(2)-1=3, 2*i(3)-1=5