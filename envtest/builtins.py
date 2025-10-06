import numpy as np
import scipy

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return scipy.gaussian_filter(a, sigma=sigma)

def my_mat_solve(A,b):
    return A.inv()*b
