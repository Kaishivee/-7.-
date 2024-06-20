def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(1, 'str'))
print(add_everything_up('str', 2.22))
print(add_everything_up(3, 5))
print(add_everything_up(4, 7.654))
