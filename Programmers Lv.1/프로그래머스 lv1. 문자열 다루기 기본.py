#내 풀이
def solution(s):
    for i in s:
        if i.isdigit():continue #for문을 왜쓰노 ㄹㅇㅋㅋ ㅠㅠ
        return False
    return len(s)==4 or len(s)==6  # len(s) in (4,6) 이렇게도 표현 가능하다고 한다.

#좀 더 깔끔하게

def solution(s):
    return s.isdigit() and (len(s)==4 or len(s)==6) #문자열 자체에 대해서도  isdigit() 적용 가능

#정규표현식을 이용해봄
import re
def solution(s):
    if re.sub('[0-9]',"",s):  #정규표현식 '[\d]'로도 표현 ㄱㄴ, 숫자만 있지 않다면 re.sub값이 공백이 아님
        return False
    return len(s)==4 or len(s)==6

#예외처리를 이용한 방식- fresh한 발상
def solution(s):
    try:
        int(s)    # 문자열에 숫자이외의 값이 있으면 int(s)에서 오류가 발생함
    except:
        return False
    return len(s) == 4 or len(s) == 6
#연산시간도 매우빠름