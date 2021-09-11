id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","muzi frodo"]
k = 2
score = [0 for _ in range(len(id_list))]

dict_id = {item : 0 for item in id_list}
dict_id2 = {item : '' for item in id_list}

report = list(set(report))
for i in range(len(report)):
    report[i] = report[i].split()
    
for i in range(len(report)):
    dict_id[report[i][1]] += 1
    dict_id2[report[i][1]] += ' '+ report[i][0] 

for key,value in dict_id.items():
    if value >= k:
        m = dict_id2[key].split()
        for i in m:
            score[id_list.index(i)] += 1