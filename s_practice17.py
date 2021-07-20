x = input()
y,y1 ='a','z'
z,z1 = 'A','Z'
result = ord(x)

if(y<=x<=y1):
    print("%c(ASCII: %d) => %c(ASCII: %d)" % (chr(result),result,chr(result-32),result-32))
elif(z<=x<=z1):
    print("%c(ASCII: %d) => %c(ASCII: %d)" % (chr(result),result,chr(result+32),result+32))
else:
    print("%c(ASCII: %d)"%(x,result))