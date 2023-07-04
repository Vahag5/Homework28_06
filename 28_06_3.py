def filtr(function, ls):
    for x in ls:
        if function(x):      
            yield x


def not_even(n):
    return n % 2 != 0 

ls1 = [4, 5, 6, 1, 7, 8, 9, 10] 

for y in filtr(not_even, ls1):
    print(y)
