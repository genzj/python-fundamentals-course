def fib(N):
    assert(N > 2)
    p_1 = 1
    p_2 = 1
    cnt = 2
    print(p_1)
    print(p_2)
    while cnt < N:
        p = p_1 + p_2
        print(p)
        p_2 = p_1
        p_1 = p
        cnt += 1

fib(10)
