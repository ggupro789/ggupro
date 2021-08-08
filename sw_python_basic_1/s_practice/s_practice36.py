number = int(input())

def sosu(x):
    sum = 0

    for i in range(x):
        try:
            if( x%i == 0):
                sum +=1
        except:
            sum +=1

    if(sum == 2):
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")

sosu(number)