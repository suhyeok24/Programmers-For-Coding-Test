def solution(numbers, hand):
    answer = ''

    L = "*"
    R = "#"
    L_Dis = 0
    R_Dis = 0

    for n in numbers:

        if n == 1 or n == 4 or n == 7:
            L = n
            answer += "L"

        elif n == 3 or n == 6 or n == 9:
            R = n
            answer += "R"

        else:
            if n == 0:  # 0을 11이라고 정의 > 계산 용이
                n = 11

            if L == "*":  # "*"을 10으로 정의
                L = 10

            if R == "#":  # "#"을 12로 정의
                R = 12

            # 거리설정 > 키패드 전체 -1 을 해서 012/345/678/91011 만듦.
            # 이후 3으로 나눈 몫, 나머지(divmod)를 담은 튜플을 좌표로 설정 (x좌표, y좌표)
            # 대각선 방향 이동이 안되므로 |x1-x2|+|y1-y2| 를 zip,list comprehension을 이용해 구현

            L_Dis = sum([abs(i - j) for i, j in zip(divmod(n - 1, 3), divmod(L - 1, 3))])
            R_Dis = sum([abs(i - j) for i, j in zip(divmod(n - 1, 3), divmod(R - 1, 3))])

            # 1. 예외: 거리계산 필요 X (L="*",R="#" 초기값에서 시작)
            if L == "*" and R == "#":

                if hand == "left":
                    L = n
                    answer += "L"
                else:
                    R = n
                    answer += "R"

            # 2. 일반적 거리계산 case
            elif L_Dis < R_Dis:
                L = n
                answer += "L"

            elif R_Dis < L_Dis:
                R = n
                answer += "R"

            else:
                if hand == "left":
                    L = n
                    answer += "L"
                else:
                    R = n
                    answer += "R"

    return answer