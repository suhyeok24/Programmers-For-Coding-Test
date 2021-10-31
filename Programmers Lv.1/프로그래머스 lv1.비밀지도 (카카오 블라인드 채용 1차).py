
#내 풀이
def solution(n, arr1, arr2):
    pro1 = []
    pro2 = []
    for i in range(n):
        # 10진수의 binary 문자열화 >> bin(10진수를 2진수의 문자열 형태로 바꿔줌)
        num1 = bin(arr1[i])[2:]
        num2 = bin(arr2[i])[2:]

        # 자릿수를 맞추기 위한 0값 전처리
        while len(num1) != n:
            num1 = "0" + num1
        while len(num2) != n:
            num2 = "0" + num2

        # 이차원 리스트 형태로 만들어주기 (type은 int)
        pro1.append(list(map(int, num1)))
        pro2.append(list(map(int, num2)))

    # 비밀지도 해독
    pro3 = []

    for j in range(n):
        s = ""
        for k in range(n):
            # 2차원 리스트 요소 차례대로 비교
            if pro1[j][k] or pro2[j][k]:
                s += "#"
            else:
                s += " "
        pro3.append(s)

    return pro3

# #비트 연산을 이용한 풀이 >> 매우 훌륭하다..

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):  # 처음부터 분해하지말고 걍 ZIP을 써서 각 리스트 첫 값부터 비교
        a12 = bin(i | j)[2:]  # bin(10진수 | 10진수) : 10진수를 자동으로 2진수로 변환하여 or비트연산을 수행한 2진수 문자열을리턴
        a12 = a12.rjust(n, "0")  # n자리로 오른쪽 정렬, 나머지는 0으로 채워넣어라.. rjust 대박
        a12 = a12.replace("1", "#").replace("0", " ")  # 문자를 치환하는 법..
        answer.append(a12)

    return answer