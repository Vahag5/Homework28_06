def zip1(*iterables):
    iterators = list(map(iter, iterables))
    while True:
        try:
            i = list(map(next, iterators))
            yield tuple(i)
        except StopIteration:
            return

tver = [1, 2, 3]
tar = ['a', 'b', 'c']
for i in zip1(tar, tver):
    print(i)
