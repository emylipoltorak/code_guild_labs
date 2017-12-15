import math

"""
>>> make_change(94)
3 quarters
1 dimes
1 nickels
4 pennies
>>> make_change(75)
3 quarters
>>> make_change(42)
1 quarters
1 dimes
1 nickels
2 pennies
"""

def make_change(ch, d_in_stock=float('inf'), q_in_stock=float('inf'), di_in_stock=float('inf'), n_in_stock=float('inf'), p_in_stock=float('inf')):
    try:
        ch = int(ch)
    except ValueError:
        return 'Please enter a number of cents.'
    d,q,di,n,p = 0,0,0,0,0
    while True:
        if ch >= 100:
            d += int(evaluate_denomination('d', d_in_stock, ch)[0])
            ch = int(evaluate_denominantion('d', d_in_stock, ch)[1])
        elif ch >= 25:
            q += ch // 25
            ch = ch % 25
        elif ch < 25 and ch >= 10:
            di += ch // 10
            ch = ch % 10
        elif ch < 10 and ch >= 5:
            n += ch // 5
            ch = ch % 5
        elif ch < 5 and ch >= 1:
            p += ch
            break
        else:
            break
    # return '{} quarters\n{} dimes\n{} nickels\n{} pennies'.format(q,d,n,p)
    if d:
        print('{} dollars'.format(d))
    if q:
        print('{} quarters'.format(q))
    if di:
        print('{} dimes'.format(di))
    if n:
        print('{} nickels'.format(n))
    if p:
        print('{} pennies'.format(p))

def evaluate_denomination(denomination,in_stock, ch):
    denomination_value = {'d':100, 'q':25, 'di':10, 'n':5, 'p':1}
    if ch // denomination_value[denomination] <= in_stock:
        denomination += ch // denomination_value[denomination]
        ch %= denomination_value[denomination]
    else:
        return 'o no borkd'

    return [denomination, ch]


# {'tw':2000, 'te':1000, 'f':500, }

if __name__ == '__main__':
    print(make_change('332'))
