#내 풀이.

from collections import Counter

def solution(nums):
    d = Counter(nums)  #Counter라는 딕셔너리 이용, 리스트의 종류별 개수 count

    return len(d) if len(d) <= len(nums) / 2 else int(len(nums) / 2)
    # 이 말이 결국 len(D) 와 len(nums)/2 중 작은 값을 return 한다는 말 . 잘생각해서 min을 쓰자.


# 더 쉬운 풀이. 중복은 set(집합)을 먼저 생각할 것!!!! (조온나 깔끔)

def solution(nums):
    #중복은 집합입니다.. 훠훠훠
    return min(len(set(nums)),len(nums)/2)