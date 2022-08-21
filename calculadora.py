def soma(x, y):
    """Soma x e y
    >>> soma(1, 1)
    2
    """
    assert isinstance(x, (int, float)), 'Os valores precisam ser números'
    assert isinstance(y, (int, float)), 'Os valores precisam ser números'
    return x + y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)