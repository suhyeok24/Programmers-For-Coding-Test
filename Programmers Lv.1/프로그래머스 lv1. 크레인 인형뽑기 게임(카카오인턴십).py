#2019 카카오 개발자 겨울 인턴십 문제!!!!!

#내 풀이.
def solution(board, moves):
    # 1. lane설정
    lane = []
    for i in zip(*board):
        lane.append(list(i))

    # 2. 0값 없애기 > 빈라인이면 []이 됨.
    count = 0
    for i in range(len(lane)):
        for j in range(len(lane)):
            if lane[i][j]:
                lane[i][:j] = []
                break
        if lane[i] == [0] * len(lane):  # 모두 0값인 경우 []만들어주기
            lane[i] = []

    # 3. 크레인 뽑아서 바구니 넣기

    bas = []  # 바구니 생성

    sum = 0
    for i, n in enumerate(moves):

        if not lane[n - 1]:  # 빈레인 골랐을때 넘어가기
            continue

        doll = lane[n - 1].pop(0)  # 크레인이 뽑은 인형

        if bas:  # 바구니가 차있을때

            if bas[-1] != doll:  # 이미 들어있던거랑 같지 않을때 append
                bas.append(doll)
            else:  # 같으면 들어있던거 펑 + append 하지 않음(2개 제거 효과) / 펑 횟수 +1
                del bas[-1]
                sum += 1
        else:
            bas.append(doll)  # 바구니가 비어있을때는 그냥 넣기

    return sum * 2  # 터진 인형 = 펑 횟수 * 2(한번에 2개 터짐)

#다른사람 풀이

# 굳이 board를 변형하지 않아도 됨. 나는 변형했었는데 굳이였던듯.

def solution(board, moves):
    stacklist = [0]  #바구니에 0값을 미리 넣어둬서 항상 채워져있는 상태로 유지.
                     #바구니의 상태를 고려하지 않아도 된다.
                     #이게 상관없는 이유. 어차피 정답은 터지는 인형의 개수를 구하는 것이고
                     #뽑히는 인형은 0이아닌 숫자기 때문에 상관 X
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:  #어차피 j순서대로 뽑아가기 때문에 차례대로 for문적용가능.

                #인형이 있을때 그냥 넣고보기
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0  # 뽑았으면 0으로 초기화.

                #나는 바구니가 비어있을때와 차있을때를 구별했지만
                #여기선 그냥 넣고보고 나중에 판단.

                if stacklist[-1] == stacklist[-2]: #넣어보니까 마지막 2개가 똑같네??
                    stacklist.pop() #펑.
                    stacklist.pop() #펑.
                    answer += 2
                break  #인형 하나라도 뽑으면 끝.

    return answer