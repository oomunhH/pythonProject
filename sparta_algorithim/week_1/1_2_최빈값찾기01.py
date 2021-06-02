input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        array_index=ord(char)-ord('a')
        alphabet_occurence_array[array_index] +=1
    max=alphabet_occurence_array[0]
    for num in alphabet_occurence_array:
        if num>=max:
            max=num
            
    return "a"


result = find_max_occurred_alphabet(input)
print(result)