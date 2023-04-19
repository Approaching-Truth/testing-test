import pytest
from addtest.add import add


@pytest.mark.parametrize("x, y, result", [
    (2, 2, 4),
    (2, 2, 4),
    (2, 2, 4),
])
def test_addition(x, y, result):
    assert add(x, y) is result
