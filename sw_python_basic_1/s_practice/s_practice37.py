number = int(input())

def pi(x):
    P = [1,1]
    for i in range(2,x):
        chi = P[i-1]+P[i-2]
        P.append(chi)
    print(P)

pi(10)

