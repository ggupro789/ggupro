number = [12,24,35,24,88,120,155,88,120,155]


def only(x):
    y = []
    for i in x:
        if( i not in y):
              y.append(i)
    
    print(y)


only(number)