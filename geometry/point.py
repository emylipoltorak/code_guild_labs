from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '{},{}'.format(self.x, self.y)


def distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def check_radius(p, r, c):
    count = 0
    for point in c:
        if distance(point, p) <= r:
            count += 1
    return count


if __name__ == '__main__':
    point1 = Point(3, 6)
    print(point1)
    point1.move(2, 2)
    print(point1)
