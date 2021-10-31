# 내 풀이. -정렬을 이용 애초에 min값만 빼면 되는 것. 비교는 필요 X
def solution(arr):
    if len(arr)==1:
        return [-1]
    arr.remove(sorted(arr)[0]) #정렬된 배열에서 가장 첫번째 항이 가장 작은 수
                               #sorted는 원본값을 건들지 않는다.
    return arr


#min 제거도 ㄱㅊ- 제일 효율적인 풀이. 리스트 정렬하는 것보다, min값 찾아서 제거가 더 효율적
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]  #arr값이 빈 리스트일때는 [-1]
#return 문에도 if else를 넣을 수 있다.


# min을 이용한 list comprehension
def solution(arr):
    return [i for i in arr if i>min(arr)] or [-1] #빈리스트면 false라 -1 출력
#return A or B는 A가 false B를 return 시키기 위해 사용
# -런타임 에러가 발생
# -코드는 굉장히 깔끔하나 min함수가 o(n)이고 모든 리스트 요소와 min값을 비교해야하기 때문에 비효율적
