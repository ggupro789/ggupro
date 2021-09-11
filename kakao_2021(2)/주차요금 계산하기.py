import math
def cal(time,fee):
    if time < fee[0]:
        return 5000

    score = fee[3]*math.ceil(((time-fee[0])/fee[2]))+fee[1]
    return int(score)

fee = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

dict_1 = {}
dict_2 = {}
dict_3 = {}

for i in range(len(records)):
    records[i] = records[i].split()

for i in range(len(records)):
    # records[i][0] = ''.join(records[i][0].split(":"))
    records[i][0] = list(records[i][0].split(":"))
    records[i][0] = int(records[i][0][0]) * 60 + int(records[i][0][1])
for i in range(len(records)):
    dict_1[records[i][1]] = 0
    dict_2[records[i][1]] = 0
    dict_3[records[i][1]] = 0

for i in range(len(records)):
    if records[i][2] == 'IN':
        dict_1[records[i][1]] = records[i][0]
        dict_3[records[i][1]] = 1
    if records[i][2] == 'OUT':
        dict_2[records[i][1]] += records[i][0] - dict_1[records[i][1]]
        dict_3[records[i][1]] = 0

for key,value in dict_3.items():
    if value == 1:
        dict_2[key] += (1439 - dict_1[key])
dict_2 = sorted(dict_2.items())

answer = []
for i in range(len(dict_2)):
    answer.append(cal(dict_2[i][1],fee))


print(dict_2)
print(answer)
# print(records)
