#내 풀이

from itertools import combinations  #combinations 이용하기 itertools!!!!

def solution(nums):
    sett = list(map(sum, combinations(nums, 3)))  # 각 list 안 combinations의 묶음은 튜플로 묶여짐.
                                                  # combinations 앞 list는 생략 가능 (range느낌으로 생성된것)
    sett2 = sett[:]  #sett의 사본

    for i in sett:
        for j in range(2, int(i ** (1 / 2)) + 1): #소수판별은 2부터 루트 n까지.
            if i % j == 0:
                sett2.remove(i) #sett에서 바로 remove를 하면 for문에 영향을 주므로 사본에서 제거.
                break

    return len(sett2)

# 이렇게도 가능하다!

from itertools import combinations


def solution(nums):
    sett = list(map(sum, list(combinations(nums, 3))))  # 각 묶음은 튜플로 묶여짐.

    answer = 0

    for i in sett:
        for j in range(2, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                break
        else:
            answer += 1
    # else문을 for문과 같은 줄에 쓰게되면, for문의 반복이 끝나고나서 else문이 실행되게 됩니다(break로 빠져나가지 않는다면)
    # 개꿀팁! 정상적으로 끝낸 for문과 break를 통해 빠져나간 for문을 else문으로 구별가능하다.
    return answer