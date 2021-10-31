
# 내 풀이
def solution(a, b):
    answer=0
    for i,j in zip(a,b):
        answer+=i*j
    return answer

#List comprehension 이용 >> 한줄.
def solution(a, b):
    return sum([i*j for i,j in zip(a,b)])