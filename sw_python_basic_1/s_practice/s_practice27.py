scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i = 0
sum =0

while i<len(scores) :
    if(scores[i]>=80):
        sum += scores[i]
    
    i+=1

print("%d"%(sum))