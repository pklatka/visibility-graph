import numpy as np


def get_intersect(a1, a2, b1, b2):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    # Code from: https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
    s = np.vstack([a1, a2, b1, b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))

    intersection_point = (x/z, y/z)

    if min([b1, b2], key=lambda x: x[0])[0] <= intersection_point[0] <= max([b1, b2], key=lambda x: x[0])[0] and min([b1, b2], key=lambda x: x[1])[1] <= intersection_point[1] <= max([b1, b2], key=lambda x: x[1])[1]:
        return intersection_point

    return (float('inf'), float('inf'))


def get_intersection_point(p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float], p4: tuple[float, float]) -> tuple[float, float]:
    """Calculate intersection point of line p1p2 and segment p3p4 with formula from: 
        https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection

    :param tuple[float, float] p1: First point on line
    :param tuple[float, float] p2: Second point on line
    :param tuple[float, float] p3: Start point defining segment
    :param tuple[float, float] p4: End point defining segment
    :return tuple[float, float]: Intersection point
    """

    denominator = (p1[0] - p2[0])*(p3[1] - p4[1]) - \
        (p1[1] - p2[1]) * (p3[0] - p4[0])

    if denominator == 0:
        return (np.inf, np.inf)

    x_numerator = (p1[0]*p2[1] - p1[1]*p2[0])*(p3[0]-p4[0]) - \
        (p1[0] - p2[0])*(p3[0]*p4[1] - p3[1]*p4[0])
    y_numerator = (p1[0]*p2[1] - p1[1]*p2[0])*(p3[1]-p4[1]) - \
        (p1[1] - p2[1])*(p3[0]*p4[1] - p3[1]*p4[0])

    intersection_point = (x_numerator/denominator, y_numerator/denominator)

    if p3[0] < p4[0]:
        segment_boundary_min_x = p3[0]
        segment_boundary_max_x = p4[0]
    else:
        segment_boundary_min_x = p4[0]
        segment_boundary_max_x = p3[0]

    if p3[1] < p4[1]:
        segment_boundary_min_y = p3[1]
        segment_boundary_max_y = p4[1]
    else:
        segment_boundary_min_y = p4[1]
        segment_boundary_max_y = p3[1]

    if segment_boundary_min_x <= intersection_point[0] <= segment_boundary_max_x and segment_boundary_min_y <= intersection_point[1] <= segment_boundary_max_y:
        return intersection_point

    return (np.inf, np.inf)


print(get_intersect((0, 0), (5, 0), (2, 2), (2, 1)))
