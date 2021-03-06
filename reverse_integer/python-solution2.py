class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1

        if x < 0:
            x = -x
            multiplier = -1

        reverted = int(str(x)[::-1])
        reverted *= multiplier

        if reverted > 2147483647 or reverted < -2147483647:
            return 0

        return reverted
