import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x_arr = np.asarray(x, dtype=float)

    sigma = np.where(
        x_arr >= 0,
        1 / (1 + np.exp(-x_arr)),
        np.exp(x_arr) / (1 + np.exp(x_arr))
    )

    return sigma * x_arr