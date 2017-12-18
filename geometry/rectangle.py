from point import Point


class Rectangle:
    def __init__(self, top_left, l, w):
        self.top_left = top_left
        self.l = l
        self.w = w
        self.top_right = Point(self.top_left.x, self.top_left.y + self.l)
        self.bottom_left = Point(self.top_left.x - self.w, self.top_left.y)
        self.bottom_right = Point(self.top_right.x - self.w, self.top_right.y)
        self.center = Point(self.bottom_left.x + (self.w/2), self.bottom_left.y + (self.l/2))

    def __repr__(self):
        return 'Top left: {}\nLength: {}\nWidth:{}'.format(self.top_left, self.l, self.w)

    def contains(self, point):
        return self.bottom_left.y <= point.y <= self.bottom_right.y and self.bottom_left.x <= point.x <= self.top_left.x


if __name__ == '__main__':
    rect = Rectangle(Point(4, 0), 4, 4)
    print(rect)
    print(rect.center)
    print(rect.contains(rect.center))
