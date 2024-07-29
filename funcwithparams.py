def func_with_params(a, b = 3, c = None):
    if c is None:
        c = []
        c.append(a)
    print(c)
func_with_params(6)
func_with_params(2)