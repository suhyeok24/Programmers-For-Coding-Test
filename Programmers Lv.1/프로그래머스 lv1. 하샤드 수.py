def solution(x):
    return not x%(sum(list(map(int,str(x)))))
%timeit solution(19238)

#map 이용


def solution(x):
    return not x%(sum([int(i) for i in str(x)]))
%timeit solution(19238)

#list comprhension 이용

# 모두 내 풀이 ㅎ