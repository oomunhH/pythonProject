# 가변적 시퀀스: 리스트 
# (다른종류의 데이터 타입도 넣을 수 있다)
# 리스트안에 또다른 리스트, 인덱싱 가능

name="파이썬"
score=[30,40,50]
phone="010-3921-1294"

# 한식 일식 중식 리스트 생성후 이 배열을 담는 리스트를 만든다
# 리스트 (append(), remove(), pop(), del, index(), insert(), sort() 메서드 이용)
k_food=[]
j_food=[]
c_food=[]
food=[k_food,j_food,c_food]
# append() 리스트에 요소 추가(맨끝에)
k_food.append("라면")
j_food.append("초밥")
c_food.append("자장면")
print(food)
# del 문, del 문은 슬라이싱을 통해 삭제도 가능 del food[1:3] or pop()
del food[1]
i_food=["피자"]
food.append(i_food)
print(food)
# 마라탕을 한국음식을 추가 했을 때, 마라탕 삭제하고 중국음식에 추가
# remove(값) 이용
k_food.append("불고기")
k_food.append("마라탕")
k_food.append("설렁탕")
k_food.append("제육볶음")
i_food.append("파스타")
c_food.append("멘보샤")
print(food)
k_food.remove("마라탕")
c_food.append("마라탕")

idx=k_food.index("라면")
tmp=k_food.pop(idx)
k_food.insert(idx,"육개장")

# 불변형 시퀀스 : 문자열, 튜플, range
# 튜플 ()로 생성, 두 개 이상이면 괄호 없이 사용가능

rainbow=("빨","주","노","초","파","남","남")
print(rainbow[1])

# range 함수
# 0~ 10전까지
r1=range(10)
# 1~11전까지 1씩 증가
r2=range(1,11,1)
# 0~30전까지 5씩 증가
r3=range(0,31,5)

# 딕셔너리
# {키:값} 딕셔너리명["키"]="값"
# 딕셔너리.keys(), 딕셔너리.values(), 딕셔너리.items()


