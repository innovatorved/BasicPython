a = [[1,1],[1,0]]

def square(a,n):
    out = [item[:] for item in a]
    b = [item[:] for item in a]
    for x in range(n-1):
        out[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        out[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        out[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        out[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        b = [item[:] for item in out]
    return b
