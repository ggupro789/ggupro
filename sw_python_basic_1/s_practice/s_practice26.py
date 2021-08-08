stu_blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
stu_count ={'A': 0,'B': 0,'O': 0,'AB': 0}
for i in stu_blood:
    if(i == 'A'):
        stu_count['A'] += 1
    elif(i == 'B'):
        stu_count['B'] += 1
    elif(i == 'O'):
        stu_count['O'] += 1
    elif(i == 'AB'):
        stu_count['AB'] += 1    

print(stu_count)

