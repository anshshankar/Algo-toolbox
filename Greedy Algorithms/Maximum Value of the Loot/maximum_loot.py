# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    l=[]
    for i in range(len(weights)):
        l.append([weights[i],prices[i],prices[i]/weights[i]])
    l.sort(key = lambda x: x[2],reverse=True)
    p=0
    pro=0
    while(True):
        # print("ok")
        if(capacity>l[pro][0]):
            capacity-=l[pro][0]
            p+=l[pro][1]
            pro+=1
            if(l[pro-1]==l[-1]):
                return p

        # print(capacity,l[pro][2],l[pro][1],l[pro][0])

        if(capacity<=l[pro][0]):
            p+=capacity*l[pro][2]
            capacity=0
            # print(p)
            return p
            break




if __name__ == "__main__":

    n,cap=map(int,input().split())
    weight=[]
    prices=[]
    for i in range(n):
        p,w=map(int,input().split())
        weight.append(w)
        prices.append(p)
    m=maximum_loot_value(cap,weight,prices)
    print(format(m,".4f"))










    # data = list(map(int, stdin.read().split()))
    # n, input_capacity = data[0:2]
    # input_prices = data[2:(2 * n + 2):2]
    # input_weights = data[3:(2 * n + 2):2]
    # opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    # print("{:.10f}".format(opt_value))
