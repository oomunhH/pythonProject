def rep_prt(str,rep_cnt):
    print((str+"\n")*rep_cnt)

rep_prt("구독과 좋아요",2)
rep_prt("댓글과 광고시청!",3)


def sample2(val1,val2):
    if val1<0 and val2<0:
        return
    elif val1*val2<=0:
        a=max(val1,val2)
        b=min(val1,val2)*-1
        print(abs(a-b))


sample2(1,-2)
sample2(-1,-2)
sample2(10,-2)

def find_max_num():
    num_arr=[]
    for i in range(5):
        input_val=eval(input(str((i+1))+"/5번째 입력:"))
        num_arr.append(input_val)
    print(max(num_arr))

find_max_num()

def find_complete_num(end_num):
    perfect_cnt=0
    perfect_nums=[]
    for i in range(1,end_num+1):
        x_total=0
        for x in range(1,i):
            if i%x==0:
                x_total+=x
        if x_total==i:
            perfect_cnt+=1
            perfect_nums.append(i)
    print(perfect_nums)
    print("완전수의 갯수는 {0}".format(perfect_cnt))

find_complete_num(10000)

def circle_circumference_area(radius):
    circumference=2*radius*3.14
    area=radius**2*3.14
    print("원둘레는 {0}".format(circumference))
    print("원넓이는 {0}".format(area))

circle_circumference_area(14)

def find_first_num(num):
    return num%10

def sum_three_numbers(num1,num2,num3):
    val1=find_first_num(num1*2)
    val2=find_first_num(num2*3)
    val3=find_first_num(num3*4)
    result=val1+val2+val3
    return result

print(sum_three_numbers(53,45,24))
