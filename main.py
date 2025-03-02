import sys, math

def getQuadraticRoots(a, b, c): 
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        return (x1, x2) if x1 != x2 else (x1,)
    else:
        return None

def get_correct_input(user_in):
    while True:
        try:
            value = float(input(user_in))
            if user_in.startswith("Enter non-zero a") and value == 0:
                raise ValueError
            return value
        except ValueError:
            print("Error: Incorrect number entered")

def interactive_mode():
    a = get_correct_input("Enter non-zero a: ")
    b = get_correct_input("Enter b: ")
    c = get_correct_input("Enter c: ")

    print(f"Quadratic equation: {a}x² + {b}x + {c} = 0")
    roots = getQuadraticRoots(a, b, c)

    if roots is None:
        print("No real roots")
    else:
        print("The roots are:", ", ".join(map(str, roots)))

def file_mode(filepath):
    try:
        with open(filepath, "r") as file:
            data = file.readline().strip().split()
            if len(data) != 3:
                raise ValueError("Invalid file format")
            a, b, c = map(float, data)
            if a == 0:
                raise ValueError
    except (ValueError, FileNotFoundError) as e:
        if isinstance(e, FileNotFoundError):
            print("File not found")
        else: 
            print("Invalid file format")
        sys.exit(1)
    
    print(f"Quadratic equation: {a}x² + {b}x + {c} = 0")
    roots = getQuadraticRoots(a, b, c)
    if roots is None:
        print("No real roots")
    else:
        print("The roots are:", ", ".join(map(str, roots)))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        interactive_mode()