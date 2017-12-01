from branch import Branch, Point
from colour import Colours

def test_find_endpoint():
    p = Point(0, 0)
    b = Branch(p)
    assert b.find_endpoint() == (0, -100)
    b = Branch(p, dst=50)
    assert b.find_endpoint() == (0, -50)
    b = Branch(p, dst=50, angle=180)
    assert b.find_endpoint() == (0, 50)


def test_populate_palette():
    c = Colours((0, 0, 0), (255, 255, 255))
    pal = c.populate_palette()
    assert pal[0] == (0, 0, 0)
    assert len(pal) == 1024
    assert pal[512] == (255, 255, 255)
    assert pal[256] == (127, 127, 127)
    assert pal[768] == (127, 127, 127)
    assert pal[1023] == (0, 0, 0)