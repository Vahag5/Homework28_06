def enumerate1(ls, start = 0):
    s = start
    for i in ls:
        yield s, i
        s +=1

ls1 = ['banan', 'apple', 'watermelon']
for index, mirg in enumerate1(ls1,start = 1):
    print (f'{index}-{mirg}')

