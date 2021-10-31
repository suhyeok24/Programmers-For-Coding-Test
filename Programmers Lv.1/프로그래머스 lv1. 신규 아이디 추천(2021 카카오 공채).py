#내 풀이.
def solution(new_id):
    # 1단계:
    answer = new_id.lower()

    # 2단계:
    exception = ["-", "_", "."]
    for chr in answer:
        if not chr.isalnum() and not chr in exception:
            answer = answer.replace(chr, "")
    # 3단계:# #연속된 문자열 제거는 stack을 활용하여 배열의 마지막 숫자와 넣을 숫자를 확인한 뒤, 넣을 여부를 결정하는 방식 사용
    #마침표(.)가 2번이상 연속된 부분을 하나의 마침표로 치환

    b = []
    for i in answer:
        if not b:
            b.append(i)
        else:
            if i == ".":
                if b[-1] != ".":  # 리스트의 슬라이싱은 리스트 / 문자열의 슬라이싱은 문자열
                    b.append(i)
            else:
                b.append(i)
    answer = "".join(b)

    # 좋은 풀이: 하나의 연속된 문자만을 필터링할때는 그냥 while 문을 사용하면 알아서 루프가 반복실행되어 반복이 없어짐.
    # while ".." in answer:
    #     answer = answer.replace("..",".")
    # 참고로 replace 는 리턴값이 없어 변수지정이 꼭 필요함(내용 저장시)

    # 연속된 문자가 여러개일경우는 stack 해바 ㅇㅇ


    # 4단계:
    if answer[0] == ".":
        answer = answer[1:]
    if answer[-1:] == ".":  # answer가 비어있을 수 있기 때문에 [-1:]을 해준다. 비어잇을때 [-1:] 하면 오류안나고 [] 출력
        answer = answer[:-1]

    # 5단계:
    if not answer:
        answer = "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer