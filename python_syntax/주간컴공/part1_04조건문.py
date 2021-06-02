math=eval(input("수학점수:"))
print(math)
if math>=70:
    print("합격입니다")
else:
    print("불합격입니다")

    

absence=eval(input("결석횟수:"))
print(absence)
if absence==0:
    print("결석횟수가 0번 입니다.")
elif absence>3:
    print("출석수를 만족하지 못 했습니다.")
else:
    print("출석수를 만족하였습니다.")