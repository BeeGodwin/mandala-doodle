import math
import numpy

class Point:
    """base class so our initial branch can have a parent."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Branch(Point):

    def __init__(self, parent, dep=1, angle=0, dev=10, dst=100, max_dep=7):

        self.dep = dep
        self.max_dep = max_dep
        self.dev = dev

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
            child_a = Branch(self,
                             dep=self.dep + 1,
                             dst=int(self.dst / 2),
                             angle=self.angle - dev,
                             max_dep=self.max_dep,
                             dev=self.dev)
            child_b = Branch(self,
                             dep=self.dep + 1,
                             dst=int(self.dst / 2),
                             angle=self.angle + dev,
                             max_dep=self.max_dep,
                             dev=self.dev)
            self.add_child(child_a)
            self.add_child(child_b)

    def set_angle(self):
        """gets my parent angle and my current relative angle to compute
        my absolute angle."""
        # if I'm depth 1, I have no parent and my relative angle is absolute
        # otherwise compute current relative angle
        # set my new end point
        pass

    def add_child(self, child_branch):
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
        coords of the endpoint."""
        vct_x, vct_y = self.cartesian(self.angle)
        end_x = vct_x * self.dst + self.x
        end_y = vct_y * self.dst + self.y
        return end_x, end_y


