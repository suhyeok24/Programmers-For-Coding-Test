
# 기본적. 범위 나누는 풀이. 큰 의미 x
def solution(a, b):
    sum=0
    if a<=b:
        for i in range(a,b+1):
            sum+=i
    else:
         for i in range(b,a+1):
            sum+=i
    return sum

#min, max 이용
def solution(a, b):
    sum=0



    for i in range(min(a,b),max(a,b)+1):
        sum+=i
    return sum

# list comprehension
def solution(a, b):
    return sum([i for i in range(min(a,b),max(a,b)+1)])

#range는 생성만 해둔것. list,sum등하면 바로 값 나옴

def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1)


# min, max 사용 안함. 변수 스왑 사용
def solution(a, b):

    if a>b: a,b = b,a   #swap 해서도 가능하다. 꼭 min max 사용안해도 됨
    return sum(range(a,b+1))