# 가장 흔한 for문
def solution(arr, divisor):
    answer = []
    for n in arr:
        if n % divisor == 0:
            answer.append(n)

    if not answer:
        return [-1]
    else:
        return sorted(answer)


# lIST COMPRHENSION 이용
def solution(arr, divisor):
    return sorted([ num for num in arr if num % divisor == 0]) or [-1]

# sorted([]) = [] 은 boolean으로 FaLSE 이므로 [-1]이 대신 리턴된다.

# return에 관하여 한말씀 올리면
# return A or B 일때 A,B가 둘다 참이면, A가 return됨(가장 첫번쨰 값)
# but A 와 B 중에 none, empty 값(boolean이 False)이 있으면 그 값을 제외한 True 값이 리턴됨
# 즉, 하나만 참이면 그 참인 값이 리턴.





#파이썬에서는 괄호 없이 값을 콤마로 구분하면 튜플이 된다.
# ex) 1,2 = (1,2)