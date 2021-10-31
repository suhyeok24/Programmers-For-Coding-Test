#내 풀이

import numpy as np


def solution(scores):
    # 1. 각각의 학생이 받은 점수 번호별로 리스트화
    scores = np.array(scores)
    s = []
    print(scores)
    for i in range(len(scores)):
        s.append(scores[:, i])

    print(s)
    s = np.array(s)
    s = s.tolist()
# ---------------------------------------------------------------------------------------------


    #1번이 좀 삽질이라 이렇게 해볼수 있음(결국 transposing이 목적)
    #numpy 사용 안해도 됨.
    scores = list(map(list,zip(*scores)))  #unpacking을 이용하면 된다.

    #numpy 사용할거면
    # import numpy as np
    # scores=np.array(scores)
    # scores.T하면 바로 if Transposing됨;; easy
    # 이후 .tolist()로 리스트화
# ------------------------------------------------------------------------------------------------
    # 2. 평군구하고 학점 부여하기
    a = []
    for i in range(len(s)):  # for i,n in enumerate(s):  대체 가능
        key = s[i][i]        # key=n[i]
        if key == max(s[i]) or key == min(s[i]):  # 최고 or 최저
            if s[i].count(key) == 1:  # 유일하면
                s[i].remove(key)
        a.append(sum(s[i]) / len(s[i]))

    print(a)

    answer = ""
    for i in a:
        if i >= 90:
            answer += "A"
        elif i >= 80:
            answer += "B"
        elif i >= 70:
            answer += "C"
        elif i >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer