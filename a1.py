def karatsuba(x,y):
    if x < 10 and y < 10:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        m = 10**(n//2)

        a, b = x//m, x%m
        c, d = y//m, y%m

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

        return (ac * (m**2)) + (ad_plus_bc * m) + bd
