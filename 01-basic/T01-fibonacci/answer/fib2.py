def fib(N):
    assert(N > 2)
    p_1, p_2 = 1, 1
    print(p_1)
    print(p_2)
    for i in range(2, N):
        p_1, p_2 = p_1+p_2, p_1
        print(p_1)

fib(10)
