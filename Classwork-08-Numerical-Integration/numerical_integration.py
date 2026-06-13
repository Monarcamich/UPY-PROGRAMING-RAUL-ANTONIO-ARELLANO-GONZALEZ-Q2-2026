
import math
#INPUT
#Functions and their exact integrals
print("\n=== FUNCTIONS ===")
print("1. x^2 + 2x - 3   → [1,4]     = 27.00")
print("2. 3x^3 - x^2 + 5 → [0,2]     = 21.33")
print("3. sin(x)         → [0,π]     = 2.00")
print("4. cos(x)+1       → [0,π/2]   = 2.5708")
print("5. exp(x)         → [0,2]     = 6.3891")
print("6. ln(x)          → [1,3]     = 1.2958")

choice = int(input("Choose function (1-6): "))

# Store function expression, interval [a,b], and exact integral
if choice == 1:
    f = "x**2 + 2*x - 3"
    a, b, exact = 1, 4, 27.00
elif choice == 2:
    f = "3*x**3 - x**2 + 5"
    a, b, exact = 0, 2, 21.33
elif choice == 3:
    f = "math.sin(x)"
    a, b, exact = 0, math.pi, 2.00
elif choice == 4:
    f = "math.cos(x) + 1"
    a, b, exact = 0, math.pi/2, 2.5708
elif choice == 5:
    f = "math.exp(x)"
    a, b, exact = 0, 2, 6.3891
else:
    f = "math.log(x)"
    a, b, exact = 1, 3, 1.2958

print(f"\nFunction: {f}   Interval: [{a}, {b}]   Exact = {exact:.4f}")

#Modes
print("\n=== MODES ===")
print("1. Default (n=100, Midpoint method)")
print("2. Custom (you set n and method)")
print("3. Auto-adjust (you set error tolerance)")
mode = input("Mode (1/2/3): ")

#PROCESS
if mode == "1":

    n = 100
    method = "MPM"
elif mode == "2":

    n = int(input("Number of subintervals n: "))
    method = input("Method (LRM, RRM, MPM, TRAP): ").upper()

else:   # mode == "3" Auto-adjust
    tol = float(input("Tolerance (e.g., 0.001 for 0.1%): "))
    auto_method = input("Method for auto-adjust (LRM/RRM/MPM/TRAP): ").upper()
    n = 10
    while True:
        h = (b - a) / n
        area = 0.0
        # Compute integral with current n
        if auto_method == "LRM":
            for i in range(n):
                x = a + i * h
                area += eval(f.replace("x", str(x))) * h
        elif auto_method == "RRM":
            for i in range(1, n+1):
                x = a + i * h
                area += eval(f.replace("x", str(x))) * h
        elif auto_method == "MPM":

            for i in range(n):
                x = a + (i + 0.5) * h
                area += eval(f.replace("x", str(x))) * h
        elif auto_method == "TRAP":

            area = (h/2) * eval(f.replace("x", str(a)))
            for i in range(1, n):
                x = a + i * h
                area += (h/2) * 2 * eval(f.replace("x", str(x)))
            area += (h/2) * eval(f.replace("x", str(b)))
        rel_err = abs(area - exact) / exact
        if rel_err < tol or n > 1000000:
            break
        n *= 2   # double subintervals

    
    method = auto_method
    print(f"Auto-adjust: reached n = {n}, rel error = {rel_err:.6f}")

#compue integral using selected method and n
if mode != "3":
    h = (b - a) / n
    area = 0.0
    if method == "LRM":
        for i in range(n):
            x = a + i * h
            area += eval(f.replace("x", str(x))) * h
    elif method == "RRM":
        for i in range(1, n+1):
            x = a + i * h
            area += eval(f.replace("x", str(x))) * h
    elif method == "MPM":
        for i in range(n):
            x = a + (i + 0.5) * h
            area += eval(f.replace("x", str(x))) * h
    elif method == "TRAP":
        area = (h/2) * eval(f.replace("x", str(a)))
        for i in range(1, n):
            x = a + i * h
            area += (h/2) * 2 * eval(f.replace("x", str(x)))
        area += (h/2) * eval(f.replace("x", str(b)))

abs_err = abs(area - exact)
rel_err = abs_err / exact

#OUTPUT
print("\n" + "="*50)
print("RESULTS")
print("="*50)
print(f"Function: {f}")
print(f"Interval: [{a}, {b}]")
print(f"Method: {method}")
print(f"Subintervals (n): {n}")
print(f"Approximation: {area:.8f}")
print(f"Exact value:   {exact:.8f}")
print(f"Absolute error: {abs_err:.8f}")
print(f"Relative error: {rel_err:.6f} ({rel_err*100:.4f}%)")