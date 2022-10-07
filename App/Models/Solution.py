from dataclasses import dataclass
from time import monotonic

@dataclass(frozen= False, order= False)
class Solution:
    method: str
    n_queens: int
    total: int = -1
    runtime: float = monotonic()

    def _end_timestamp(self):
        delta = monotonic() - self.runtime
        self.runtime = round(delta, 7)
        self.timestamp = str(self.runtime)
        if (len(self.timestamp) >= 32):
            self.timestamp = self.timestamp[:32]

    def update_total(self, total: int):
        """
        Sets the total solutions for n queens and stops its execution timer
        """
        self.total = total
        self._end_timestamp()