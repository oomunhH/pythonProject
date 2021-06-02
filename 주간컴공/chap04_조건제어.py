value=int(input("값 입력:"))
if value<0:
    print("오류")

print("점수 입력")
score1=int(input("과목1:"))
score2=int(input("과목2:"))
score3=int(input("과목3:"))
scores=[score1,score2,score3]
if sum(scores)/3>=60 and not(min(scores)<40):
    print("합격")
else:
    print("불합격")
    
val1=int(input("num1:"))
val2=int(input("num2:"))

if max(val1,val2)-min(val1,val2)>=20:
    print("편차큼")