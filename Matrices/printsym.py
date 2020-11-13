# This function prints a symbolic matrix.

def newterm(j, size):
    # This is an auxiliar function that chooses whether or not to print '&' after a new term of the matrix.
    if (j < size):
        print(end=r"& ")

def printsym(nl, nc=1, sym='a', t='b'):
    #This function only needs 1 argument 'nl' which is the number of lines in the matrix.
    #This function receives a number of lines 'nl' and a number of columns 'nc', a symbol 'sym' and a LaTeX matrix style 't'.
    #The parameter 'sym' is any string you want for a symbolic variable.
    #The style 't' can be: '' for plain matrix, 'b' for square brackets matrix, 'B' for curly brackets matrix, 'v' for pipes matrix, 'V' for double pipes matrix and 'small' for small matrix.
    #By default if 'nc', 'sym and 't' are no especified, the function will print a collum matrix with the symbol 'a' and LaTeX square brackets matrix style.
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
