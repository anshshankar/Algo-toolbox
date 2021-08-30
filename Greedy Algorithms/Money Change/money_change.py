# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    m=money
    d=0
    d=m//10
    m=m%10
    d+=m//5
    m=m%5
    d+=m//1
    return d


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
