from toy_repository.utils.create_toy_data import generate_random_data
# import pdb

def maximum(number: int) -> float:
    """
    generate random data and choose maximum

    Parameters
    ----------
    number : int
        length of random data.

    Returns
    -------
    data_max : float
        maximum of random data.

    """
    data = generate_random_data(number)
    # pdb.set_trace()
    data_max = data.max()
    return data_max


def minimum(number: int) -> float:
    """
    generate random data and choose minimum

    Parameters
    ----------
    number : int
        length of random data.

    Returns
    -------
    data_min : float
        minimum of random data.

    """    
    data = generate_random_data(number)
    data_min = data.min()
    return data_min


if __name__ == "__main__":
    max_data = maximum(number=5)  # 0.5625919433373465
    min_data = minimum(number=5)  # -0.8454361447111014
    
    print(max_data)    
    print(min_data)