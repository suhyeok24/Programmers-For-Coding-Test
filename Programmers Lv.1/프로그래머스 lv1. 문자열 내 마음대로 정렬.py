def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

#sorted에서 정렬방식을 key로 지정할 수 있음. >> 함수이용 ㄱㄴ or len(길이)
#함수는 def를 써도 되지만 간편하게 lambda를 쓰는게 좋음
#그리고 lambda를 쓸때, 기준이 2개이상이면 튜플로 써야됨 반드시!!!!


#sort도 key 사용 ㄱㄴ,  ex) s.sort(key=len)


