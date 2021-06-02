lst=[3,6,9]
# for in 반복문
print("for in 반복문")
for i in lst:
    print(i)

# for range 반복문 
print("for in range")
for a in range(3,10,3):
    print(a)
    
# for if 같이
name=['강병구','김호영','김지원']
score=[70,80,90]

for i in range (3):
    if score[i]>=90:
        grade="A"
    elif score[i]>=80:
        grade="B"
    elif score[i]>=70:
        grade="C"
    else:
        grade="F"
    print("{0}학생의 점수는 {1}점이고, 등급은 {2}입니다."
          .format(name[i],score[i],grade))
    
#list와 dictionary 같이 사용
student=[
        {"이름":"강병구", '점수':70},
        {"이름":"김호영", '점수':80},
        {"이름":"김지원", '점수':90},
        {"이름":"박현우", '점수':100}]
for i in student:
    if i['점수']>=90:
        grade="A"
    elif i['점수']>=80:
        grade="B"
    elif i['점수']>=70:
        grade="C"
    else:
        grade="F"
    print("{0}학생의 점수는 {1}이고, 등급은 {2}입니다."
          .format(i["이름"],i['점수'],grade))

#난수 33 위치 찾기
# enumerate이용하고 for else문 이용(break 문을 만나지않으면 else문 실행된다.)
number=[55,34,81,33,28,46,70,49,14,47]
key=33
for idx, value in enumerate(number):
    print(idx,value)
    if value==key:
        print("{0}은 {1}번째 위치에 있습니다.".format(key,idx+1))
        break
else:
    print("{0}은 존재하지 않습니다.".format(key))

# while 특정조건을 만족할 때까지 반복한다
while True:
    score=eval(input("숫자입력:"))
    if score<0 or score>100:
        print("반복문 탈출")
        break
    if score>=90:
        print("합격입니다")
    elif score>=80:
        print("재시험 응시!")
    else:
        print("불합격입니다.")
        
