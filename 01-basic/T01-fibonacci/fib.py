def fib(N): # defines function "fib" with inpara "N"
    assert(N > 2)
    # p_1, p_2 = 1, 1
    p_1 =1
    p_2 =1
    print(p_1)
    print(p_2)
    for _ in range(2, N):    # starts a while loop till "cnt" hits "N"
        p_1, p_2 = p_1 + p_2, p_1
        print(p_1)

fib(10)

