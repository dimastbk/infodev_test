def some_func(a, b=None):
    b = b or []
    b.append(a)
    return b


if __name__ == '__main__':
    assert some_func(6) == [6]
    assert some_func(7) == [7]
    assert some_func(5, [1]) == [1, 5]
