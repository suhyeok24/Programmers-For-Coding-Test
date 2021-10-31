#내 풀이
def solution(n):
    return min([(n-1)/a for a in range(1,n-1) if (n-1) % a ==0])

#걍 이런문제는 문제 그대로 하면 됨. 수학적으로 생각할 필요 없다... ㅈㅅ

def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer