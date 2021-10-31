import re


def solution(dartResult):
    num = []
    op = []  # 2차원 리스트

    n = re.split('[^0-9]', dartResult)  # 리스트 형태

    for i in n:
        if i:  # 공백이 아닌 것
            num.append(int(i))

    b = re.sub('[^a-zA-Z]', '', dartResult)  # 문자열 형태

    bonus = list(b)

    o = re.split('[0-9]', dartResult)  # 맨앞에 공백이 하나 생김

    for index, j in enumerate(o):
        if len(j) == 2:
            op.append([j[1], index - 1])
    while len(op) != 3:
        op.append([])

    print(num, bonus, op)

    answer = []

    for index, j in enumerate(zip(num, bonus)):
        a = 0
        print(index, j)

        # num, bonus 계산
        if j[1] == "S":
            a += j[0] ** 1
        if j[1] == "D":
            a += j[0] ** 2
        if j[1] == "T":
            a += j[0] ** 3

        answer.append(a)

    # 옵션 따로 계산
    for k in op:
        if len(k) == 2:
            if k[0] == "*":
                answer[k[1]] = answer[k[1]] * 2  # k[1]이 인덱스 넘버.
                if k[1] - 1 >= 0:  # 5번 조건
                    answer[k[1] - 1] = answer[k[1] - 1] * 2
            else:
                answer[k[1]] = answer[k[1]] * (-1)

    return sum(answer)

#정규표현식을 이용한 좋은 풀이

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1} #없을때도 '':1 이라고 dict에 넣음
    p = re.compile('(\d+)([SDT])([*#]?)')  #\d+: 숫자가 한번이상 반복(10점떄매 이상을 붙인듯)
    # [SDT]: "S, D, T 중 한 개의 문자와 매치 , [*#]?: *,# 중 하나 매치 + ?(있어도 되고 없어도 됨) 즉 없을 수도 있음.
    # 없을떄는 "" 공백으로 반환 >> 이게 중요함.. ㄹㅇ
    # re.compile을 함으로써 패턴 객체가 생성
    dart = p.findall(dartResult) # findall:  패턴과 일치하는 모든 문자열을 리스트로 리턴
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] #i=0일때는 if skip이므로 변수정의가
        #무조건 되어잇음.
        #이렇게도 변수 정의가 가능하다..(원래는 튜플 그 자체인데 덮어 씌우기)

    answer = sum(dart)
    return answer