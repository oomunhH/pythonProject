input = "hello my name is sparta"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if i.isalpha():
            num=ord(i)-ord('a')
            alphabet_occurrence_array[num]+=1

    return alphabet_occurrence_array

def find_max_index(arr):
    max_index=0
    for i in range(len(arr)):
        if arr[i]>=arr[max_index]:
            max_index=i
    return max_index

def find_max_occurred_alphabet(string):
    arr=find_alphabet_occurrence_array(string)
    print("빈도 배열:")
    print(arr)
    max_index=find_max_index(arr)
    print("최빈값이 있는 알파벳 위치의 index값")
    print(max_index)
    ascii_num=ord('a')+max_index
    frequent_alphabet=chr(ascii_num)

    return frequent_alphabet


result = find_max_occurred_alphabet(input)
print(result)

print("두번째 방법")
def find_max_occured_alphabet2(string):
    max_ocuurence=0
    alphabet_arr=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    max_alphabet="z"
    for i in alphabet_arr:
        occurence=0
        for char in string:
            if char==i:
                occurence+=1
        if occurence>max_ocuurence:
            max_ocuurence=occurence
            max_alphabet=char
    return max_alphabet

result2 = find_max_occured_alphabet2(input)
print(result2)