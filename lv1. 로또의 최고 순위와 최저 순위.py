#내 풀이.

def solution(lottos, win_nums):
    pung = 0
    # 0이 아닌 번호중 당첨된 번호가 있나 확인
    for i in win_nums:
        if i in lottos:
            pung += 1

    if 0 not in lottos:  # 0이 없을때
        mi = pung
        ma = pung

    # 0이 있을때  #생각해보니까 0이 없을때, 있을 때 나눌 필요 X
    mi = pung
    ma = pung + lottos.count(0)

    answer = [ma, mi]

    return [1 + (6 - i) if i else 6 for i in answer]

# 인덱스를 활용한 좋은 풀이

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]  # rank index = 맞은 번호 개수

    mi = 0  # 조커 안쓴게 최솟값
    ma = lottos.count(0)  # 0의 개수만큼 더 맞을 수 있음. (조커)

    for i in lottos:
        if i in win_nums:
            mi += 1
            ma += 1

    return [rank[ma], rank[mi]]

#set을 활용 >> for문 안쓰기. 지린다. 두 리스트 모두 중복된 수가 없다는 것을 활용해 for문이 아닌 교집합을 활용.
# 무지성 for문을 줄여야 할때. 안그럼 실력이 늘지 않는다..

def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}  # 맞은 개수 : 순위 dict 근데 이건 list로 써도 됨.

    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)],
            rank[len(set(lottos) & set(win_nums))]]

    # 최대.조커(0) 다 쓸때
    # 최소.조커안쓸때. lottos와 win_nums의 교집합ㄷ