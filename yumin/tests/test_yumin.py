import pytest
from yumin import __version__
from yumin.practice.task_a import Abekobe


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
