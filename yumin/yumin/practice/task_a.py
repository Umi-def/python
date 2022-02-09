class Abekobe(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num - other.num


"""
    あべこべクラス
    四則演算をあべこべにする
    >>> abekobe = Abekobe(5)
    >>> abekobe + 1
    4
    # 足し算なら引き算に
    >>> abekobe - 1
    6
    >>> abekobe * 5
    1
    # 掛け算なら割り算に
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
