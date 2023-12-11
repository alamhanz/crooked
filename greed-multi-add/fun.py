from typing import Optional
import random
import numpy as np


class Solution:
    """_summary_"""

    def diamondProb(self, t, x, y) -> list:
        """_summary_

        Args:
            t (_type_): _description_
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            list: _description_
        """
        # if len(solutions) == 0:
        #     solutions.append(prefix_used+" 1")
        # else:
        #     prev_prefix, prev_k = solutions[-1].split(' ')
        #     if  prev_prefix == prefix_used:
        #         solutions[-1] = " ".join([prev_prefix,str(int(prev_k)+1)])
        #     else:
        #         solutions.append(prefix_used+" 1")

        return point


import math


def solution(t, x, y):
    # if x+1 > t and y > t:
    #     return ["no_solution"]
    # else:
    solutions = []
    m0 = 0
    m = 0
    k = 0
    prefix_prev = ["operator_add", "operator_multiply"]
    lg = int(math.log(t, y))  ## total multiplication
    while t > 1:
        if t % y == 0 and y != 1:
            lg0 = lg
            while t / (y**lg0) != int(t / (y**lg0)) and lg0 >= 1:
                lg0 -= 1

            t = t / (y**lg0)
            lg -= lg0
            iter = lg0
            m = 0
        elif t - x >= 1:
            t = t - x
            iter = 1
            m = 1
        else:
            break

        if m0 == m:
            k = k + iter
        else:
            if k != 0:
                solutions.append(" ".join([prefix_prev[m], str(int(k))]))
            m0 = m
            k = iter

    solutions.append(" ".join([prefix_prev[abs(m - 1)], str(int(k))]))

    if t > 1:
        return ["no_solution"]
    else:
        solutions.reverse()
        return solutions
