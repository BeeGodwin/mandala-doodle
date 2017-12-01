class Colours:

    def __init__(self, *args):

        self.colours = []
        self.range = 1024

        for col in args:
            self.colours.append(col)

        self.palette = self.populate_palette()

    def populate_palette(self):
        """returns a list of (r, g, b) values forming a cycle between all
        the colours in self.colours. Interpolates to create a list of length
        self.range."""
        palette = []
        delta_range = self.range // len(self.colours)
        for j in range(len(self.colours)):
            col_a = self.colours[j]
            col_b = self.colours[(j + 1) % len(self.colours)]
            col_change = [r, g, b] = [col_b[k] - col_a[k] for k in range(3)]
            for i in range(delta_range):
                rgb = [int(col_a[k] + (col_change[k] / delta_range) * i) for k in range(3)]
                palette.append((rgb[0], rgb[1], rgb[2]))
        return palette
