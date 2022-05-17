import sys

# maximum integer to represent x-infinity
INT_MAX = 100000


def direction(x: tuple, y: tuple, z: tuple):
    """
        Returns the orientation direction of ordered points x,y,x
        by comparing the signs of the gradients

        Parameters:
        x(int): point as tuple
        y(int): point as tuple
        z(int): point as tuple

        Returns:
        0: points are collinear
        1: Clockwise direction
        2: Anti-clockwise direction   
    """
    sign = (((y[1] - x[1]) * (z[0] - y[0])) -
            ((y[0] - x[0]) * (z[1] - y[1])))

    if sign == 0:
        return 0
    elif sign > 0:
        return 1
    else:
        return 2


def on_line_segment(x: tuple, y: tuple, z: tuple):
    """
        If points x,y,z are colinear points, this function checks 
        if y lies on the line segement x-z

        Parameters:
        x(int): point as tuple
        y(int): point as tuple
        z(int): point as tuple

        Returns:
        True: if y lies on the line segment x-z
        False: y is outside the line segment x-z
    """
    if ((y[0] <= max(x[0], z[0])) and
        (y[0] >= min(x[0], z[0])) and
        (y[1] <= max(x[1], z[1])) and
            (y[1] >= min(x[1], z[1]))):
        return True
    return False


def if_intersect(p1: tuple, q1: tuple, p2: tuple, q2: tuple):
    """
        Checks if the line segments p1-q1 and p2-q2 intersect

        Parameters:
        p1(int): point as tuple
        q1(int): point as tuple
        p2(int): point as tuple
        p2(int): point as tuple

        Returns:
        True: line segments p1-q1 and p2-q2 intersect
        False: line segments p1-q1 and p2-q2 does not intersect
    """
    # different combinations needed to check all possible cases
    o1 = direction(p1, q1, p2)
    o2 = direction(p1, q1, q2)
    o3 = direction(p2, q2, p1)
    o4 = direction(p2, q2, q1)

    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    elif (o1 == 0) and (on_line_segment(p1, p2, q1)):
        return True

    # p1, q1 and p2 are collinear and q2 lies on segment p1q1
    elif (o2 == 0) and (on_line_segment(p1, q2, q1)):
        return True

    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    elif (o3 == 0) and (on_line_segment(p2, p1, q2)):
        return True

    # p2, q2 and q1 are collinear and q1 lies on segment p2q2
    elif (o4 == 0) and (on_line_segment(p2, q1, q2)):
        return True

    else:
        return False


def intersect_counter(polygon: list, point: tuple):
    """
        Returns the number of intersection of a test point with all
        possible sides of a polygon

        Parameters:
        polygon(int): list of tuples which specifies the shape of polygon
        point(int): test point as tuple

        Returns:
        counter: number of intersections encountered
    """
    n = len(polygon)
    # point at arbitrary infinity
    point_inf = (INT_MAX, point[1])
    i = counter = 0

    if n < 3:
        print("A polygon must have more than 3 vertices!")
        return

    while True:
        next = (i + 1) % n

        # Checks if the line segment point-point_inf intersects with the
        # line segment polygon[i]-polygon[next]
        if (if_intersect(polygon[i], polygon[next], point, point_inf)):

            # if the test point is colinear with the line segment polygon[i]-polygon[next],
            # check if it lies on that line segment
            if direction(polygon[i], point, polygon[next]) == 0:
                if on_line_segment(polygon[i], point, polygon[next]) == True:
                    return counter
                else:
                    return counter
            counter += 1

        i = next

        if (i == 0):
            break

    return counter


def is_inside_shape(polygon: list, cut: list, point: tuple):
    """
        Check if a given point lies in a polygon with cutouts

        Parameters:
        polygon(int): list of tuples which specifies the shape of polygon
        cut(int): list of cuts defined in the given text file 
        point(int): test point as tuple

        Returns:
        1: If point lies in polygon
        0: If point lies outside of polygon
    """
    counter_1 = intersect_counter(polygon, point)
    counter_2 = 0
    for i in range(len(cut)):
        counter_2 += intersect_counter(cut[i], point)
    counter_sum = counter_1 + counter_2

    if ((counter_sum % 2 == 1) or (counter_sum == 0)):
        print("Point ({}, {}) is INSIDE the shape".format(point[0], point[1]))
        return 1

    else:
        print("Point ({}, {}) is OUTSIDE the shape".format(point[0], point[1]))
        return 0


# Driver code
if __name__ == '__main__':
    # command-line arguments to grab text file and test point
    text_string = sys.argv[1]
    test_point = (int(sys.argv[2]), int(sys.argv[3]))

    polygon = []
    cut_list = []

    with open(text_string) as file:

        for line in file:
            if line.startswith('C'):
                break

            if not line.startswith('O'):
                polygon.append(tuple(map(int, line.split())))

    with open(text_string) as file1:

        for line1 in file1:
            cut = []
            if line1.startswith('C'):
                for i in line1:
                    if i.isdigit():
                        a = int(i)

                for i in range(a):
                    cut.append(tuple(map(int, next(file1).split())))

                cut_list.append(cut)

    # print(polygon)
    # print(cut_list)
    is_inside_shape(polygon, cut_list, test_point)
