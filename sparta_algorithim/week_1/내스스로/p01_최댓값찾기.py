input = [3, 5, 6, 1, 2, 4]


def find_max_num(arr):
    max_num=arr[0]
    for i in arr:
        if i>=max_num:
            max_num=i
    return max_num

def find_max_num2(arr):
    for num in range(len(arr)):
        for compare_num in range(len(arr)):
            if arr[compare_num]>arr[num]:
                break
        else:
            return arr[num]

result = find_max_num(input)
result2 = find_max_num2(input)

print(result)
print(result2)