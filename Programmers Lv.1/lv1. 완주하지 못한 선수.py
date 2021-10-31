from collections import Counter (시간복잡도: O(n))
def solution(participant, completion):
    par = Counter(participant)
    com = Counter(completion)
    for key in par.keys(): # 두가지 조건
        if key not in com:  # 1. key가 없을때, 선수가 동명이인이 없는데 그대로 완주 실패
            return key
        if par[key]!=com[key]: # 2. key가 있는데, key값이 다를 때(동명이인이 완주 실패)
            return key
# Collections-Counter를 활용한 내 풀이


# 딕셔너리의 성질을 극한으로 ..
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion) # 카운터 객체는 뺄셈이 가능하다..지렷다.
    return list(answer.keys())[0] # key 자체 리턴은 a.keys() 이용 >> dict 내 모든 key 리턴
                                  # but list로 리턴되는 것이 아닌 dict_keys 객체로 리턴
                                  # list(a.keys())로 해야 list로 리턴됨, 인덱스 조회 가능.
                                  # 완주 못한 사람은 한명이므로 리스트 요소는 한개


# sort 정렬을 이용한 for문 풀이 - 나름 깔끔( 빅오: O(n log n))
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]: # for문을 돌렸을때 다른 부분 나오면 바로 컽
            return participant[i]
    return participant[-1] # 다 같으면 결국 남은 참가자가 return(마지막 1명)