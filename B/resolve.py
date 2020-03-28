def resolve():
    '''
    code here
    '''
    S = input()
    N = len(S)


    def chk_kaibun(S):
        is_kaibun = False
        center_index = (len(S)-1)//2
        if S[:center_index] == S[center_index:-1:-1]:
            is_kaibun = True
        return is_kaibun

    is_front = False
    front_string = S[:]

    if is_kaibun and is_flag:
        is_ans = True
    print('Yes') if is_ans else print('No')

if __name__ == "__main__":
    resolve()
