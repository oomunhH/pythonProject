number=[55,34,81,33,28,46,70,49,14,47]
key=33
for idx,value in enumerate(number):
    if(value==key):
        print(idx)
        
idx=number.index(33)
print(idx)

lst=[8,9,13,14,2,5,60,32,33]
cnt_odd=0
cnt_even=0

for i in lst:
    if(i%2==0):
        cnt_even+=1
    else:
        cnt_odd+=1
print("짝수의 갯수는 {0}이고 홀수의 갯수는 {1}이고 총 갯수는 {2}입니다.".format(cnt_even,cnt_odd,cnt_odd+cnt_even))

cnt_four=0
val_four=[]
while True:
    value=int(input("값 입력:"))
    if value==0:
        break
    if(value%4==0):
        cnt_four+=1
        val_four.append(value)
print("입력 받은 4의 배수의 갯수는 {0} 입니다.".format(cnt_four))
print(val_four)