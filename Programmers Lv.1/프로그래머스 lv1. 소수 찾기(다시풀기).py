
# - 처음 그냥 중첩 for문 >> 이후 n/2까지만 while문 돌리기, >> 루트 n까지만 while문 돌리기해도 안됨:
import math
def solution(n):
    count=0
    for i in range(2,n+1):
        j=2
        while j <= math.sqrt(i):
            if i%j ==0: break
            j+=1
        if j == math.floor(math.sqrt(i))+1:
            count+=1
    return count

# 정확성은 통과하나 효율성 검사에서 계속 떨어짐 결국 풀이 실패

# 정답풀이- 에라토스테네스의 체를 이용
# 수를 모두 나열해놓고 2의 배수 모두 제거, 3의 배수 모두 제거,

def solution(n):
    num=set(range(2,n+1)) #중복불가능한 set을 활용

    for i in range(2,n+1):
        if i in num: # i가 num집합에 있는지 확인
            num-=set(range(2*i,n+1,i)) # i배수를 num에서 제외, 리스트는 -연산이 안되므로 set을 사용한듯(차집합 이용)
    return len(num)

#
# 단일 숫자 소수 여부 확인
# 어떤 수의 소수의 여부를 확인 할 때는, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.
# 수가 수(N이라고 가정)를 나누면 몫이 생기는데, 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.
# 만약, 대량의 소수를 한꺼번에 판별해야할 경우는 '에라토스테네스의 체'를 이용한다.

# 출처.https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4


# 앞 풀이에서 for문의 range를(i배수의 범위를 루트n배수까지만으로 제한) >> 더욱 최적화
def solution(n):
    num=set(range(2,n+1)) #중복불가능한 set을 활용

    for i in range(2,int(n**(1/2))+1):
        if i in num: # i가 num집합에 있는지 확인
            num-=set(range(2*i,n+1,i)) #set(range(i*i,n+1,i)를 해도 더 빨라짐. i*i부터 i까지 약수임을 확인해야함
            # i배수를 num에서 제외, 리스트는 -연산이 안되므로 set을 사용한듯(차집합 이용)
    return len(num)