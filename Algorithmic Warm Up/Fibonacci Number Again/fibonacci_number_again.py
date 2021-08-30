# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def pisano(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def fibonacci_number_again(m, n):
    assert 0 <= m <= 10 ** 18 and 2 <= n <= 10 ** 3


    p=pisano(n)
    m=m%p
    l=[0 for i in range(0,m+2)]
    l[0]=0
    l[1]=1
    for i in range(2,m+1):
        l[i]=(l[i-1]+l[i-2])%n
    return(l[m])



if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
