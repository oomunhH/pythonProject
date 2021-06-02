# 체중, 키를 저장하는 변수를 만들고 BMI를 계산하여 
# 'BMI 수치는 31.9 입니다' 형식으로 출력(체중을 키(m)의제곱으로 나눈값)
height=1.78
weight=95
bmi=weight/(height**2)
f_bmi="BMI 수치는 {0}입니다"
print(f_bmi.format(bmi))

# 근의 공식을 이용하여 방정식의 해 구하기 (루트는 **0.5)
a=4
b=-6
c=+2

x=[(-b+(b**2-4*a*c)**0.5)/2*a,(-b-(b**2-4*a*c)**0.5)/2*a]
f_result="{0}x^2{1}x{2}c의 해는 {3}"
for i in range(len(x)):
    print(f_result.format(a,b,c,x))

# 주민번호 앞자리를 문자열로 저장하는 변수를 만들고 아래와 같은 형식으로 출력
# 1992년 11월 29일
regNum="921129-1234567"
first_regNum=regNum[0:2]
second_regNum=regNum[2:4]
third_regNum=regNum[4:6]
print(first_regNum)
print(second_regNum)
print(third_regNum)
f_birth="19{0}년 {1}월 {2}일"
print(f_birth.format(first_regNum,second_regNum,third_regNum))