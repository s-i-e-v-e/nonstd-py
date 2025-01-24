from nonstd.data import List, Maybe

def test_list():
    xs = List([1, 2, 3])
    assert xs.head().just() == 1
    assert xs.last().just() == 3
    assert List([1]).head().just() == List([1]).last().just()

    assert xs == (xs.reverse().reverse())

def test_maybe():
    apple = Maybe('apple')
    assert apple == Maybe('apple')
    assert Maybe(1).map(lambda x: x+1) == Maybe(2)
