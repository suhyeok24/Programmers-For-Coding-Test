# 내 첫 풀이
def solution(s, n):
    answer=""
    for char in s:
        if char.islower():
            if ord(char)+n > 122:  #이 풀이의 한계는 n이 커지면 답이없음. 나머지를 이용해야함
                answer += chr(ord(char)+n-26)
            else:
                answer += chr(ord(char)+n)
        elif char.isupper():
            if ord(char)+n > 90:
                answer += chr(ord(char)+n-26)
            else:
                answer += chr(ord(char)+n)
        else:
            answer += char
    return answer

# if 내 case를 하나로 합쳐봄.
def solution(s, n):
    answer=""
    for char in s:
        if char.islower():
                answer += chr(ord(char)+n-26*((ord(char)+n)//123))
        elif char.isupper():
                answer += chr(ord(char)+n-26*((ord(char)+n)//91))
        else:
            answer += char
    return answer

#다른 사람 풀이 -나머지 응용 A와 a를 기준으로 모두 생각. 이 첫문자 포함 각각 25문자씩 있으며,
#26번쨰 부터 다시 순환함. 즉, 26으로 나눈 나머지를 이용하면 아무리 큰 숫자가 들어와도 연산 ㄱㄴ


def solution(s, n):
    answer=""
    for char in s:
        if char.islower():
                answer += ord("A")+(ord(char)-ord("A")+n)%26
        elif char.isupper():
                answer += ord("a")+(ord(char)-ord("a")+n)%26
        else:
            answer += char
    return answer

#리스트를 이용- 리스트를 쓰면 공백 처리 안해도 됨. 그냥 놔두면 됨.
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# 문자열이 순환하는 상황에서는 기준을 잡고 나머지를 쓰면 손쉽게 문제를 풀 수 있다.
# 나머지는 몇 cycle을 돌리던지 구애받지 않고 원하는 값을 도출한다.