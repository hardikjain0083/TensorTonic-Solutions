import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    a=np.shape(v)[0]
    b=np.zeros([a,a])
    for i in range(0,np.shape(b)[0]):
        b[i][i]=v[i]
    return b

    pass
