import math
# terminology
# number = digits[n] * positions[n] + digits[n-1] * positions[n-1] + ...
#           digits[0] * positions[0]

# example: 10 -> radix = 2
# 10 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 => 1010
def convert_dec_to(dec: int, base: int = 10) -> str:
    max_position = find_max_position(dec, base)
    positions = [pow(base, p) for p in range(max_position, -1, -1)]
    number = dec
    digits = []
    for p in positions:
        digit = math.floor(number / p) % base
        digits.append(digit)

    return digits

def find_max_position(dec: int, base: int = 10) -> int:
    val = 0
    position = 0

    while dec > val:
        val = pow(base, position)

        if dec < val:
            break

        position += 1

    max_position = position - 1 if position > 1 else 0
    return max_position


# print(int('1010', base=2))
# print(find_max_position(0, base=2) == 0)
# print(find_max_position(1, base=2) == 0)
# print(find_max_position(2, base=2) == 1)
# print(find_max_position(3, base=2) == 1)
# print(find_max_position(10, base=2) == 3)
# print(find_max_position(16, base=2) == 4)

print(convert_dec_to(10, base=2))
