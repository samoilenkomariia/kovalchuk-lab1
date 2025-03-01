import math

def getQuadraticRoots(a, b, c): 
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        return (x1, x2) if x1 != x2 else (x1,)
    else:
        return None

def interactive_mode():
    try:
        a = float(input("Enter non-zero a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except ValueError as err:
        print(f"Error: {err}")
        return

    print(f"Quadratic equation: {a}x² + {b}x + {c} = 0")
    roots = getQuadraticRoots(a, b, c)

    if roots is None:
        print("No real roots")
    else:
        print("The roots are:", ", ".join(map(str, roots)))

if __name__ == "__main__":
    interactive_mode()