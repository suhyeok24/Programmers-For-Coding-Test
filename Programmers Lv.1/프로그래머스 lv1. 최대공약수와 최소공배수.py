
#내풀이 - 최대공약수를 for문 노가다로 돌리고, 최소공배수는 최대공약수를 이용해 풀이
# -O(n)이라 비효율적
def solution(n, m):
    maxi = 1  # default 값 1 , for문을 돌려서 max값을 교체할 거임.
    for i in range(1, min(n, m) + 1):  # 최대공약수는 min(n,m)보다 클 수 없음
        if not (n % i or m % i):
            if i > maxi:
                maxi = i

    n_small, m_small = n // maxi, m // maxi
    mini = maxi * n_small * m_small  # n= G*n_small, m= G*m_small (G는 최대공약수, n_small과 m_small은 서로소)

    return [maxi, mini]

# 유클리드 호제법- 최대공약수를 구하는 유클리드의 <원론>에 나온 알고리즘..-고전 느낌 지리구~
# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.

# ex)78696과 19332의 최대공약수를 구하면,
# # # #
# # # #     78696 ＝ 19332×4 ＋ 1368
# # # #     19332 ＝ 1368×14 ＋ 180
# # # #      1368 ＝ 180×7 ＋ 108
# # # #       180 ＝ 108×1 ＋ 72
# # # #       108 ＝ 72×1 ＋ 36
# # # #        72 ＝ 36×2 ＋ 0
# # # # 따라서, 최대공약수는 36이다.

def solution(n, m):
    a, b = min(n, m), max(n, m)  # 다른 변수로 둬야함. 기존 n,m을 훼손시키지 않기 위함

    r = 1  # while문 들어가기 전 초기화
    while r > 0:
        r = b % a  # 나머지 계속 반복
        b, a = a, r  #변수 swaping 여기가 매우 중요..

    # while문 종료 후 상태: r= 0, b=a*Q (첫째줄) 여기서 최대공약수는 바로 a
    #                    b=a ,a=r=0 (둘째 줄) b가 a가 되고 a가 0이 되었으므로 최대공약수는 b

    return [b, int(n * m / b)]  # n =  b * X , m= b * Y
    # 최소공배수 = n*m = b*b*X*Y /b = b*X*Y(X,Y는 서로소)
