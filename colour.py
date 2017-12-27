import random


class Colours:

    def __init__(self, *args):
        """Takes a list of colour 3-tuples."""
        self.colours = []
        self.range = 1024

        self.objects = {}

        for col in args:
            self.colours.append(col)

        self.palette = self.populate_palette()

    def populate_palette(self):
        """returns a list of (r, g, b) values forming a cycle between all
        the colours in self.colours. Interpolates to create a list of length
        self.range. self.colours must not be an empty list, and needs at least
        two values for this code to make any difference."""
        palette = []
        delta_range = self.range // len(self.colours)
        for j in range(len(self.colours)):
            col_a = self.colours[j]
            col_b = self.colours[(j + 1) % len(self.colours)]
            col_change = [r, g, b] = [col_b[k] - col_a[k] for k in range(3)]
            for i in range(delta_range):
                rgb = [int(col_a[k] + (col_change[k] / delta_range) * i) for k in range(3)]
                palette.append((rgb[0], rgb[1], rgb[2]))
        while len(palette) < self.range:
            palette.append(palette[-1])
        return palette

    def set_range(self, _range):
        """Pass in a new value for range and rebuild the palette."""
        self.range = _range
        self.populate_palette()

    def assign_colour(self, obj, col_id):
        """Assigns a colour to an object by making a key/val pair in self.objects,
        where the key is the object and the value is an integer in the range 0-self.range."""
        self.objects[obj] = col_id

    def get_colour(self, obj):
        """Returns the colour id associated with obj. If obj doesn't have a colour, it
        gets a random colour id."""
        if obj in self.objects.keys():
            return self.objects[obj]
        else:
            self.assign_colour(obj, random.randrange(0, self.range))
            return self.palette[self.objects[obj]]

    def inc_colours(self, i):
        """Increments all colour id integers by i."""
        for obj in self.objects.keys():
            self.objects[obj] += i
            self.objects[obj] %= self.range
