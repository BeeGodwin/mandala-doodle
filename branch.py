import math
import numpy

class Point:
    """base class so our initial branch can have a parent."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Branch(Point):

    def __init__(self, parent, dep=1, angle=0, dst=100, maxdep=7):

        self.dep = dep

        if self.dep == 1:
            self.x, self.y = parent.x, parent.y
        else:
            self.x, self.y = parent.end_x, parent.end_y
            # also tell my parent I am its child

        self.angle = angle
        self.dst = dst

        # self.end_x, self.end_y = # some function

        self.chn = []

        if self.dep < maxdep:
            pass  # recurse

    def set_angle(self):
        """gets my parent angle and my current relative angle to compute
        my absolute angle."""
        # if I'm depth 1, I have no parent and my relative angle is absolute
        # otherwise compute current relative angle
        # set my new end point
        pass

    def add_child(self, child_branch):
        self.chn.append(child_branch)

