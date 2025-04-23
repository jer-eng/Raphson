def bisection_method(f, a, b, tol=1e-6, max_iter=1000):
    # First, check if the function has opposite signs at a and b (which means there's a root in between)
    if f(a) * f(b) >= 0:
        raise ValueError("The function must change signs in the interval [a, b].")

    steps = 0  # To keep track of how many steps it takes
    while (b - a) / 2 > tol and steps < max_iter:
        c = (a + b) / 2  # This is the midpoint of the interval
        if f(c) == 0:
            break  # If f(c) is exactly zero, we've found the root!
        elif f(a) * f(c) < 0:
            b = c  # The root is in the left half
        else:
            a = c  # The root is in the right half
        steps += 1  # Count this step

    return (a + b) / 2, steps  # Return the estimated root and how many steps it took

def newton_raphson(f, df, x0, tol=1e-6, max_iter=1000):
    steps = 0  # Count steps
    x = x0  # Starting guess
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("The derivative is zero — can't divide by zero!")  # Stop if slope is flat
        x_new = x - fx / dfx  # Newton-Raphson formula
        steps += 1
        if abs(x_new - x) < tol:
            break  # If the change is very small, we consider it converged
        x = x_new  # Update x to the new value
    return x, steps  # Return root and number of steps

def compare_methods(f, df, a, b, x0, tol=1e-6):
    # Try the Bisection method first
    try:
        b_root, b_steps = bisection_method(f, a, b, tol)
    except Exception as e:
        b_root, b_steps = None, str(e)  # Catch any errors and store them

    # Now try the Newton-Raphson method
    try:
        nr_root, nr_steps = newton_raphson(f, df, x0, tol)
    except Exception as e:
        nr_root, nr_steps = None, str(e)  # Catch any errors here too

    # Return a dictionary comparing both methods
    return {
        "Bisection": {"root": b_root, "steps": b_steps},
        "Newton-Raphson": {"root": nr_root, "steps": nr_steps}
    }
