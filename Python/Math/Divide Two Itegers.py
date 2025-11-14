class Solution:
    
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow for the special case:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # 32-bit overflow

        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while(dividend >= divisor):
            temp_d = divisor
            i = 1
            while dividend >= temp_d:
                dividend -= temp_d
                result += i
                temp_d += temp_d
                i += i

        return -result if negative else result
