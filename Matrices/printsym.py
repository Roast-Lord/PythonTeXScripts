# This function prints a symbolic matrix.

def newterm(j, size):
    # This is an auxiliar function that chooses whether or not to print '&' after a new term of the matrix.
    if (j < size):
        print(end=r"& ")

def printsym(nl, nc=1, sym='a', t='b'):

    matrix_style = '{' + t + 'matrix' + '}'

    print(end=r"\begin")
    print(matrix_style)

    for i in range(1, nl+1):
        for j in range(1, nc+1):
            if(nl == 1):
                print(end='%s_{%i} ' % (sym, j))
                newterm(j, nc)
            else:
                if(nc == 1):
                    print(end='%s_{%i} ' % (sym, i))
                else:
                    print(end='%s_{%i%i} ' % (sym, i, j))
                    newterm(j, nc)
        print(r"\\")

    print(end=r"\end")
    print(matrix_style)
printsym(4,sym='x')
