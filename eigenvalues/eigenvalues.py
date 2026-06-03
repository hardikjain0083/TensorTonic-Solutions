import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    Returns None if the input is not a valid square numeric matrix.
    """
    try:
        # This will throw a ValueError if the input rows are inhomogeneous
        matrix = np.asarray(matrix, dtype=float)
    except ValueError:
        return None

    # Now that it's safely a standard numpy array, check your other constraints
    if np.ndim(matrix) < 2 or np.shape(matrix)[0] != np.shape(matrix)[1] or np.shape(matrix)[0] < 1:
        return None
    
    try:
        return np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        # Handles cases where the matrix cannot be decomposed (e.g., contains NaNs/Infs)
        return None
        