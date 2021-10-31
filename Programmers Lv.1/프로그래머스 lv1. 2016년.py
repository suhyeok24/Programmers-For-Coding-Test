def getDayName(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    #1월 1일을 기준으로 리스트 다시 정렬(7로 나눈 나머지)

    fin = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #규칙이 없을때는 나열하는 것이 가장 좋은방법일 수 잇다. ㅎㅎ

    edate = sum(fin[:a - 1]) + b

    return day[edate % 7]