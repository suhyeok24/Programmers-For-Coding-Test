def solution(num):
    i=0
    if num==1:
        return 0
    while i<500:
        i+=1
        if num%2:
            num=num*3+1
        else:
            num=int(num/2)
        if num==1:break
    return i if i!=500 else -1

#mine