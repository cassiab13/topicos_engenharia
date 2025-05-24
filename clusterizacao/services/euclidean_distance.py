import math
from typing import Tuple

def euclidian_distance(c1: list[Tuple[int, float, float]]) -> float:
    return math.sqrt(
        (c1[0][0] - c1[1][0])**2 +
        (c1[0][1] - c1[1][1])**2 +
        (c1[0][2] - c1[1][2])**2
    )