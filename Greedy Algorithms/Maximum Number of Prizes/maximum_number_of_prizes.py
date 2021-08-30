# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    if n==2:
        return [2]
    if n==1:
        return [1]

    for i in range(1,n):
        if((i*(i+1))//2 <=n):
            summands.append(i)
            continue
        else:
            i-=1
            k=i+n-(i*(i+1))//2
            if(k in summands):
                break
            else:
                summands.pop()
                summands.append(i+n-(i*(i+1))//2)
                break


    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
