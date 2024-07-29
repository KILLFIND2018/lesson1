def print_params(a,b,c):
    print(a,b,c)
list = [1,2]
dict = {'c':3}
print_params(*list, **dict)