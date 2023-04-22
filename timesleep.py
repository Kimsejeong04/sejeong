import time
str = "python programming"
slen = len(str)

for s in range(0, slen):
    for i in range(s, slen, 1):
        print("%c" %str[i], end='')
    time.sleep(0.5)
    for i in range(s, slen):
        print("\b", end='')