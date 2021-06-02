def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if i.isalpha():
            num=ord(i)-ord('a')
            alphabet_occurrence_array[num]+=1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))