# 내풀이. 3진법 구하는 함수를 새로 만들었음. 좀 더러움.
def three(n):
    s = 1
    count = 0
    while s <= n:
        s = s * 3
        count += 1

    num = ""

    for i in range(count - 1, -1, -1):
        a = str(n // (3 ** i))  # a=divmod(n,3**i)[0]
        num += a  # n=divmod(n,3**i)[1]

        n -= int(a) * (3 ** i)

    return num


def solution(n):
    return sum([int(n) * (3 ** i) for i, n in enumerate(three(n))])


# 나머지정리 이용한 훌륭한 풀이.(다른풀이)
def solution(n):
    # 함수 안만들고 바로 앞뒤반전 3진법을 만들기.
    tmp = ""
    # 개수가 정해져있지 않을때는 while(3진법 숫자의 길이를 모름)
    while n:  # (n>=1)
        tmp += str(n % 3)  # 3진법에서 맨 끝자리 수 3의 0 승자리는 n을 3으로 나눈 나머지와 동일.
        # 3의 1승자리는 n이 9의배수이면 0임. 3의 2승 자리는 n이 27의 배수이면 0임. 이 성질을 이용.
        n = n // 3  # A= P * 3 + R1, P= Q * 3 + R2, 형식의 나머지 정리 이용

    return int(tmp, 3)  # int는 다른 진법을 10진법으로 변환한다.