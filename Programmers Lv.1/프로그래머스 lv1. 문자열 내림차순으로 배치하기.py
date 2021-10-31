# 내 풀이
def solution(s):
    return "".join(sorted(s)[::-1])
#   return ''.join(sorted(s, reverse=True))
#   sorted와 sort에는 reverse 옵션이 있다.(역정렬, 내림차순정렬)
#   sorted(s, reverse= True) or s.sort(reverse= True)



# 정렬기법 sort는 리스트의 method
# sorted는 문자열, 리스트 모두 가능하나 반드시 리스트로 리턴, join활용해 문자열로 만듦.
# 사전정렬은 대문자 >> 소문자 순임
