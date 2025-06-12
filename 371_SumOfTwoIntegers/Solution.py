
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF  # 32 bit mask
        maxInt = 2**31 - 1

        while b != 0:
            sum = (a ^ b) & mask  # contain to 32 bits
            carry = (a & b) & mask  # contain to 32 bits
            a = sum
            b = carry << 1

        return a if a <= maxInt else ~(a ^ mask)


solution = Solution()
print(solution.getSum(-1, -6))


# 3 + 2 = 5
# 0 0 1 1
# 0 0 1 0
# -----------
# 0 0 1 0       (a & b) = 2
# -----------
# 0 1 0 0       left shift  << 1 = > 4 => b
# -----------
# 0 0 0 1       a ^ b (XOR) => 1 => a
# -----------
# 0 0 0 0        (a & b) = 0
# -----------
# 0 0 0 0        left shift  << 1 => 0 => b
# -----------
#  0 1 0 1        a ^ b (XOR) => 0 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2 ^0  => 4 +1 = 5

# -1 + 1 = 0
# -1 => 2s complement of 1 => 0 0 0 1 => 1 1 1 0 =>  + 1 => 1 1 1 1 =>
# 1 1 1 1
# 0 0 0 1
# -----------
# 0 0 0 1       ( a & b) = 1
# -----------
# 0 0 1 0       left shift  << 1  => 2  => b
# -----------
# 1 1 1 0       a ^ b (XOR) => 1 => a
