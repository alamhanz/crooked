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


import numpy as np


def solution(your_company_name, other_company_names, other_company_prices):
    other_companies = [list(i) for i in other_company_names]
    all_chars = set().union(*other_companies)
    your_chars = set(your_company_name)

    print("check the charachters")
    if len(your_chars - all_chars) > 0:
        return -1

    else:
        Mc = []
        all_chars = tuple(all_chars)
        for name in other_companies:
            Mc.append([name.count(c) for c in all_chars])

        Mc = np.array(Mc).transpose()
        val = np.array([your_company_name.count(c) for c in all_chars]).reshape(-1, 1)

        combination, error, _, _ = np.linalg.lstsq(Mc, val, rcond=None)
        combination = combination.reshape(-1)
        print(combination)
        print(np.mean(error))

        if np.mean(error) >= 0.01:
            return -1
        else:
            total_price = sum(
                [a * b for a, b in zip(combination, other_company_prices)]
            )

        return total_price
