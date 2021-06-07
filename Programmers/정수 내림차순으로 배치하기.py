def solution(n):
    return int("".join(sorted(str(n))[::-1]))
#의외로 복잡하다. 자연수>>문자>>리스트>>문자>>자연수 순