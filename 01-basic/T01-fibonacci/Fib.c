#include <stdio.h>
#include <assert.h>

void fib(int N)
{
    int p_1 = 1, p_2 = 1, p, cnt;
    assert(N>2);
    printf("%d\n%d\n", p_1, p_2);
    cnt = 2;
    while (cnt < N) {
        p = p_1 + p_2;
        p_2 = p_1;
        p_1 = p;
        printf("%d\n", p);
        ++cnt;
    }
}

int main(int argc, char* argv[])
{
    fib(10);
    getc(stdin);
    return 0;
}
