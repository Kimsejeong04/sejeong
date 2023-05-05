book = ' '
bookList = []
number = 0

print("입력을 종료하려면 [Enter] 키를 누르세요.")
print('=' * 30)

while True:
    book = input("도서명 입력: ")
    if book == '':
        break
    bookList.append(book)

bookList.sort()

print('=' * 30)
for b in bookList:
    number += 1
    print(number, ':', b)