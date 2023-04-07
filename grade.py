score = int(input("정수를 입력하세요: "))
grade = ' '

if score < 0 or score > 100:
    print("값이 범위(0~100)을 초과함!")
elif score >= 95:
    grade = 'A+'
elif score >= 90:
    grade = 'A'
elif score >= 85:
    grade = 'B+'
elif score >= 80:
    grade = 'B'
elif score >= 75:
    grade = 'C+'
elif score >= 70:
    grade = 'C'
elif score >= 65:
    grade = 'D+'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
    
print("등급은", grade)
    