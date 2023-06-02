members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
          ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))

def Bi_search(search, members, start, end):
    global rcnt
    rcnt += 1
    mid = (start + end) // 2  # 가운데 항목을 첫 번째 검색 위치로 설정
    if search == members[mid][0]:  # 찾는 아이디가 있으면 점수를 저장하고 반복 종료
        number = members[mid][1]
        return number, mid
    else:
        if start == (end - 1): # 검색 범위를 줄일 수 없음(=찾는 값이 없음)
            return -1, -1
        elif search > members[mid][0]:
            start = mid + 1   # 검색 범위를 뒤쪽 반으로 줄이기
            return Bi_search(search, members, start, end)
        else:
            end = mid  # 검색 범위를 앞쪽 반으로 줄이기
            return Bi_search(search, members, start, end)

search = input("아이디 입력 : ")
number = 0     # 만족도 점수의 초기화
index = -1
start = 0       # 범위의 시작과 마지막 설정
rcnt = 0
end = len(members)   #index 값이므로 -1
number, index = Bi_search(search, members, start, end)

if number != -1:
    print(">>Index : %3d, Value : %s" %(index, search))
    print(">>Count of search : %d" % rcnt)
else:
    print("Not found!")
