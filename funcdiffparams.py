def my_sum(n, *args, text = "Sum number:"):
    s = 0
    # цикл повторяется до конца длины введенных параметров
    for i in range(len(args)):
        #брать числа введеные через параметр и повзести в степернь n
        s += args[i] ** n
    print(text + ":" , s)

my_sum(1,222,236,258)
my_sum(2, 144,125, text = "сумма квадратов")