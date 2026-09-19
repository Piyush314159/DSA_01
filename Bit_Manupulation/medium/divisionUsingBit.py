class Sollution:
    def divide(self, dividend: int, divisor: int ) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # false != false -> False ; false != true -> True ; true != true -> False
        negative = (dividend < 0) != (divisor < 0)

        dvd, dvs = abs(dividend), abs(divisor)

        quotient = 0
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            while (temp << 1) > dvd:    #left shift
                temp <<= 1
                multiple <<= 1

            dvd -= temp
            
            quotient += multiple
        result = -quotient if negative else quotient

        # Clamp to 32-bit signed range
        return max(INT_MIN, min(INT_MAX, result))

s = Sollution()
print(s.divide(-43, -8))