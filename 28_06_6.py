def counter():
    x = kacnhi_qanak = 0
    def inner():
        nonlocal  x
        x += 1
        return x
    return inner
my_counter = counter()
print(my_counter())  #1
print(my_counter())  #2   
print(my_counter())  #3
print(my_counter())  #4
