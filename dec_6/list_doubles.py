#for loop solution
def list_doubles_1(lst,n):
    return_list = []
    for x in lst:
        if x*n:
            return_list.append(x*n)
        else:
            continue
    return return_list

#list comprehensions
def list_doubles_2(lst,n):
    return [x*n for x in lst if x*n]


if __name__ == '__main__':
    print(list_doubles_1([1,2,0,4,5],2))
    print(list_doubles_2([1,2,0,4,5],2))
