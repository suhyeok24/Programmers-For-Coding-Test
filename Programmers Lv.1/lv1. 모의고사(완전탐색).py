

# 내풀이- for문 생노가다 후 (o(3n))* sorted(o(nlogn)) dict에 값 저장. 이후 최댓값 찾기
import collections
def solution(answers):
    A1 = [1, 2, 3, 4, 5] * 2000
    A2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    A3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000   # 입력항의 최대값으로 설정 (10000자리 리스트)
                                                 # 개손해.
    A = [A1, A2, A3]
    c = collections.defaultdict(int)

    for j in range(3):
        for i, n in enumerate(answers):
            if n == A[j][i]:
                c[j + 1] +=1  #int 값도 딕셔너리 key가 될수 있음. 불변객체(일단 리스트만 가변객체)
    return sorted(k for k, v in c.items() if v == max(c.values()))


# 딕셔너리 최대 key값 출력 : max(c) -default
# 딕셔너리 최대 value값 출력 : max(c.values())
# 딕셔너리 최대 value값 기준 key 출력 (1개일때) : max(c, key=c.get)
# 딕셔너리 최대 value값 기준 key 출력 (2개이상) : [k for k,v in c.items() if v == max(c.values())]


#딕셔너리를 사용하지 않고 리스트로만 해결- 이게 훨 빠름(3배 이상) (0(9n))

def solution(answers):
    A1 = [1, 2, 3, 4, 5]
    A2 = [2, 1, 2, 3, 2, 4, 2, 5]
    A3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    A = [A1, A2, A3]
    score = [0, 0, 0] # 초기화 해놔야 바로 값 넣기 가능.
    result = []

    for j in range(3):
        for i, n in enumerate(answers):
            if n == A[j][i % len(A[j])]:  #cycle을 돌릴땐 나머지..
                score[j] += 1
    #여기까진 동일: count 를 쓸필요 없이 리스트에 직접넣자.
    # 결국 max값들의 index만 return 하면 된다. >> enumerate 사용(인덱스와 값 둘다 다룰 떄)
    for idx, num in enumerate(score):
        if num == max(score): # 값이 최대값과 같을때 index 리스트에 append
            result.append(idx + 1)
    return result

#무식하게 코딩하지 말자.
# cycle이나 pattern 돌릴때는 나머지 이용, 인덱스와 값 모두 다룰 때는 enumerate 이용!!