num=eval(input("정수 입력:"))
for i in range(1,num+1,1):#,1은 생략가능
    print(i)
    
lst=[8,9,13,14,2,5,60,32,33]
cnt_even=0  #짝수 갯수
cnt_odd=0   #홀수 갯수
for i in lst:
    if i%2==0:
        cnt_even+=1
    else:
        cnt_odd+=1
print("리스트안의 숫자 중 짝수의 갯수는 {0}개, 홀수의 갯수는 {1}개 입니다"
      .format(cnt_even,cnt_odd))

num2=int(input())
cnt_4multi=0 #4의 배수 갯수
lst4=[] #4의 배수를 담을 리스트
while True:
    num2=int(input())
  
    if num2%4==0 and num2!=0:
        cnt_4multi+=1
        lst4.append(num2)
    if num2==0:
        print("4의 배수 갯수는 {0}개 이고, 입력된 값은 {1} 입니다."
              .format(cnt_4multi,lst4))
        break    
# 구구단
num3=int(input())
for i in range(1,10):
    print("{0}x{1}={2}".format(num3,i,(num3*i)))
    
    