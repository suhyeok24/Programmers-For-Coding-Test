
def solution(s, n):
    s = list(s)
    for i in s:
        if i.isupper():
            i=chr((ord(i)-ord('A')+ n)%26+ord('A'))
        elif i.islower():
            i=chr((ord(i)-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# 문자열이 순환하는 상황에서는 기준을 잡고 나머지를 쓰면 손쉽게 문제를 풀 수 있다.
# 나머지는 몇 cycle을 돌리던지 구애받지 않고 원하는 값을 도출한다.