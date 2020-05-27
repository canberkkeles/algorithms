import matplotlib.pyplot as plt
import math

x_axis = [i for i in range(1,31)]

a_results = [math.sqrt(x) for x in x_axis]
b_results = [pow(10,x) for x in x_axis]
c_results = [pow(x,1.5) for x in x_axis]
d_results = [pow(2,math.sqrt(math.log2(x))) for x in x_axis]
e_results = [pow(x,(5/3)) for x in x_axis]

print(a_results[29])
print(b_results[29])
print(c_results[29])
print(d_results[29])
print(e_results[29])