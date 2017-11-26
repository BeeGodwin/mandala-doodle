import random
import math
import numpy


class Branch:

    def __init__(self, ori=[0, 0], vct=(0, -1), dist=1.0, n=6, p=0.5, dep=0):

        max_depth = 3
        self.ori = ori
        self.vct = vct
        self.dist = dist
        self.n = n
        self.dens = self.dist / self.n
        self.p = p
        self.dep = dep + 1

        self.angles = self.get_angles()
        self.nodes = self.place_nodes()

        self.branches = []
        if self.dep < max_depth:
            self.branches = [self.place_branches(node) for node in self.nodes]

    def place_nodes(self):
        """returns a list of (x, y) tuples of points along this branch. dens says
        how many pixels apart nodes should be. prob is the likelihood of a given
        node being added to the returned list."""
        nodes = []
        x_gap, y_gap = self.vct[0] * self.dens, self.vct[1] * self.dens
        node = (self.ori[0] + x_gap, self.ori[1] + y_gap)
        for i in range(int((self.dist // self.dens)) - 1):
            if self.choose():
                nodes.append(node)
            node = (node[0] + x_gap, node[1] + y_gap)
        return nodes

    def get_angles(self):
        """returns a list of tuples of (x, y) tuples, describing normalised
        vectors of the angles that the branches off this branch will produce."""
        my_angle = self.polar(self.vct)
        pairs = (self.n - 1) // 2
        angles = []
        angle_inc = 360 / self.n
        for i in range(pairs):
            pair = [my_angle + angle_inc * (i + 1), my_angle - angle_inc * (i + 1)]
            angles.append([self.cartesian(pair[0]), self.cartesian(pair[1])])
        return angles

    def choose(self):
        """uses self.prob to choose true/false."""
        # if self.dist < self.dens:
        #     return False
        if random.random() < self.p:
            return True
        else:
            return False

    def place_branches(self, node):
        """instantiates a pair(s) of new branches at the given node, and returns
        a list of pairs of branches."""
        if len(self.angles) == 1:
            branches = self.branch_gen(node, self.angles[0])
            return branches
        else:
            j = random.randrange(0, len(self.angles) - 1)
            branches = self.branch_gen(node, self.angles[j])
        return branches

    def branch_gen(self, node, angles):
        """parametrises & instantiates one pair of new branches."""
        sd = random.randrange(random.getrandbits(32))
        _len = self.dist - self.dens
        _den = self.dens
        if self.choose():
            _len /= 2
            _den /= 2

        random.seed(sd)
        branch_a = Branch(ori=node, vct=angles[0], dist=_len, p=self.p, n=self.n, dep=self.dep)
        # print('New branch at {} with vec {} and leng {}'.format(branch_a.ori, branch_a.vec, branch_a.leng))
        random.seed(sd)
        branch_b = Branch(ori=node, vct=angles[1], dist=_len, p=self.p, n=self.n, dep=self.dep)
        # print('New branch at {} with vec {} and leng {}'.format(branch_b.ori, branch_b.vec, branch_b.leng))
        return [branch_a, branch_b]

    @staticmethod
    def polar(vct):
        """given a normalised (x, y) vector, return its angle (with 0 being
        considered vertical, on a scale 0-359.99.)"""
        phi = math.degrees(numpy.arctan2(vct[0], -vct[1]))
        if vct[0] < 0:
            phi += 360
        return round(phi, 3)

    @staticmethod
    def cartesian(phi):
        """given an angle phi, return a normalised (x, y) vector as a tuple of
        floats."""
        x = round(math.sin(math.radians(phi)), 3)
        y = -round(math.cos(math.radians(phi)), 3)
        return x, y

    def move(self, move_vct):
        """move origin by move_vct, update node positions,
        and pass to children."""
        self.ori[0] += move_vct[0]
        self.ori[1] += move_vct[1]
        # do the same for all my node positions
        # then pass the node positions downstream

    def rotate(self, angle):
        """rotate branch by angle. Recalculate node positions,
        pass to children"""
        my_angle = self.polar(self.vct)
        my_angle += angle
        self.vct = self.cartesian(my_angle)
        # more loopage
