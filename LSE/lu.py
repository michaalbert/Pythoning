#let a matrix be a list of lists, we assume that the matrix being square is given. 
#the index in the outer list indicates the current row, the index in the inner list the column.

def idmatrix(n):
    """Creates an nXn identity matrix."""
    id = [[1 if i == j else 0 for j in xrange(n)] for i in xrange(n)]
    return id
            
def lu(mat):
    """Performs LU-decomposition on a matrix."""
    n = len(mat)
    lower = idmatrix(n)
    upper = mat   
    for i in xrange(n-1):
        for k in xrange(i+1, n):
            lower[k][i] = upper[k][i]/float(upper[i][i])
            for j in xrange(i, n):
                upper[k][j] -= lower[k][i]*upper[i][j]
    return (lower, upper)

def forward_elimination(lower, b):
    """Solves lower*res = b."""
    n = len(lower)
    res = [b[0]/float(lower[0][0])]
    n = len(lower)
    for i in xrange(1, n):
        res.append((1/float(lower[i][i]))*(b[i] - sum([lower[i][j]*res[j] for j in xrange(i)])))
    return res

def backward_elimination(upper, c):
    """Solves upper*res = c."""
    n = len(upper)-1
    res = [0 for i in xrange(n)]
    res.append(c[n]/float(upper[n][n]))
    for i in xrange(n-1, -1, -1):
        res[i] = (1/float(upper[i][i])*(c[i] - sum([upper[i][j]*res[j] for j in xrange(i+1, n+1)])))
    return res

def solve(mat, vec):
    """Solves the linear system of equations mat*x = vec for x, returns x."""
    lower = lu(mat)[0]
    upper = lu(mat)[1]
    return backward_elimination(upper, forward_elimination(lower, vec))
