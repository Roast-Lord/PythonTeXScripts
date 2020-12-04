import sympy as sp

a = sp.MatrixSymbol('x',3,3)
b = sp.MatrixSymbol('y',3,1)

c = sp.Matrix(a*b)

print(sp.latex(c))

