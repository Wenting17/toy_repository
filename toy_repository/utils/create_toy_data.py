import numpy as np

def generate_random_data(number: int) -> np.ndarray:
    """
    generate random data by numpy

    Parameters
    ----------
    number : int
        length of data.

    Returns
    -------
    data : np.ndarray
        random data.

    """
    np.random.seed(127)
    data = np.random.randn(number)
    return data


if __name__ == "__main__":
    data = generate_random_data(3)
    print(data)  # array([-0.57180948,  0.02962396,  0.56259194])
