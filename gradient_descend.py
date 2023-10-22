import numpy as np

#implementing training data sets, x_train, y_train

x_train = np.array([1.0, 2.0, 3.0])
y_train = np.array([150, 220, 430])

#amount of data in the training sets
m = len(x_train)

#set initial params w,b
w = 1
b = 0.5

#learning rate for gradient descent

alpha = 0.1

#the function that calculates the linear regression model
def linear_model(x_train, w, b):
    f_wb = 0
    for i in range(m):
        f_wb = f_wb + (w*x_train[i] + b)
    return f_wb


# Squared error cost function
def cost_func(x_train, y_train, w, b):
    cost_sum = 0
    total_cost_func = 0
    for i in range(m):
        cost_sum = cost_sum + (((w*x_train[i] + b) - y_train[i])**2)
    total_cost_func = (1/(2*m)) * cost_sum
    return total_cost_func
    
#Gradient

dj_dw = 0
dj_db = 0


def gradients(x, y, w, b):
    dj_dw_tmp = 0
    dj_db_tmp = 0
    dj_db = 0
    dj_db = 0
    for i in range(m):
        dj_dw_tmp  = dj_dw_tmp +  ((w*x[i] + b) - y[i])*x[i]
        dj_db_tmp = dj_db_tmp + ((w*x[i] + b) - y[i])
    dj_dw = (1/m) * dj_dw_tmp
    dj_db = (1/m) * dj_db_tmp
    return dj_dw, dj_db



def gradient_descend(x, y, wi, bi, alpha, iters, gradient_function):
    #J_hist = []
    #P_hist = []

    w = wi
    b = bi

    for i in range(iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)

        #updating w and b
        w = w - alpha*dj_dw
        b = b - alpha*dj_db
    
    return w, b

w, b = gradient_descend(x_train, y_train, w, b, alpha, 20, gradients)

print(w, b)

    
    