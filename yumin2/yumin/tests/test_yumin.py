import pytest
from yumin import __version__
from yumin.practice.task_a import Abekobe
from yumin.practice.task_b import GeckoDriver


def test_version():
    assert __version__ == "0.1.0"


def test_task_a():
    abekobe = Abekobe(5)
    # 足し算
    assert abekobe + 1 == 4
    # 引き算
    assert abekobe - 1 == 6
    # 掛け算
    assert abekobe * 5 == 1
    # 割り算
    assert abekobe / 5 == 25
    # 0入力掛け算
    with pytest.raises(ValueError):
        _ = abekobe * 0


def test_task_b():
    driver = GeckoDriver()
    # ping
    code, res = driver.ping()
    assert code == 200
    assert isinstance(res, dict)
    # coins/list
    code, res = driver.get_coins_list()
    assert code == 200
    assert isinstance(res, list)
    for coin in res:
        assert isinstance(coin, dict)
    # get symbols
    symbols = driver.get_coins_symbol()
    assert isinstance(symbols, list)
    assert len(symbols) > 100
