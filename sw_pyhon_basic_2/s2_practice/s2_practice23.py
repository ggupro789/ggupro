# 리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서
# 첫번째, 다섯번째, 여섯번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.


            
number =  [12, 24, 35, 70, 88, 120, 155]
result = [number[i] for i in range(len(number)) if(i+1 != 1 and i+1 != 5 and i+1 !=6)]
print(result)