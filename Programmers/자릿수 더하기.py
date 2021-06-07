#일반 for문

def solution(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum

#map을 이용한 한줄풀이
def solution(n):
    return sum(list(map(int,str(n))))


#재귀를 이용한 풀이 .. -대박

def solution(n):
    if n<10:
        return n
    return (n%10) + solution(n//10)

# ex) solution(112) = solution (11) + (solution(2)=2)
# ex) solution (1112) = solution(111) + (solution(2)=2)
# 즉 아무리 큰 수라도 인수의 끝자리를 계속 절삭할 수 있고, 결국 재귀를 돌리면 모두 일의자리 인수의
#   합으로 귀결됨