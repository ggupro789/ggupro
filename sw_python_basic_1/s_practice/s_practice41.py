# 숫자 제곱 + ,로 구분지어준다.
x1 = input()

def jgob(x):
    y = x.split(',')

    for i in y:
        print("square({0}) => {1}".format(int(i),int(i)*int(i)))

jgob(x1)