def credit_card_validation(card_number):
    card_number_list = []
    for num in card_number.replace(' ',''):
        card_number_list.append(int(num))
    check_digit = card_number_list.pop()
    card_number_list.reverse()
    card_number_list[::2] = [num*2 for num in card_number_list[::2]]
    sum_list = []
    for num in card_number_list:
        if num>9:
            sum_list.append(num-9)
        else:
            sum_list.append(num)
    return str(sum(sum_list))[1]==str(check_digit)

print(credit_card_validation('4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5'))
