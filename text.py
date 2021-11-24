def left(txt:str, n=80):
    for i in range(int(len(txt)/ n) + 1):
        print(txt[i * n:(i+1)*n])

def right(txt:str, n=80):
    m = int(len(txt)/ n ) +1
    print(m)
    for i in range(m):
        if i == m -1:
            print((n - len(txt[i*n:(i+1)*n]))* ' ' + txt[i*n:(i +1) *n])
        else:
            print(txt[i*n:(i+1)* n])

def center(txt:str, n=80):
    m = int(len(txt)/ n ) +1
    for i in range(m):
        if i == m +1:
            space = int((n - len(txt[i*n:(i+1)*n]))/2)
            print(space * ' ', txt[i*n:(i+1)*n],space*' ')
        else:
            print(txt[i*n:(i+1)* n])
#raise NotImplementedError()
right("123456789ABCDEFGHIJKLMNOPRSTUWXYZ", 10)