import copy

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


def steepest_descent(grad, params):
	TOLERANCE = 0.00000001
	ALPHA = 0.0001
	MAX_ITER = 1000000

	if type(params) is not list:
		params = [params]

	step = [float('inf')]

	while max([abs(i) for i in step]) > TOLERANCE and MAX_ITER > 0:
		gradient = grad(*params)
		if type(gradient) is not list:
			gradient = [gradient]

		step = [ALPHA * g for g in gradient]
		params = [i - j for i, j in zip(params, step)]

		MAX_ITER -= 1

	if MAX_ITER <= 0:
		print("Hit maximum")
	return params


def conjugate_gradient(grad, params):
    TOLERANCE = 0.00000001
    ALPHA = 0.0001
    MAX_ITER = 1000000

    if type(params) is not list:
	       params = [params]

    step = [float('inf')]
    prevstep = []
    prevgrad = []

    while max([abs(i) for i in step]) > TOLERANCE and MAX_ITER > 0:
        gradient = grad(*params)
        if type(gradient) is not list:
            gradient = [gradient]

        if prevstep == []:
            step = [-ALPHA * g for g in gradient]

        else:
            numerator = sum([g**2 for g in gradient])
            denominator = sum([x**2 for x in prevgrad])
            if denominator == 0:
                beta = 0
            else:
                beta = numerator/denominator
            step = [(-g+beta*s)*ALPHA for g,s in zip(gradient,prevstep)]

        params = [i + j for i, j in zip(params, step)]
        prevstep = copy.deepcopy(step)
        prevgrad = [-g for g in gradient]
        # gradient = sum([g**2 for g in gradient])
        MAX_ITER -= 1

	if MAX_ITER <= 0:
		print("Hit maximum")
	return params











x_opt = conjugate_gradient(g1, 3.0)
# It should be ~ 3
print x_opt

#
# x_opt = steepest_descent(g2, [3.0, 30.0])
# # It should be ~ 0 and 23.2
# print x_opt
#
#
# x_opt = steepest_descent(g4, [1.0, 2.0, 5.0, 3.14159265])
# print x_opt
