# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

def pisano(n):
    f0=0
    f1=1
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        # Pissano period of 10 is 60
        rem=n%60
        if(rem==0):
            return 0
        for i in range(2,n+3):
            f=(f1+f0)%60
            f0=f1
            f1=f
        return f1%10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    a=pisano(n)
    b=pisano(n+1)
    return a*b


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))