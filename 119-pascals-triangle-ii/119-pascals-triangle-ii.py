from scipy.special import binom
from math import ceil

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        return [int(ceil(binom(rowIndex, i))) for i in range(rowIndex + 1)]