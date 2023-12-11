from typing import Optional
import random
import numpy as np


class Solution:
    """_summary_"""

    def diamondProb(self, xs, ys, xe, ye) -> np.array:
        """_summary_

        Args:
            xs (_type_): _description_
            ys (_type_): _description_
            xe (_type_): _description_
            ye (_type_): _description_

        Returns:
            float: _description_
        """
        steps = [[-1, 0], [0, -1], [0, 0], [0, 1], [1, 0]]
        steps = [np.array(i) for i in steps]
        step = random.choice(steps)

        point = np.array([xs, ys])
        endpoint = np.array([xe, ye])
        k = 0
        while point != endpoint and point in steps:
            point = point + step

        # 4/13

        return point


def solution(xs, ys, xe, ye):
    print("check the xs,ye=0,0 or not. if yes then 1, else 0.25")
    if xe == ye == 0:
        return 0.25
    else:
        p = 1 if xs == ys == 0 else 0.25
        return p * (4 / 13)
