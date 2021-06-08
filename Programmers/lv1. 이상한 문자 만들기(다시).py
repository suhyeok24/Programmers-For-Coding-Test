def solution(s):
    s_list=s.split()
    for j,chr in enumerate(s_list):
        chr_new =""
        for i,str in enumerate(chr):
            if i % 2 ==0:
                chr_new += str.upper()
            else:
                chr_new += str.lower()
        s_list[j]=chr_new
    return " ".join(s_list)  #공백이 한칸으로 일정할때 밖에 안됨

