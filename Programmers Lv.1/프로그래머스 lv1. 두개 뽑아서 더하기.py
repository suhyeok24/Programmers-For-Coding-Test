#브루트포스  >> 이거 밖에 답 없었음;
def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])

    return sorted(list(set(result)))


#