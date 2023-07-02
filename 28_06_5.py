def map1(function, ls):
    for i in ls:
        print(function(i))

def add_10(x):
    k = 10
    y = x + 10
    return y


ls1 = [1, 5, 10]
map1(add_10, ls1)
