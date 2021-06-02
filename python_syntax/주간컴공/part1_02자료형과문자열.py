# 자료형 : 데이터를 담는 형태 (공간의 형태를 정해놓음)
# 키워드(예약어) : 파이썬을 사용하기 위해서 사용해둔 식별자
# 식별자 : 대소문자 구문, 빈칸 x, _사용가능,  숫자가능(첫번째는 x)
# 식별자 유형 : CamelCase, snake_case(변수,함수명 권장)
# 변수 : 변수명=값 (왼쪽 : 공간, 오른쪽 : 값)

# 1.a와 b에 각각 10, 20이 정의됨
a,b=10,20
print(a,b)
# 2.a와 b의 값을 서로 바꿈
a,b=b,a
print(a,b)
# # 3.a와 b에 30을 정의
# a=b=30
# print(a,b)


# 산술연산자 (plus, minus, multiply, power, div, div2(정수로나오는버림))
# 나누기 연산자는 결과가 실수로 나옴(float) 
# : 결과가 정수가 나와도 ex 결과값 5 => 5.0
plus=2+3
minus=10-2.0
multi=5*3.0
power=2**4
div=10/2
div2=10//2
print(plus)
print(minus)
print(multi)
print(power)
print(div)
print(div2)
print(type(plus))
print(type(minus))
print(type(multi))
print(type(power))
print(type(div))
print(type(div2))

# 복합대입연산자
val=5
val+=10 #val=val+10
val-=10 #val=val-10
val**=10 #val=val**10
val%=10 #val=val%10
val<<=10 #val=val<<10
val^=10 #val=val^10

# 슬라이싱, 
s="860908-1234567"
y=s[0:2]
m=s[2:4]
d=s[4:6]
print(s)
print(y)
print(m)
print(d)
# format함수({값순서대로 인덱스 주기}), format정의한것.format(값1,값2,값3)
f_string="19{0}년 {1}월 {2}일"
print(f_string.format(y,m,d))

# 문자열 종합 활용
f_str="식:{0}={1}, 타입:{2}"
res_1,res_2=2+3,10-2.0
exp_1,exp_2="2+3","10-2.0"
type_1=str(type(res_1))[8:-2]
type_2=str(type(res_2))[8:-2]
print(f_str.format(exp_1,res_1,type_1))
print(f_str.format(exp_2,res_2,type_2))
