input = [3, 5, 6, 1, 2, 4]
# 1.이중반복문
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num<compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)

# 2.지정변수 지정
def find_max_num2(array):
    max=array[0]
    for i in array:
        if i>max:
            max=i
    return max


# 3.정렬
def find_max_num3(array):
    array.sort(reverse=True)
    print(array)
    return array[0]


result3 = find_max_num3(input)
print(result3)