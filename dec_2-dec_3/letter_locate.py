def letter_locate(str):
    result = []
    for index, letter in enumerate(str):
        result.append(index)
    return result

def letter_locate_2(str):
    result = []
    for letter in str:
        result.append(str.index(letter))
    return result

def letter_locate_3(str):
    result = []
    counter = 0
    while counter < len(str):
        result.append(counter)
        counter += 1
    return result

print(letter_locate('abcdefg'))
print(letter_locate_2('abcdefg'))
print(letter_locate_3('abcdefg'))
