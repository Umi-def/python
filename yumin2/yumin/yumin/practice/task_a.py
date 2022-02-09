class Abekobe(object):
    """
    あべこべクラス
    四則演算をあべこべにする
    >>> abekobe = Abekobe(5)
    >>> abekobe + 1
    4
    >>> abekobe - 1
    6
    >>> abekobe * 5
    1
    >>> abekobe / 5
    25
    >>> abekobe * 0
    ValueError

    Parameters
    ----------
    number : int or float

    Returns
    -------

    Raises
    ------
    ValueError
        もし*の時0を入力したら発する
    """
