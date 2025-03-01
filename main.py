import math

def getQuadraticRoots(a, b, c): 
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        return (x1, x2) if x1 != x2 else (x1,)
    else:
        return None
