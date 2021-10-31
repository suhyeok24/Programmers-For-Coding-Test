#내풀이

def solution(d, budget):
    d.sort()

    if sum(d) <= budget:
        return len(d)

    s = 0
    for i, n in enumerate(d):
        s += n
        if s > budget:
            break
    return i