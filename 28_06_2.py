def zip1(*iters):
    minlen = min(len(i) for i in iters)  
    for x in range(minlen):
        yield tuple(i[x] for i in iters)

tver = [1, 2, 3, 4, 5]
tar = ['a', 'b', 'c', 'd']
for i in zip1(tver, tar):
    print(i)


'''(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')'''
