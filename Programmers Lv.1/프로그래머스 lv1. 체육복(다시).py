#남의 풀이.
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    #걍 뭐냐면 어렵게 생각하지 말고 각각의 경우에 대해 최선의 선택을 하는 거임
    # 근데 결국 이웃한 애들한테만 빌릴 수 있는것이고
    # 잃어버린 번호의 순서에 따라 빌릴 수 잇는 번호의 순서가 정해짐(크기순서)
    # 즉, 빌리는 경우의 규칙(나보다 큰걸 빌릴꺼냐, ㄴ작은걸 빌릴꺼냐) 만 정하면
    # 최선의 선택이 된다.(이 규칙을 일정하게 하면 됨)
    return answer

    # 한마디로 그냥 reserve에 숫자가 있으면 무조건 되는 거고
    (밴다이엄그램상 )  없으면 운없게 안되는 것.

    #그리고 for문 돌리는 범위를 remove하면안됨.
    