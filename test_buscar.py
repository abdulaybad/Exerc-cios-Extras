import buscar
import pytest
def test_buscar():
    assert buscar.busca(123456789) != 445576480


def test_buscar2():
    assert buscar.busca(252140711) == ['252140711']
