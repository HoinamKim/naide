import os
import sys

class NullWriter (object):
    def write (self, arg):
        pass
    def flush(args):
        pass
def print2(*args):
    res = ""
    for s in args:
        res += str(s)
    return res + "\n"

import numpy as np
import random
from sklearn import datasets

nullwrite = NullWriter()
oldstdout = sys.stdout
sys.stdout = nullwrite
iris = datasets.load_iris()
x_data = np.array([[x[1] for x in iris.data]]).T # sepal width  #(150, 1)
y_data = np.array([[y[3] for y in iris.data]]).T # petal width  #(150, 1)

# Random Value
ridx = 0 #random.randrange(0, 3)
# sys.in (range 0 ~ 6)
rv = int(sys.argv[1])

# Train Data (43~50)
x_test = x_data[ridx * 50 + 43:ridx * 50 + 50] # setosa test  #(15, 1)
y_test = y_data[ridx * 50 + 43:ridx * 50 + 50] # setosa test  #(15, 1)

random_x_test = x_test[rv]
result_y_test = y_test[rv]

sys.stdout = oldstdout
#print(str(rv))
print(str(random_x_test))
#print(str(result_y_test))
sys.out.flush()
