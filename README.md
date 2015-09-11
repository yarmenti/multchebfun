# multchebfun- Python Chebyshev multi-dimensional functions

This module allows to make an interpolated version of any multidimensional python function.
Here is an example on how to use it:

```python
import multchebfun

# define a function
def f(x, y):
	return x*y
	
# define lower and upper bounds
l_bounds = [-10., -10.]
u_bounds = [10., 10.]

# define number of nodes by dimensional
nodes = [5, 5]

f_tcheb = multchebfun.ChebyshevFun(f, l_bounds, u_bounds, nodes)

# then you can call whatever you want your function 
# or the interpolated one with the parameters.
print f_tcheb(2., 4.)
print f(2., 4.)
```
