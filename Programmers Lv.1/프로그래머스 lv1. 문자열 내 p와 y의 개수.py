
# 첫 내 풀이, Counter이용
def solution(s):
    from collections import Counter
    c= Counter(s.lower())
    if c["p"]==c['y'] or not(c["p"] or c["y"]):
        return True
    else:
        return False

# 다른 풀이 참고
def solution(s):
    from collections import Counter
    c= Counter(s.lower())

    return c["p"]==c['y']   # 딕셔너리에서 조회는 O(1)임



    #어차피 p,y 둘다 아예 없는게, 둘의 개수가 같은 것에 속하므로 없애도 됨.(not(c["p"] or c["y"]) 이조건ㅇㅇ

    # 그리고 return 자체에 비교문을 걸어두면 if문을 생략해도 됨.알아서 같으면 True, 틀리면 False 반환함.

# Count 이용

def solution(s):
    return s.lower().count("p") == s.lower().count("y")

#시간복잡도 o(n) -Count는 일일히 다 세는 거기 때문

#collections.Counter 이용한 것이 Count보다 연산이 더 빠르다 나옴.
#Counter가 유용함. ㅇㅇ