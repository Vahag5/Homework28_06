def filtr(function, ls):
    filtr_result = []
    for x in ls:
        if function(x):
            filtr_result.append(x)       
    yield filtr_result


def not_even(n):
    return n % 2 != 0 

ls1 = [4, 5, 6, 1, 7, 8, 9, 10] 
print(list(filtr(not_even, ls1)))
