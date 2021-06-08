def solution(n):
    if n**(1/2)==int(n**(1/2)):
        return (n**(1/2)+1)**2
    return -1
# int는 내림을 해서 정수를 만듦. 그것과 비교(내풀이)



#정수판별하는 방법 - 1로 나눈 나머지를 이용한다.. 대박 ㅋㅋ(내꺼 보다 2배가까이 빠름)
def solution(n):
    sqrt=n**(1/2)
    if not sqrt%1:
        return (sqrt+1)**2
    return -1

# # return A and B
# -A,B 둘다 참이면 B출력
# -A,B 둘다 거짓이면 A출력

# # return A or B
# -A,B 둘 중에 하나만 참이면 참인 것 출력

#여기서 중요한 것 연산은 AND >> OR 순이다.
