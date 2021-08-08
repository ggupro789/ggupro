# 다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
# 구분하는 프로그램을 작성하십시오.

alpha = input()
protocol = alpha.split('://')
host = protocol[1].split('/')
others = host[1]
print("protocol: {0}".format(protocol[0]))
print("host: {0}".format(host[0]))
print("others: {0}".format(host[1]))



# for i in range(len(result)):
#     if(i<len(result)-1):
#         print("{0}".format(result[i]),end=' ')
#     else:
#         print("{0}".format(result[i]))