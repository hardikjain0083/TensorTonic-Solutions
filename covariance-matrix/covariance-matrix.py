import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    if np.ndim(X)<2 or np.shape(X)[0]<2:
        return None
    else:
        X = np.asarray(X, dtype=float)
        return np.dot((X - X.mean(axis=0)).T, X - X.mean(axis=0)) / (X.shape[0] - 1)
        pass