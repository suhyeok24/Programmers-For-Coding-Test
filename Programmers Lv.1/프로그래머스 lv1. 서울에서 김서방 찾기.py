# %이용
def solution(seoul):
    return "김서방은 %d에 있다" % seoul.index("Kim")

#f-string이용  >> 무조건 변수화 시켜서 사용해야됨 : f'문자열 {변수} 문자열'
def solution(seoul):
    Kim= seoul.index("Kim")
    return f"김서방은 {Kim}에 있다"