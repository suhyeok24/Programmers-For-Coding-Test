# 내 풀이 - dict 정렬 이용

def solution(N, stages):
    import collections

    # 1. 실패율 계산

    error = collections.defaultdict(float)

    for i in range(N):
        bottom = 0
        top = 0
        for n in stages:
            if n >= i + 1:
                bottom += 1
                if n < i + 2:
                    top += 1
        try:
            err_rate = top / bottom
        except:  # bottom이 0일때 - 스테이지에 도달한 유저 없음
            err_rate = 0

        error[i + 1] += err_rate

    # 2. 실패율의 내림차순으로 스테이지 번호 리턴

    # 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
    return sorted(error, reverse=True, key=error.get)

# 다른 풀이(좋은 풀이)

def solution(N, stages):
    fail = {}   # 일반 dict도 dict[key]=values로 정의 가능, 없는 키 조회만 안될뿐임.
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i]) /len([a for a in stages if a>=i])
                    #i 스테이지에 머물러 있는것 len 이용
                    #list comprehension 을 이용해 코드 간소화
        except:
            fail_ = 0  # 분모가 0 일때
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)  # key값을 출력할때는 그냥 dict명만 쓰면됨(default)
    return answer