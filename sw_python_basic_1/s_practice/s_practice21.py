scores = [88,30,61,55,95]


for i in range(5):
    if(scores[i]>=60):
        s = "합격입니다."
    else:
        s = "불합격입니다."
    print("%d번 학생은 %d점으로 %s"%(i+1,scores[i],s)) 