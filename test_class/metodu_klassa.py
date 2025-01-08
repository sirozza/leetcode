
class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y


class Point2:
    x = 0
    y = 0


pt = Point()
pt.set_coords(1, 3)
print(pt.__dict__)