def test(a=2, b=True):
    print(a,b)

test(False, 'ok')
test(*[1,2])