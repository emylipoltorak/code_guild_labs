def letter_locate(s,x):
    i_list = []
    for i,char in enumerate(s):
        if char.lower() == x.lower():
            i_list.append(i)
    if i_list:
        return i_list
    else:
        return -1

if __name__ == '__main__':
    print(letter_locate('Batteries','e'))
