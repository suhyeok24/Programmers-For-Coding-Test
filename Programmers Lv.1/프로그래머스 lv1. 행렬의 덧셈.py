def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        answer.append(list(map(sum,zip(arr1[i],arr2[i]))))
    print(list(map(sum,zip(*arr1,*arr2))))
    return answer

# 내 풀이- 하나의 for문 과 zip을 사용(zip은 각 iterator 의 요소들을 모으는 이터레이터를 만들어줌)


# best 풀이 1.
def solution(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

# unlist를 쓰지 말고 zip을 두번 쓰자.
# for i in zip(list1,list2)
#    print(i) 에서 출력된 i는 list1 과 list2의 첫번쨰 iterator 를 하나로 모은 형태

#for a,b in zip(list1, list2)
#   print(a,b) 에서 출력된 a,b는 각각 list1 과 list2의 첫번째 iterator 가 된다.

# 이중 리스트에서는 zip함수를 항상 생각하자.



# Numpy 이용 - 연산 시간은 그렇게 빠르지 않음. but 알고리즘 매우 간단

import numpy as np
def solution(arr1, arr2):
    a1=np.array(arr1)
    a2=np.array(arr2)
    answer = a1 + a2
    return answer.tolist()  # 마지막에 다시 리스트로 바꿔서 리턴해야함.

# list >> array : np.array(list)
# array >> list : array.tolist()
