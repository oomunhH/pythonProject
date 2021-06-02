input = [3, 5, 6, 1, 2, 4]
# 2.지정변수 지정
def find_max_num2(array):
    max=array[0]
    for i in array:
        if i>max:
            max=i
    return max


result2 = find_max_num2(input)
print(result2)

