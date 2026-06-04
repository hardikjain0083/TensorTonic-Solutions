import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    Assumes rows are observations and columns are features.
    """
    X = np.asarray(X, dtype=float)
    
    # Check for valid dimensions (need at least 2 samples and 2D array)
    if X.ndim < 2 or X.shape[0] < 2:
        return None

    # 1. Mean-center the data
    X_centered = X - X.mean(axis=0)
    
    # 2. Calculate the sample covariance matrix
    # Dividing by (N - 1) for sample covariance
    N = X.shape[0]
    cov_matrix = np.dot(X_centered.T, X_centered) / (N - 1)
    
    # 3. Calculate standard deviations for all columns
    # Use ddof=1 to match the (N - 1) sample covariance division
    std_devs = np.std(X, axis=0, ddof=1)
    
    # 4. Create a matrix of std_dev products (outer product)
    std_matrix = np.outer(std_devs, std_devs)
    
    # 5. Divide covariance matrix by standard deviation matrix
    # Using np.errstate to safely handle division by zero (e.g., zero variance)
    with np.errstate(divide='ignore', invalid='ignore'):
        corr_matrix = cov_matrix / std_matrix
        
        # Replace NaNs (caused by 0/0 division) with 0 or 1 where appropriate
        corr_matrix[~np.isfinite(corr_matrix)] = None
        
    return corr_matrix