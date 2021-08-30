# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    cr,nr,lr=0,0,0
    stops.insert(0,0)
    n=len(stops)-1
    if(d-stops[-1]>m):
        return -1
    if(d<=m):
        return 0
    while(cr<=n):
        while(cr<n and stops[cr+1]-stops[lr]<=m):
            cr+=1
        if(cr==lr):
            return -1
        lr=cr
        if(cr<=n):
            nr+=1
        if(d-stops[lr]<=m):
            return nr

        if(cr==n):
            if(d-stops[lr]>m):
                nr+=1
            return nr


import random

if __name__ == '__main__':

    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

    #
    # k=int(input())
    # if(k==1):
    #     while(True):
    #         input_d=random.randint(1,10**3)
    #         input_m=random.randint(1,400)
    #         input_n=random.randint(1,10)
    #         input_stops=random.sample(range(1,input_d-1),input_n)
    #         input_stops.sort()
    #         assert len(input_stops) == input_n
    #         print(input_d)
    #         print(input_m)
    #         print(input_n)
    #         print(*input_stops)
    #         print(compute_min_number_of_refills(input_d, input_m, input_stops))
    #
    #
    #
    # if(k==2):
    #     input_d = int(input())
    #     input_m = int(input())
    #     input_n = int(input())
    #     input_stops = list(map(int, input().split()))
    #     assert len(input_stops) == input_n
    #
    #     print(compute_min_number_of_refills(input_d, input_m, input_stops))
