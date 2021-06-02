def find_alphabet_occurence_array(string):
    alphabet_occurence_array=[0]*26
    # 0이 든 26개의 배열
    for char in string:
        if not char.isalpha():
            continue
        arr_index=ord(char)-ord("a")
        alphabet_occurence_array[arr_index]+=1

    return alphabet_occurence_array

a=find_alphabet_occurence_array("hello my name is sparta")
print(a)