import math
from typing import Tuple

def euclidian_distance(c1: Tuple[int, float, float], c2: Tuple[int, float, float]) -> float:
    return math.sqrt(
        (c1[0] - c2[0])**2 +
        (c1[1] - c2[1])**2 +
        (c1[2] - c2[2])**2
    )