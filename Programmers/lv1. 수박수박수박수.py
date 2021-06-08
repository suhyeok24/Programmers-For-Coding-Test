# 내 풀이- 남는 메모리 없음
def solution(n):
    return "수박"* int(n/2) + "수" * (n%2)

# 그냥 s라는 긴 문자열을 만들어놓고, 리스트 슬라이싱, 식은 간단하나 잉여메모리 발생
def solution(n):
    s="수박"*(int(n/2)+1)
    return s[:n]
