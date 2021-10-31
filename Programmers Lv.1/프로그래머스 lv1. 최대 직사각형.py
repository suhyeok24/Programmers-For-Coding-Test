import numpy as np


def solution(sizes):
    # 가로 max * 세로 max가 목표
    # 1.회전이 영향을 주는 경우
    # 가로나,세로의 max가 바뀔때

    # max(가로max 교환,세로max교환,default)

    sizes = np.array(sizes).T.tolist()
    print(sizes)  # [[가로],[세로]]

    width = sizes[0]
    height = sizes[1]
    default = max(width) * max(height)
    h_index = width.index(max(width))

    sizes[0][h_change], sizes[1][h_change] = sizes[1][h_change], sizes[0][h_change]

    h_change = max(width) * max(height)

