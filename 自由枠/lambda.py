def loop(func):
    for i in range(10):
        print(func(i))

# def square(num):
#     return num * num

# def add(num):
#     return num + num

loop(lambda num : num + num)