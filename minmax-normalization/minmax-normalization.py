import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # 1. Convert input to a float array to ensure precise division
    X = np.asarray(X, dtype=float)
    
    # 2. Find min and max along the specified axis. 
    # keepdims=True allows the resulting array to broadcast correctly against X.
    x_min = np.min(X, axis=axis, keepdims=True)
    x_max = np.max(X, axis=axis, keepdims=True)
    
    # 3. Calculate the denominator (range)
    denominator = x_max - x_min
    
    # 4. Use np.maximum to replace any exact 0s with eps to prevent divide-by-zero
    denominator = np.maximum(denominator, eps)
    
    # 5. Apply the scaling formula
    return (X - x_min) / denominator