import random
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
randarr = ['0', '0', '0'] 
guessarr = ['0', '0', '0'] 
bcnt = 0    
randarr = random.sample(arr, 3)
print(randarr)

while True :
    guessarr = list(input(">>3자리수(001~999; esc 00) 입력: "))
    if guessarr == ['e', 's', 'c', '0', '0']:
        break
    strike = 0
    ball = 0
    
    for i in range(3):
        if guessarr[i] == randarr[i]:
            strike += 1
        elif guessarr[i] != randarr[i]:
            ball += 1
    result = "%d strike, %d ball" %(strike, ball)
    if strike == 3:
        print("성공")
        break
    elif strike > 0 or ball > 0:
        print(result)
  