import math


class Point:
    """base class so our initial branch can have a parent."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO- make a propagate method that does all the post-creation recursion.


class Branch(Point):

    def __init__(self, parent, dep=1, angle=0, dev=10, dst=100, max_dep=5):

        self.parent = parent

        self.dep = dep
        self.max_dep = max_dep
        self.dev = dev
        # self.pos = pos

        if self.dep == 1:
            self.x, self.y = parent.x, parent.y
        else:
            self.x, self.y = parent.end_x, parent.end_y
            parent.add_child(self)

        self.angle = angle
        self.dst = dst

        self.end_x, self.end_y = self.find_endpoint()

        self.chn = []

        if self.dep < max_dep:
            ch_dst = self.dst - ((1 / self.max_dep) * self.dst)
            child_a = Branch(self,
                             dep=self.dep + 1,
                             dst=int(ch_dst),  # changing these vals
                             angle=self.angle - dev,  # in opposite direction?
                             max_dep=self.max_dep,
                             dev=self.dev)
            child_b = Branch(self,
                             dep=self.dep + 1,
                             dst=int(ch_dst),
                             angle=self.angle + dev,
                             max_dep=self.max_dep,
                             dev=self.dev)
            self.add_child(child_a)
            self.add_child(child_b)

    def inc_angle(self, degrees, dep):
        """Modifies self.angle by angle at depth dep."""
        if dep == self.dep:
            self.angle += degrees
        else:
            for ch in self.chn:
                ch.inc_angle(degrees, dep)

    def inc_tree_angle(self, degrees, min_dep):
        """modifies self.angle, and that of all children, by degrees."""
        if self.dep >= min_dep:
            self.angle += degrees
            if len(self.chn) > 0:
                self.chn[0].inc_tree_angle(-degrees)
                self.chn[0].inc_tree_angle(degrees)

    def inc_dev(self, degrees, dep):
        """Modifies self.dev by degrees at depth dep."""
        if dep == self.dep:
            self.dev += degrees
        else:
            for ch in self.chn:
                ch.inc_dev(degrees, dep)

    def inc_tree_dev(self, degrees):
        self.dev += degrees
        for ch in self.chn:
            ch.inc_tree_dev(degrees)

    def set_position(self, x, y):
        """Changes self.x and self.y to new values."""
        self.x, self.y = x, y

    def add_child(self, child_branch):
        """Adds a child branch."""
        self.chn.append(child_branch)

    @staticmethod
    def cartesian(phi):
        """given an angle phi, return a normalised (x, y) vector as a tuple of
        floats."""
        vct_x = round(math.sin(math.radians(phi)), 3)
        vct_y = -round(math.cos(math.radians(phi)), 3)
        return vct_x, vct_y

    def find_endpoint(self):
        """given self.x, self.y, self.angle and self.dst, compute the x,y
        co-ords of the endpoint."""
        vct_x, vct_y = self.cartesian(self.angle)
        end_x = vct_x * self.dst + self.x
        end_y = vct_y * self.dst + self.y
        return end_x, end_y

    def propagate(self):
        """Re-evaluate my own state, and recursively tell child branches
        to update theirs."""
        self.x, self.y = self.get_parent_origin()
        self.end_x, self.end_y = self.find_endpoint()
        if len(self.chn) > 0:
            self.push_angles()
            self.chn[0].propagate()
            self.chn[1].propagate()

    def get_parent_origin(self):
        """get my x and y from parent branch or point."""
        if self.dep == 1:
            return self.parent.x, self.parent.y
        return self.parent.end_x, self.parent.end_y

    def push_angles(self):
        if len(self.chn) > 0:
            self.chn[0].angle = self.angle - self.dev
            self.chn[1].angle = self.angle + self.dev


