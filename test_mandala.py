from branch import Branch, Point


def test_find_endpoint():
    p = Point(0, 0)
    b = Branch(p)
    assert b.find_endpoint() == (0, -100)
    b = Branch(p, dst=50)
    assert b.find_endpoint() == (0, -50)
    b = Branch(p, dst=50, angle=180)
    assert b.find_endpoint() == (0, 50)

