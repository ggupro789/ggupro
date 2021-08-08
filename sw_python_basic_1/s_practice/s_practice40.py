what = int(input())

def ox(x):
    gob = 1
    for i in range(x):
        gob *= i+1

    print(gob)

ox(what)