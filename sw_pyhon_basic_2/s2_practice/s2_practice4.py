#리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
 

power = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
cut = 'aeiou'

result = [i for i in power if i not in cut]
result1 = ''.join(result)
print(result1)
