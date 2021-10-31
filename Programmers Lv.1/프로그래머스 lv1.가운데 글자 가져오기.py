def solution(s):
    left=0
    right=len(s)-1
    while left<right:
        left+=1
        right-=1

    return s[right:left+1]

#투 포인터 풀이! 간단하지만 시간복잡도 O(n) 입력값의 크기에 따라 노가다 업

def solution(s):
    return s[len(s) - ((len(s) // 2) + 1):(len(s) // 2) + 1]

# 그냥 /하면 소숫점 발생, 불편. // 몫을 이용해서 강제로 정수화시킴.
# len(s)은 O(1)이므로 이 알고리즘이 더 효율적
# 그리고 S[3] = S[3:4] 임을 응용해서 홀수, 짝수 구분 없앰.