# 내 풀이
import numpy as np
def solution(sizes):


    sizes=np.array(sizes).T.tolist()
    print(sizes) #[[가로],[세로]]

    width=sizes[0]
    height=sizes[1]

    big=max(max(width),max(height))

    #가장 big을 찾는다. > 나머지 가로(세로)를 최소화시켜야 함.
    # index끼리 대소비교해서 smaller를 나머지 선분으로 몰빵

    if big in width:
        for i in range(len(width)):
            if width[i] < height[i]:
                width[i],height[i] = height[i],width[i]
        return big*max(height)

    else:
        for i in range(len(height)):
            if width[i] > height[i]:
                width[i],height[i] = height[i],width[i]
        return big*max(width)

#좋은 풀이  > 아 ㅋㅋ

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

#max(max(x) for x in sizes) : 내가 말한 가장 큰놈. big
#max(min(x) for x in sizes) : smaller ones 들중 가장 큰 놈..(나머지 선분의 최소화)