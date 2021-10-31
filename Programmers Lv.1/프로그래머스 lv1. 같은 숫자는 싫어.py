# 내 풀이
def solution(arr):
    answer = []
    answer.append(arr[0])  #공백 비교 안하기 위해

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  #일반적인 연속하지 않음의 정의. 현재의 숫자와 바로 직전 시점의 숫자와의 값비교
        #if len(answer)==0 or arr[i] != arr[i - 1]: >> 공백포함 조건 설정
            answer.append(arr[i])

    return answer
# ---------------------------------------------------------------------------------------

def solution(arr):
    a = []
    for num in arr:
        if a[-1:] != [num]:   #리스트의 크기가 어떻든 리스트의 마지막 항은 list[-1]로 추출할 수 있다.
                              #하지만 리스트 슬라이싱은 문자열 슬라이싱과 다르게 무조건 리스트로 추출
                              #즉 list[1:2](리스트 포함)과 list[1](리스트 포함x) 은 다르다.
                              # 공백 리스트여도 슬라이싱 가능함. 인덱스 조회는 불가
            a.append(num)

    return a