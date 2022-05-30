class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        current_sum = divisor

        while current_sum <= dividend:
            current_quotient = 1
            while current_sum + current_sum <= dividend:
                current_sum += current_sum
                current_quotient += current_quotient

            dividend -= current_sum
            current_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(quotient if positive else -quotient, -2147483648))
