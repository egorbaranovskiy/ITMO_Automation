def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# def test_fail():
#     assert 'test' == 'testing'


#функция для проверки несоответствия
def test_not():
    a = 'test'
    b = 'testing'
    assert not a==b


def test_list():
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    assert not a==b