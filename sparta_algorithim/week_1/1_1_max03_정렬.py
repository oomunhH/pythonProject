input = [3, 5, 6, 1, 2, 4]
# 3.정렬
def find_max_num3(array):
    array.sort(reverse=True)
    print(array)
    return array[0]


result3 = find_max_num3(input)
print(result3)