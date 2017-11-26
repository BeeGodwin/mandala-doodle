from branch import Branch


def test_polar():
    branch = Branch()
    eps = 0.001
    assert abs(branch.polar((0.707, -0.707)) - 45) < eps
    assert abs(branch.polar((0.707, 0.707)) - 135) < eps
    assert abs(branch.polar((-0.707, 0.707)) - 225) < eps
    assert abs(branch.polar((-0.707, -0.707)) - 315) < eps


def test_cartesian():
    branch = Branch()
    eps = 0.001
    assert abs(branch.cartesian(45)[0] - 0.707) < eps
    assert abs(branch.cartesian(45)[1] - -0.707) < eps
    assert abs(branch.cartesian(135)[0] - 0.707) < eps
    assert abs(branch.cartesian(135)[1] - 0.707) < eps
    assert abs(branch.cartesian(225)[0] - -0.707) < eps
    assert abs(branch.cartesian(225)[1] - 0.707) < eps
    assert abs(branch.cartesian(315)[0] - -0.707) < eps
    assert abs(branch.cartesian(315)[1] - -0.707) < eps


def test_get_angles():
    branch = Branch(n=4)
    assert branch.angles[0] == [(1, 0), (-1, 0)]
    assert len(branch.angles) == 1
    branch = Branch(n=6)
    assert branch.angles[0] == [(0.866, -0.5), (-0.866, -0.5)]
    assert branch.angles[1] == [(0.866, 0.5), (-0.866, 0.5)]
    assert len(branch.angles) == 2
    branch = Branch(n=7)
    assert len(branch.angles) == 3
    assert branch.angles[0] == [(0.782, -0.623), (-0.782, -0.623)]


def test_choose():
    branch = Branch(p=1)
    assert branch.choose()
    branch.p = 0
    assert not branch.choose()


def test_create_nodes():
    branch = Branch(dist=30, n=3, p=1)
    nodes = branch.place_nodes()
    assert nodes == [(0, -10), (0, -20)]
    branch = Branch(dist=40, n=4, p=1)
    nodes = branch.place_nodes()
    assert nodes == [(0, -10), (0, -20), (0, -30)]
    branch = Branch(dist=100, p=0)
    nodes = branch.place_nodes()
    assert nodes == []
    branch = Branch(dist=30, n=3, vct=(0, 1), p=1)
    nodes = branch.place_nodes()
    assert nodes == [(0, 10), (0, 20)]