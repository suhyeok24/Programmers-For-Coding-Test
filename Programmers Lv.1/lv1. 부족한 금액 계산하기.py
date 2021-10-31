# 나의 풀이(range를 곁들인)
def solution(price, money, count):
    total = price * sum(range(count+1))
    if total >= money:
        return total - money
    return 0

# max를 활용하여 return문을 깔끔하게
def solution(price, money, count): 
    total = price * sum(range(count+1))
    return max(total - money,0)

#두 변수간의 대소관계에 따른 조건문은 max로 대체할 수 있다!! 중요.

# p.s  sum(range()) 를 등차수열 공식으로 대체
def solution(price, money, count):
    total = price * count * (count+1) / 2
    return max(total - money,0)