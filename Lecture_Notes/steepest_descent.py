
def f1(x):
    return (x-5.0)**2

def g1(x):
    return 2.0*(x-5.0)

def f2(x,y):
    return x**2+(y-23.2)**2

def g2(x,y):
    return [2.0*x, 2.0*(y-23.2)]

def f4(x,y,w,z):
    return (x-20)**2+y**4+w**6+z**6
def g4(x,y,w,z):
    return [2*(x-20),4*y**3,6*w**5,6.0*z**5.0]

def steepest_descent(grad, params):
    TOLERANCE = 0.0000001
    ALPHA = 0.000001 # must be smaller than the TOLERANCE
    MAX_ITER = 100000

    if type(params) != list:
        params = [params]

    step = [float('inf')]
    while max([abs(x) for x in step]) > TOLERANCE and MAX_ITER>0:
        # unpacks list into a function (only in python)
        gradient = grad(*params)
        if type(gradient) is not list:
            gradient = [gradient]
        step = [ALPHA * g for g in gradient]
        params = [i-j for i,j in zip(params,step)]
        MAX_ITER -= 1

    return params



x_opt = steepest_descent(g1,3.0)
# expect a value ~5
print x_opt

x_opt = steepest_descent(g4,[1.0, 2.0, 5.0, 100.0])
# expect value ~0 and ~23.2
print x_opt
