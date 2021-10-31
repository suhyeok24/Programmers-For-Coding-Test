#1.list comprehension 이용한 가장 완벽한 풀이?
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

#for i,j,k in commands 이 방식을 사용하면 2차원 리스트에서 한번에 내부 리스트 요소까지 추출가능!

#2. lambda, map 이용

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#3. 일반적 for문과 append 이용

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j]))[k-1])
    return answer

#4. 첫 내 풀이

 def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        s = array[i - 1:j]
        a = sorted(s)
        answer.append(a[k - 1])

    return answer

