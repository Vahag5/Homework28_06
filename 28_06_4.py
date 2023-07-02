def enumerate1(ls, start = 0):
    en_result = []
    for i in range(len(ls)):
        x = ls[i]
        tp = (start + i, x)
        en_result.append(tp)
    return en_result


ls1 = ['banan', 'apple', 'watermelon']
enumerated_list = enumerate1 (ls1, start = 0)
for tp in enumerated_list:
        print(tp)