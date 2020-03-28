def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    res = N*(N-1)//2 + M*(M-1)//2
    print(res)



if __name__ == "__main__":
    resolve()
