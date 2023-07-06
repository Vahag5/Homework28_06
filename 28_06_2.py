def zip1(*iterables):
    iterators = list(map(iter, iterables))
    while True:
        try:
            x = list(map(next, iterators))
            yield tuple(x)
        except StopIteration:
            return

tver = [1, 2, 3]
tar = ['a', 'b', 'c']
for i in zip1(tar, tver):
    print(i)
