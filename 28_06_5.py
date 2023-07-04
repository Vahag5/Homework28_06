def map1(function, ls):
    for i in ls:
        yield i

def add_10(x):
    if isinstance(x, (int, float)):
        return x + 10
    else: 
        return ("You input is not int or float")

ls1 = [1, 5, 10]
print(tuple(map1(add_10, ls1)))


'''You input is not int or float
    15
    20                       '''

