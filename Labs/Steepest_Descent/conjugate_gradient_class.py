def steepest_descent(func, grad, vals, verbose=False):
    '''
    A function to find the minimum of a function via its gradient using
    the steepest descent method.

    **Parameters**

        func: *function*
            A function to be minimized
        grad: *function*
            The gradient of a function
        vals: *list, float*
            A list of values to minimize the function
        verbose: *bool, optional*
            Whether to print data every now and then.
    '''
    # Verify vals is in the correct form
    if not isinstance(vals, list):
        vals = [vals]

    # Some default values
    step_size = 0.00001
    g_tol = 0.00000001
    max_iter = 1000000

    iteration = 0
    gradient = float('inf')

    while iteration < max_iter and gradient > g_tol:
        if verbose and iteration % 100000 == 0:
            print("Iter %d: x = %s, f(x) = %.2f, g(x) = %.2f "
                  % (iteration, str(vals), func(*vals), g_tol))

        step = grad(*vals)
        if not isinstance(step, list):
            step = [step]

        # Take a step along the opposite of the gradient
        vals = [v - s * step_size for v, s in zip(vals, step)]

        gradient = (sum([s**2 for s in step]) / float(len(step)))**0.5

        iteration += 1

    return vals


def conjugate_gradient(func, grad, vals, verbose=False):
    '''
    This function was made in class, in a step-by-step build up from the
    steepest descent code.

    A function to find the minimum of a function via its gradient using
    the steepest descent method.

    **Parameters**

        func: *function*
            A function to be minimized
        grad: *function*
            The gradient of a function
        vals: *list, float*
            A list of values to minimize the function
        verbose: *bool, optional*
            Whether to print data every now and then.
    '''
    # Verify vals is in the correct form
    if not isinstance(vals, list):
        vals = [vals]

    # Some default values
    step_size = 0.00001
    g_tol = 0.00000001
    max_iter = 1000000

    iteration = 0
    gradient = float('inf')

    prev_grad = None
    prev_step = None

    # Begin iterating until the RMS gradient is below some tolerance or
    # until some number of iterations has been reached
    while iteration < max_iter and gradient > g_tol:
        if verbose and iteration % 100000 == 0:
            print("Iter %d: x = %s, f(x) = %.2f, g(x) = %.2f "
                  % (iteration, str(vals), func(*vals), g_tol))

        # Get the gradient and ensure it is in a list
        gradient = grad(*vals)
        if not isinstance(gradient, list):
            gradient = [gradient]

        # Take a step along the opposite of the gradient
        if prev_grad is None:
            # First step is done as a steepest descent method
            step = [-g for g in gradient]
        else:
            # All other steps are done by first calculating what beta is...
            numerator = sum([x**2 for x in gradient])
            denominator = sum([x**2 for x in prev_grad])
            if denominator == 0:
                beta = 10000.0
                # beta = 0
            else:
                beta = numerator / denominator

            # And then using the conjugate gradient method (Fletcher-Reeves)
            step = [-g + beta * s for g, s in zip(gradient, prev_step)]

        # Here we take our step, and save the current step and gradient as
        # previous for the next iteration.
        vals = [v + s * step_size for v, s in zip(vals, step)]
        prev_step = [s for s in step]
        prev_grad = [-g for g in gradient]

        # RMS (root-mean-squared gradient)
        gradient = (sum([s**2 for s in step]) / float(len(step)))**0.5

        iteration += 1

    return vals


def f1(x):
    return (x - 5.0)**2


def g1(x):
    return 2.0 * (x - 5.0)


def f2(x, y):
    return x**2 + (y - 23.2)**2


def g2(x, y):
    return [2.0 * x, 2.0 * (y - 23.2)]


def f4(x, y, w, z):
    return (x - 20.0)**2 + y**4 + w**6 + z**6


def g4(x, y, w, z):
    return [2.0 * (x - 20.0), 4.0 * y**3, 6.0 * w**5, 6.0 * z**5]


# Using a random value between -15.0 and 15.0, find the minimum of the
# function f1
# x1 = random.random() * 30.0 - 15.0
# x_min = conjugate_gradient(f1, g1, x1)
# print("x = %s, f(x) = %.2f, g(x) = %.2f "
#       % (str(x_min), g1(*x_min), g1(*x_min)))

# Using random values between -100.0 and 100.0, find the minimum of the
# function f2
# x1 = random.random() * 200.0 - 100.0
# x2 = random.random() * 200.0 - 100.0
# vals = [x1, x2]
# x_min = conjugate_gradient(f2, g2, vals)
# print("x = %s, f(x) = %.2f, g(x) = %s "
#       % (str(x_min), f2(*x_min), str(g2(*x_min))))

print("Using Conjugate Gradient...\n")
vals = [15.0, 3.0, -2.0, 5.0]
x_min = conjugate_gradient(f4, g4, vals)
print("x = %s, f(x) = %.2f, g(x) = %s "
      % (str(x_min), f4(*x_min), str(g4(*x_min))))

print("\n\nUsing Steepest Descent...\n")
x_min = steepest_descent(f4, g4, vals)
print("x = %s, f(x) = %.2f, g(x) = %s "
      % (str(x_min), f4(*x_min), str(g4(*x_min))))
