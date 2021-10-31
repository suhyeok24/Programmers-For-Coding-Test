# 간단하게 list comprehension 이용 >> but error , x=0 일때 처리 해주어야 함.
def solution(x, n):
    return [ i for i in range(x,x*n+int(x/abs(x)),x)]



# 내 풀이: x가 0일때는 예외처리해주어야함.
def solution(x, n):
    if not x:
        return [0]*n    # range(a,b,c) 중 c 즉, 3번째 argument는 0이 될 수 없다.!!!! 중요.
    return list(range(x,x*n+int(x/abs(x)),x))   # range의 2번쨰 argument를 x*(n+1)로 해도 되지만
                                                # 극한의 효율을 뽑기 위해 int(x/abs(x))를 사용함(양수:1, 음수:-1)

# 입력값에 대한 검증, 예외 처리(0이거나 null일때) 를 확실히 하자. 가장 실수하기 쉬운 부분이다.


# 마지막 try, except 예외처리 구문을 이용한 풀이
def solution(x, n):
    try:
        return list(range(x,x*n+int(x/abs(x)),x))
    except:
        return [0]*n

