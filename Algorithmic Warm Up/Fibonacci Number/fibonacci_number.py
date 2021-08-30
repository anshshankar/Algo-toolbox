# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    l=[0 for i in range(0,n+2)]
    l[1]=1
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
    return(l[n])




if __name__ == '__main__':
    n = int(input())
    print(fibonacci_number(n))
